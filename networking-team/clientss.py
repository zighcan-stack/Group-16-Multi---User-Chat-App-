import socket
import threading

class NetworkError(Exception):
    pass

class ChatClient:
    def __init__(self, host="127.0.0.1", port=12345, username="Guest"):
        self.host = host
        self.port = port
        self.username = username
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        try:
            self.client_socket.connect((self.host, self.port))
            self.client_socket.sendall(self.username.encode("utf-8"))
            print(f"✅ Connected to server as {self.username}")

            threading.Thread(target=self.receive_messages, daemon=True).start()
        except Exception as e:
            raise NetworkError(f"Connection error: {e}")

    def receive_messages(self):
        while True:
            try:
                msg = self.client_socket.recv(1024).decode("utf-8")
                if msg:
                    print(msg)
            except:
                print("⚠️ Disconnected from server.")
                break

    def send_message(self, msg):
        try:
            self.client_socket.sendall(msg.encode("utf-8"))
        except Exception as e:
            print(f"Send error: {e}")


if __name__ == "__main__":
    username = input("Enter username: ")
    client = ChatClient(username=username)
    client.connect()

    while True:
        msg = input("")
        if msg.lower() == "quit":
            break
        client.send_message(msg)
        
        
