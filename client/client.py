import socket

HEADER = 64 # 64 tells msg that is going to come next Header = 64 symbols
PORT = 5050 # SERVER = "192.168.31.127" на этом порте сервер будет слушать входящие сообщения
SERVER = socket.gethostbyname(socket.gethostname()) #gethostname - полуаем имя компьютера

ADDR = (SERVER, PORT) # tuple
FORMAT = 'UTF-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)