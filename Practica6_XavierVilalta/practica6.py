import datetime
import time

from multiprocessing import Process, Queue

def t(s):
    while True:
        time.sleep(1.1)
        print(datetime.datetime.now().time())


def main():
    i = 0
    p = Process(target=t, args=(1,))
    p.start()

    while i <= 10:
        pass
        time.sleep(0.5)
        print(p.pid)
        i=i+1

    p.terminate()
    print("fi")

if __name__ == '__main__':
    main()
