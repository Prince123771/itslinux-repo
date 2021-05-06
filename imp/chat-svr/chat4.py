import socket
import threading 
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


port = 2222
ip = ""

s.bind(( ip , port ))
s.listen()


def chat(csessiona , addr):
   print(addr)
   csessiona.send(b"i am sneh")
   data = csessiona.recv(1000)
   print(data)

while True:
    csessiona , addr = s.accept()
    t1 = threading.Thread(target = chat, args=(csessiona , addr))
    t1.start()
