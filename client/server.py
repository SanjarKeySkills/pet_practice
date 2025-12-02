import socket
import threading
from datetime import datetime
import json
import urllib.parse

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
server.bind(ADDR)

users_db = [
	{"id": 1, "name": "John Doe", "email": "john@example.com", "active": True},
	{"id": 2, "name": "Jane Smith", "email": "jane@example.com", "active": True},
]
next_user_id = 3

class HTTPRequest:
    
    def _init_(self, raw_request):
        self.method = ""
        self.path = ""
        self.version = ""
        self.headers = {}
        self.body = ""
        self.query_params = {}
        self.parse_request(raw_request)

	def parse_request(self, raw_request):
		try:
			lines = raw_request.split('\r\n')
			if not lines:
				return
			request_line = lines[0]
			parts = request_line.split(' ')
			if len(path_parts) > 1
 
def handle_client(conn, addr):
    # handle communication between client and server
    print(f"[NEW CONNECTION] {addr} connected.")
    
    while True:
        connected = True
        while connected:
            #decode this function from its bite format to str using utf-8 format
			msg_length = conn.recv(HEADER).decode(FORMAT)
			#how many bites we are going to receive
			if msg_length:
				msg_length = int(msg_length)
				msg_length = conn.recv(msg_length).decode(FORMAT)
				if msg == DISCONNECT_MESSAGE:
				connected = False
				print(f"[{addr}] {msg}") # handling the disconnection clearly
			conn.close() #closed disconnection

def start():
    pass

print("[STARTING] server is starting...")