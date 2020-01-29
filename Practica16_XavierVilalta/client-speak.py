# Echo client program
import socket
from threading import Thread

def rebre(s):
    while True:
        data = s.recv(1024)
        print ">>"+data
        if data.lower() == "bye":
            s.sendall(data)
            break

def enviar(conn):
    while True:
        data = raw_input("Envia un missatge: ")
        conn.sendall(data)
        if data.lower() == "bye":
            break



HOST = 'localhost'    # The remote host
PORT = 50007          # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))
s.sendall("Sending...")


enviar1 = Thread(target = enviar, args= (s,))
enviar1.daemon = True
enviar1.start()
rebre1 = Thread(target = rebre, args =(s,))
rebre1.start()

rebre1.join()
print "Disconnected"

s.close()
