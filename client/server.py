import socket
import threading

PORT = 5050 # SERVER = "192.168.31.127"
SERVER = socket.gethostbyname(socket.gethostname()) #gethostname - полуаем имя компьютера
# gethostbyname - получаем по имени IP локальные адреса
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    pass

def start():
    pass

print("[STARTING] server is starting...")