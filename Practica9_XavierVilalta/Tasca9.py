#-*- coding: utf8 -*-
#4523

# 40 / 2 = 20
# 40 / 4 = 10
from multiprocessing import Pool
from datetime import datetime

def primers(num):
    for i in range(2, num/2):
        if num % i == 0:
            return False
        else:
            pass
    return True

if __name__ == '__main__':

    pool = Pool(processes = 2)
    l = range(4000000, 4000010)#[45445535, 56534563, 43566487, 43635453, 52346557, 53454433, 43546453, 26847357, 54577647]
    start = datetime.now()
    for i in pool.map(primers,l):
        s = primers(i)
        print i, l
    print datetime.now() - start


  #0:00:00.344863
  #0:00:00.344863
  #0:00:00.340357
  #0:00:00.349121
  #0:00:00.342021

  # A mesura que anem inicialitzant el programa el que fa
  # es que el temps d'execució serà menor.
