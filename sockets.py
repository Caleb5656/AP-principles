import socket

# AF_INET is ipv4; SOCK_STREAM is TCP, SOCK_DGRAM is udp
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# allow socket to be reused
tcp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
host = socket.gethostname()  # get local device ip
port = 9999


def do_server():
    tcp.bind((host, port))
    tcp.listen(5)  # listen to 5 connections
    print("listening....")
    while True:
        csocket, addr = tcp.accept()
        print(f"client connected: {addr}")
        message = "thanks for connecting".encode('ascii')
        csocket.send(message)
        csocket.close()


def do_client():
    tcp.connect((host, port))
    msg = tcp.recv(1024)  # recieve up to 1024 bytes
    tcp.close()
    print(f"Received server message: {msg.decode('ascii')}")

choice = input("Are you client or server: ")
if choice in "client":
    do_client()
else:
    do_server()