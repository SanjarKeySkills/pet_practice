import socket
import threading

HEADER = 64 # 64 tells msg that is going to come next Header = 64 symbols
PORT = 5050 # SERVER = "192.168.31.127" на этом порте сервер будет слушать входящие сообщения
SERVER = socket.gethostbyname(socket.gethostname()) #gethostname - полуаем имя компьютера
# gethostbyname - получаем по имени IP локальные адреса
ADDR = (SERVER, PORT) # tuple
FORMAT = 'UTF-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

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
  
def start():
    pass

print("[STARTING] server is starting...")