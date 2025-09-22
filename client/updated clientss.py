import socket
import threading
import tkinter as tk
from tkinter import simpledialog, messagebox
from datetime import datetime  # 👈 for timestamps


class ChatClient:
    def __init__(self, host="127.0.0.1", port=12345):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # GUI setup
        self.root = tk.Tk()
        self.root.title("Multi-User Chat")
        self.root.geometry("600x400")

        # Frame for chat + scrollbar
        chat_frame = tk.Frame(self.root)
        chat_frame.pack(side="left", fill="both", expand=True, padx=5, pady=5)

        # Chat messages area
        self.chat_area = tk.Text(chat_frame, bg="white", state="disabled", wrap="word")
        self.chat_area.pack(side="left", fill="both", expand=True)

        # Scrollbar for chat
        scrollbar = tk.Scrollbar(chat_frame, command=self.chat_area.yview)
        scrollbar.pack(side="right", fill="y")
        self.chat_area.config(yscrollcommand=scrollbar.set)

        # Active users panel
        self.user_listbox = tk.Listbox(self.root, bg="lightgray", width=20)
        self.user_listbox.pack(side="right", fill="y", padx=5, pady=5)

        # Message entry box
        self.entry = tk.Entry(self.root, bg="white")
        self.entry.pack(fill="x", padx=5, pady=5)
        self.entry.bind("<Return>", self.send_message)

        # Connect to server
        self.username = simpledialog.askstring("Username", "Enter your username:", parent=self.root)
        if not self.username:
            messagebox.showerror("Error", "Username cannot be empty!")
            self.root.destroy()
            return

        try:
            self.sock.connect((self.host, self.port))
            self.sock.sendall(self.username.encode("utf-8"))
        except Exception as e:
            messagebox.showerror("Connection Error", f"Could not connect to server:\n{e}")
            self.root.destroy()
            return

        # Start listening to server
        threading.Thread(target=self.receive_messages, daemon=True).start()

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        self.root.mainloop()

    def send_message(self, event=None):
        msg = self.entry.get().strip()
        if msg:
            try:
                self.sock.sendall(msg.encode("utf-8"))
                self.append_chat(f"You: {msg}")   # 👈 Show your own message instantly with timestamp
                self.entry.delete(0, tk.END)
            except:
                self.append_chat("⚠️ Failed to send message.")
                self.sock.close()

    def receive_messages(self):
        while True:
            try:
                msg = self.sock.recv(1024).decode("utf-8")
                if not msg:
                    break

                if msg.startswith("USERLIST:"):
                    users = msg.replace("USERLIST:", "").split(",")
                    self.update_user_list(users)
                elif msg.startswith("ERROR:"):
                    messagebox.showerror("Error", msg.replace("ERROR:", ""))
                    self.sock.close()
                    self.root.quit()
                    return
                else:
                    self.append_chat(msg)

            except ConnectionResetError:
                self.append_chat("⚠️ Disconnected from server.")
                break
            except OSError:
                break

    def append_chat(self, msg):
        timestamp = datetime.now().strftime("[%H:%M]")  # 👈 Format like [12:45]
        self.chat_area.config(state="normal")
        self.chat_area.insert(tk.END, f"{timestamp} {msg}\n")
        self.chat_area.config(state="disabled")
        self.chat_area.see(tk.END)

    def update_user_list(self, users):
        self.user_listbox.delete(0, tk.END)
        for user in users:
            if user.strip():
                self.user_listbox.insert(tk.END, user)

    def on_close(self):
        try:
            self.sock.close()
        except:
            pass
        self.root.destroy()


if __name__ == "__main__":
    ChatClient()
