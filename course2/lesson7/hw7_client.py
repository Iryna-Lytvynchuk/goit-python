import socket

message = input("Some message: ")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 8888))
s.send(bytes(message, 'utf-8'))
data = s.recv(1024)

if data == b"True":
    print(f'From server: Yes')
else:
    print(f'Good by')

s.close()
