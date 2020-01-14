# Echo server program
import socket
import time

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST,PORT))
while True:
    contingut = s.recv(1024)
    print contingut
    if contingut == "bye":
        time.sleep(1)
        break

s.close()
