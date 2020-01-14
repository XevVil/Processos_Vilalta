# Echo client program
import socket

HOST = 'localhost'    # The remote host
PORT = 50007              # The same port as used by the server
contingut = ''
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    contingut = raw_input()
    s.sendto(contingut,(HOST,PORT))
    if contingut == "bye":
        False

s.close()
