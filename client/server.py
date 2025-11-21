import socket
import threading

PORT = 5050 # SERVER = "192.168.31.127" на этом порте сервер будет слушать входящие сообщения
SERVER = socket.gethostbyname(socket.gethostname()) #gethostname - полуаем имя компьютера
# gethostbyname - получаем по имени IP локальные адреса
ADDR = (SERVER, PORT) # tuple
FORMAT = 'UTF-8'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    # handle communication between client and server
    print(f"[NEW CONNECTION] {addr} connected.")

def start():
    pass

print("[STARTING] server is starting...")