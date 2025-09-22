# server.py
import socket
import threading
import sys

class ChatServer:
    def __init__(self, host="0.0.0.0", port=12345):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.clients = {}  # {conn: username}
        self.lock = threading.Lock()

    def start(self):
        try:
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(5)
            print(f"✅ Server started on {self.host}:{self.port}")

            while True:
                conn, addr = self.server_socket.accept()
                print(f"🔗 New connection from {addr}")
                threading.Thread(target=self.handle_client, args=(conn,), daemon=True).start()
        except Exception as e:
            print(f"❌ Server failed: {e}")
            sys.exit(1)

    def broadcast(self, msg, sender_conn=None):
        with self.lock:
            disconnected = []
            for conn in list(self.clients.keys()):
                if conn != sender_conn:
                    try:
                        conn.sendall(msg.encode("utf-8"))
                    except:
                        disconnected.append(conn)
            for conn in disconnected:
                conn.close()
                self.clients.pop(conn, None)

    def send_userlist(self):
        with self.lock:
            users = ",".join(self.clients.values())
            for conn in list(self.clients.keys()):
                try:
                    conn.sendall(f"USERLIST:{users}".encode("utf-8"))
                except:
                    pass

    def handle_client(self, conn):
        try:
            username = conn.recv(1024).decode("utf-8").strip()
            if not username:
                conn.sendall("ERROR: Username cannot be empty.".encode("utf-8"))
                conn.close()
                return

            with self.lock:
                self.clients[conn] = username

            print(f"👤 {username} joined")
            self.broadcast(f"📢 {username} joined the chat!", conn)
            self.send_userlist()

            while True:
                msg = conn.recv(1024).decode("utf-8")
                if not msg:
                    break
                print(f"{username}: {msg}")
                self.broadcast(f"{username}: {msg}", conn)

        except Exception as e:
            print(f"⚠️ Client error: {e}")
        finally:
            with self.lock:
                username = self.clients.get(conn, "Unknown")
                self.clients.pop(conn, None)

            print(f"❌ {username} disconnected")
            self.broadcast(f"❌ {username} left the chat.", conn)
            self.send_userlist()
            conn.close()


if __name__ == "__main__":
    server = ChatServer()
    try:
        server.start()
    except KeyboardInterrupt:
        print("\n🛑 Server shutting down...")
        sys.exit(0)
