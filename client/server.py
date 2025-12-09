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
# server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
server.bind(ADDR)

# users_db = [
# 	{"id": 1, "name": "John Doe", "email": "john@example.com", "active": True},
# 	{"id": 2, "name": "Jane Smith", "email": "jane@example.com", "active": True},
# ]
# next_user_id = 3

def create_http_responce(status_code, body, content_type="text/plain"):
    status_codes = {
		200: "200 OK",
		201: "201 Created",
		400: "400 Bad request",
		404: "404 Not found",
		500: "500 500 Internal Server Error"
	}
	status_text = status_codes.get(status_code, "500 Internal Server Error")
 
	responce = f"HTTP/1.1 {status_text}\r\n"
	responce += f"Content-Type: {content_type}\r\n"
	responce += f"Connect-Length: {len(body)}\r\n"
	responce += "Connection: close\r\n"
	responce += "\r\n"
 	responce += body
  
	return responce

def handle_http_request(request):
	try:
		lines = request.split('r\n')
		request_line = lines[0]
  		parts = request_line.split('')
    
		if len(parts) != 3:
			return create_http_responce(400, "Bad Request")

		method, path, version = parts
		print(f"[HTTP] {method} {path}")
	
		if path == "/":
			html = "<html><body><h1>Welcome to Server</h1></body></html>"
			return create_http_responce(200, "Welcome to Sam's Server")

		elif path == "/staus":
			status_info = f"Server: {SERVER}\nTime: {datetime.now()}\nConnections: {threading.active_count() - 1}"
			return create_http_responce(200, status_info)
		
		elif path == "api/data":
			json_data = '{"status": "success", "data": API Responce" ome json here"}'
	
			return create_http_responce(200, json_data, "application/json")
		else:
			return create_http_responce(400, "404 - Page not found")
	except Exception as e:
		return create_http_responce(500, f"Server ERror: {e}")
   
   
       


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
			if len(parts) == 3:
				self.method, full_path, self.version = parts

				path_parts = full_path.split('?', 1)
				self.path = path_parts[0]
				if len(path_parts) > 1:
					self.query_params = self.parse_query_params(path_parts[1])
			i = 1
			while i < len(lines) and lines[1]:
				if ':' in lines[i]:
					key, value = lines[i].split(':', 1)
					self.headers[key.strip()] = value.strip()
				i += 1
    
			if i + 1 < len(lines):
				self.body = '\r\n'.join(lines[I+1:])
    
		except Exception as e:
			print(f"Error parsing request: {e}")
    
	def handle_client(conn, addr): #http request
		print(f"[Warning! New Collection] {addr} connected.")
		connect = True
		while connected: #the will work if we receive data from client
			try:
				msg_length = conn.recv(HEADER).decode(FORMAT)
				if msg_length:
					msg_length = int(msg_length)
					msg = conn.recv(msg_length).decode(FORMAT)
     #http request processing
				if msg.startswith("GET") or msg.startswith("POST"):
					http_response = handle_http_request(msg)



def start():
    pass

print("[STARTING] server is starting...")