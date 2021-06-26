import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 8888))
s.listen(2)

while True:
    try:
        conn, addr = s.accept()
        print(f"Connected by {addr}")
    except KeyboardInterrupt:
        s.close()
        break
    else:               
        data = conn.recv(1024)
                
        if not data:
            break

        if data == b"Hello":
            conn.send(b"True")
            conn.close()
            print('Message: ', data.decode('utf-8'))
            break
        else:
            conn.send(b"False")
            conn.close()
            print(f'I wont message: Hello, not: {data} ')
            break
        
        
 