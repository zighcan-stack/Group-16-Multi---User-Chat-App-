import socket
import threading

# Custom exception
class NetworkError(Exception):
    pass

class ChatServer:
    def __init__(self, host="0.0.0.0", port=12345):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = {}  # {conn: username}

    def start(self):
        try:
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(5)
            print(f"✅ Server started on {self.host}:{self.port}")

            while True:
                conn, addr = self.server_socket.accept()
                print(f"🔗 New connection from {addr}")
                threading.Thread(target=self.handle_client, args=(conn,)).start()
        except Exception as e:
            raise NetworkError(f"Server error: {e}")

    def broadcast(self, msg, sender_conn):
        for conn in self.clients.keys():
            if conn != sender_conn:
                try:
                    conn.sendall(msg.encode("utf-8"))
                except:
                    conn.close()
                    del self.clients[conn]

    def handle_client(self, conn):
        try:
            username = conn.recv(1024).decode("utf-8")
            self.clients[conn] = username
            self.broadcast(f"📢 {username} joined the chat!", conn)

            while True:
                msg = conn.recv(1024).decode("utf-8")
                if not msg:
                    break
                print(f"{username}: {msg}")
                self.broadcast(f"{username}: {msg}", conn)
        except:
            pass
        finally:
            username = self.clients.get(conn, "Unknown")
            print(f"❌ {username} disconnected")
            self.broadcast(f"❌ {username} left the chat.", conn)
            conn.close()
            if conn in self.clients:
                del self.clients[conn]


if __name__ == "__main__":
    server = ChatServer()
    server.start()
