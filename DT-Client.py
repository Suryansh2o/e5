import socket
import time

def client_program():
host = socket.gethostname()
port = 6123

client_socket = socket.socket()
client_socket.connect((host, port))

while (True) :
# client_socket.send(message.encode())
data = client_socket.recv(1024).decode()

print('Received from server: ' + data)
# message = input (" -> ")
break

client_socket.close()

if __name__ == '__main__':
client_program()
