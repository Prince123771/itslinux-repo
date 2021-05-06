import socket 

# udp protocol
myp = socket.SOCK_DGRAM
# net address family : ipv4
afn = socket.AF_INET


s = socket.socket(afn, myp)
ip = "192.168.43.198"
port = 4040
s.bind((ip, port))

x = s.recvfrom(1024)
print(x)

