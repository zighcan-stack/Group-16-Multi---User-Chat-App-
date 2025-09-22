# 💬 Multi-User Chat App

## 📖 Project Summary

Python Multi-User Chat App is a real-time chatroom built with Python 3.10+ that allows users on the same local network to connect, choose usernames, and exchange messages instantly.  

The system is structured with separate classes for the server and clients, includes custom exceptions for network errors, and provides a simple Tkinter GUI for flexibility.  
This implementation showcases professional practices including modular design, clean architecture, and automated testing with pytest.



## ✨ Features

- 👥 **Multi-User Chatroom**: Many clients can connect simultaneously  
- 🖥️ **GUI Client**: Tkinter-based chat interface with user list  
- 💻 **Console Client**: Lightweight terminal version for quick use  
- 🕒 **Timestamps**: Every message is time-stamped for clarity  
- 🗒️ **User List Sync**: Real-time updates of connected users  
- 🚫 **Duplicate Username Protection**: Prevents collisions  
- ⚡ **Threaded Server**: Handles multiple clients concurrently  
- 🛠️ **Cross-Platform**: Works on Windows, macOS, Linux  



## 👥 Team Collaboration

Development is organized through GitHub with clear role assignments:

- **Networking Team** → Implement the socket-based server and client communication  
- **GUI Team** → Design and polish the Tkinter-based interface  
- **Testing Team** → Write unit tests and document network procedures  
- **Docs/Media Team** → Prepare README files, reports, and demo videos  
- **Coordinator** → Oversee integration, consistency, and submission  



## 🎯 Minimum Viable Product (MVP)

To achieve the MVP, we deliver:

- A functioning server that accepts multiple clients, broadcasts messages, and handles disconnects gracefully.  
- A basic Tkinter client GUI supporting usernames, real-time chat, user lists, and timestamps.  
- A test suite verifying network stability and error handling, ensuring a reliable, minimal chatroom experience.  



## 🛠️ Installation & Setup

### 📌 Prerequisites
- Python 3.10+  
- `pipenv` (recommended) or `pip`  

### 🚀 Quick Start

**Clone the repository:**
```bash
git clone https://github.com/yourname/multi-chat-app.git
cd multi-chat-app
````

**Install pipenv (if not installed):**

```bash
pip install pipenv
```

**Install dependencies:**

```bash
pipenv install --dev
```

**Activate the virtual environment:**

```bash
pipenv shell
```

**Run the server:**

```bash
python server/server.py
```

**Run a client (GUI client):**

```bash
python client/client_gui.py
```

Enter username when prompted.

* Type messages in the input box, press Enter to send
* Messages appear in the chat log with timestamps
* The right panel shows online users

**Run a Console client:**

```bash
python client/client_console.py
```

* Enter username on startup
* Type messages and press Enter to send
* Type `/quit` or `/exit` to disconnect

---

## 🧩 Module Documentation

### 🔹 `server.py` – Chat Server

**Role:** Accepts client connections, manages message broadcasting, and updates user lists.
**Responsibilities:**

* Handle multiple clients with threads
* Broadcast messages to all except sender
* Prevent duplicate usernames
* Send real-time user list updates

### 🔹 `client_gui.py` – GUI Client

**Role:** Tkinter chat interface with online user panel.
**Features:**

* Chat log with timestamps
* User list sidebar
* Local echo for sent messages
* Smooth scrolling

### 🔹 `client_console.py` – Console Client

**Role:** Minimal terminal client.
**Features:**

* Quick testing without GUI
* Local echo of sent messages
* `/quit` command to exit

### 🔹 `utils.py` & `helpers.py`

**Role:** Shared utilities (timestamp formatting, sanitization).

---

## 🧪 Testing

**Run Tests:**

```bash
pipenv run pytest tests/ -v
```

**With Coverage:**

```bash
pipenv run pytest tests/ -v --cov=server --cov=client --cov-report=html
```

Open `htmlcov/index.html` in a browser to view coverage.

---

## 📺 Demo (Optional)

* **Screenshots:**
  https://github.com/user-attachments/assets/a37a9024-0294-4549-a2ba-cbcfc7cb4442

* **Video Demo:** *(Add link if hosted)*

---

## 🚀 Performance & Specs

* **Concurrent Clients:** Handles 50+ connections on a modern laptop
* **Message Latency:** < 100ms on local network
* **Memory Usage:** < 50MB per client
* **Cross-Platform:** Tested on Windows 10, Ubuntu 22.04, macOS Ventura

---

## 🔧 Development & Contribution

**Setup:**

```bash
git clone https://github.com/yourname/multi-chat-app.git
cd multi-chat-app
pipenv install --dev
pipenv shell
```

### 🌟 Future Enhancements

* 🔒 Add authentication (username/password)
* 📜 Save chat history to file/database
* 💬 Private messages (`/w user message`)
* 🌐 Encrypted communication (TLS)
* 📱 Mobile client

---

## 📄 License

This project is licensed under the **MIT License**.

```


