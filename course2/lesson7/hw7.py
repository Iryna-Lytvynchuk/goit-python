import socket
from time import sleep
import threading


def echo_server(host, port):
    with socket.socket() as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, port))
        s.listen(1)
        conn, addr = s.accept()
        print(f"Connected by {addr}")
        with conn:
            while True:
                data = conn.recv(1024)
                print(f'From client: {data}')
                if not data:
                    break
                if data == b"Hello":
                    conn.send(b"True")
                else:
                    conn.send(b"False")

def simple_client(host, port, message):
    with socket.socket() as s:
        while True:
            try:
                s.connect((host, port))
                s.sendall(bytes(message, 'utf-8'))
                data = s.recv(1024)
                if data == b"True":
                    print(f'From server: {host} on {port}')
                    break
                else:
                    print(f'good by')
                    break
            except ConnectionRefusedError:
                sleep(0.5)

if __name__ == "__main__":

    HOST = '127.0.0.1'
    PORT = 55555

    while True:
        MESSAGE = input("Some message: ")
        
        if MESSAGE == "Stop":
            print("Finish")
            break

        server = threading.Thread(target=echo_server, args=(HOST, PORT))
        client = threading.Thread(target=simple_client, args=(HOST, PORT, MESSAGE))

        server.start()
        client.start()
        server.join()
        client.join()
        print('Done!')
