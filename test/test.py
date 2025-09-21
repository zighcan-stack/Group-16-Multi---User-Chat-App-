import pytest
import socket
import threading
import time

from server.server import ChatServer
from client.helpers import format_timestamp


class TestChatServer:
    """Test cases for ChatServer functionality"""

    def setup_method(self):
        """Start the server in a background thread before each test"""
        self.server = ChatServer(host="127.0.0.1", port=12346)
        self.thread = threading.Thread(target=self.server.start, daemon=True)
        self.thread.start()
        time.sleep(0.2)  # Give server time to start

    def teardown_method(self):
        """Close the server socket after each test"""
        try:
            self.server.server_socket.close()
        except:
            pass

    def test_server_socket_setup(self):
        """Server should bind and listen on correct host/port"""
        assert self.server.host == "127.0.0.1"
        assert self.server.port == 12346
        assert isinstance(self.server.server_socket, socket.socket)

    def test_server_accepts_client_connection(self):
        """Server should accept incoming connections"""
        client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_sock.connect(("127.0.0.1", 12346))
        client_sock.sendall(b"tester1")
        time.sleep(0.2)
        assert "tester1" in self.server.clients.values()
        client_sock.close()


class TestChatHelpers:
    """Test cases for helper functions"""

    def test_format_timestamp_returns_valid_string(self):
        """Ensure timestamp is correctly formatted"""
        ts = format_timestamp()
        assert ts.startswith("[") and ts.endswith("]")
        assert len(ts) == 7  # Format: [HH:MM]


class TestClientServerInteraction:
    """Integration tests for client-server communication"""

    def setup_method(self):
        """Start fresh server for integration tests"""
        self.server = ChatServer(host="127.0.0.1", port=12347)
        self.thread = threading.Thread(target=self.server.start, daemon=True)
        self.thread.start()
        time.sleep(0.2)

    def teardown_method(self):
        """Shutdown server socket"""
        try:
            self.server.server_socket.close()
        except:
            pass

    def test_message_broadcast_between_clients(self):
        """Messages from one client should be received by another"""
        # Connect two clients
        client1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client1.connect(("127.0.0.1", 12347))
        client1.sendall(b"user1")

        client2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client2.connect(("127.0.0.1", 12347))
        client2.sendall(b"user2")

        time.sleep(0.2)

        # Send message from client1
        msg = "Hello from user1"
        client1.sendall(msg.encode("utf-8"))

        # Receive on client2
        data = client2.recv(1024).decode("utf-8")
        assert "user1" in data
        assert "Hello from user1" in data

        client1.close()
        client2.close()


"""
======================================================================================
Pytest Sample Report (from previous run)

Test Session:
  Date/Time   : 2025-09-18T19:43:38+01:00
  Host        : isah-HP-EliteBook-820-G1
  Framework   : pytest
  Total Time  : 0.029s

Executed Tests:
  tests.test_client::test_client_socket_creation      PASSED   [0.001s]
  tests.test_client::test_client_connection_failure   PASSED   [0.001s]
  tests.test_server::test_server_socket_setup         PASSED   [0.001s]
  tests.test_server::test_server_host_and_port        PASSED   [0.001s]

Summary:
  Total tests : 4
  Passed      : 4
  Failed      : 0
  Errors      : 0
  Skipped     : 0
  Duration    : 0.029s

All tests passed successfully ✅
======================================================================================
"""
