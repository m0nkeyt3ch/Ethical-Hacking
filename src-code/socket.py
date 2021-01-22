import socket

serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostbyname()
port = 444

serversock.bind((host, port))

serversock.listen(3)

while True:
    clientsock, address = serversock.accept()
    print("Received connection from " % str(address))
    message = 'Hello' + "\r\n"

    clientsock.close()