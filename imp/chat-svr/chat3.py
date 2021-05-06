import socket 

s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

ip = "192.168.43.198"
port = 3456

s.bind((ip, port))
s.listen()

c, addr = s.accept()

x = c.recv(1024)
print(x)

c.send(b"hi from server")

