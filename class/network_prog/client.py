import socket


def client_program():
    host = "10.100.100.105"
    port = 1234

    s = socket.socket()
    s.connect((host, port))

    message = input(" -> ")

    while message.lower().strip() != 'bye':
        s.send(message.encode())
        data = s.recv(1024).decode()

        print('Received from server: ' + data)

        message = input(" -> ")

    s.close()


if __name__ == '__main__':
    client_program()

