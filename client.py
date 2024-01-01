import socket
import threading


class SharedCode:
    def __init__(self, host, port):
        self._lock = threading.Lock()
        self._data = None
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((host, int(port)))

    def get_data(self):
        with self._lock:
            return self._data

    def set_data(self, value):
        with self._lock:
            self._data = value

    def data_pull(self):

        try:
            # Receive data from the server
            print("grabbing")
            #recv limit is to allow large amounts of data
            data = self.client_socket.recv(500000).decode()
            self.set_data(data)
            print("Received:", data)

        except KeyboardInterrupt:
            # Close the client socket when Ctrl+C is pressed
            self.client_socket.close()
            print("Client disconnected.")
