# Echo server program
import socket
import time
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




HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)

conn, addr = s.accept()
conn.sendall('Connected...')



enviar1 = Thread(target = enviar, args = (conn,))
enviar1.daemon = True
enviar1.start()
rebre1 = Thread(target = rebre, args= (conn,))
rebre1.start()



rebre1.join()
time.sleep(1)
print "Disconnected"

conn.close()
