# Echo server program
import socket
from threading import Thread
import time

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)
global nomusuaris
nomusuaris = []
global conexio
conexio = []

def add_Con():

    while True:
        user = ""
        conexio.append(s.accept())
        if len(nomusuaris) == 0:
            conexio[-1][0].sendto("Server : Introdueix el nom d'usuari: \n", conexio[-1][1])
            user = conexio[-1][0].recv(1024)
            nomusuaris.append((user, conexio[-1][1][1]))
        else:
            for client in conexio:
                for uname in nomusuaris:
                    if client[1][1] != uname[1]:
                        client[0].sendto("Server : Introdueix el nom d'usuari: \n", client[1])
                        user = client[0].recv(1024)
                        nomusuaris.append((user,  client[1][1]))

        Thread(target = send_to, args = (conexio[-1][0], conexio[-1][1], user)).start()


def send_to(conn, addr, uname):
    while True:
        message = conn.recv(1024)
        print(message)
        for client in conexio:
            if addr[1] != client[1][1]:
                for username in nomusuaris:
                    if addr[1] == username[1]:
                        client[0].sendto(str(username[0]+":"+message), addr)
                        print(message + "    " + str(client[1]))
            else:
                print (str(client[1][1]) + "\n" + str(addr[1]))
        if message[:-1].lower() == "bye":
            for i in range(len(conexio)):
                if addr[1] == conexio[i][1][1]:
                    conexio.pop(i)
                    break
            for i in range(len(nomusuaris)):
                if addr[1] == username[i][1]:
                    nomusuaris.pop(i)
                    break
            break

thread = Thread(target = add_Con, args = ( ))

thread.start()
time.sleep(1)
thread.join()
s.close()
