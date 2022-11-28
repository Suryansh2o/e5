import socket
import time

def server_program():
host = socket.gethostname()
port = 6123

server_socket = socket.socket()
server_socket.bind((host, port))

server_socket.listen(5)
conn, address = server_socket.accept()
print ( "Connection from: " + str (address))

while True:

ti = time.gmtime()
data = (time.asctime(ti))
conn.send(data.encode())
print('Received from server: ' + data)
break

conn.close()

if __name__ == '__main__':
server_program()
