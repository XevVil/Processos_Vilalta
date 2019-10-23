#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

class llista_primers:
    """
    El programa el que fa es crear una llista de numeros començant per el 2
    la llargada d'aquesta sera determinada per el numero introduit per l'usuari.

    >>> llista_primers(5).llista
    [2, 3, 5, 7, 11]

    >>> llista_primers(6).llista
    [2, 3, 5, 7, 11, 13]
    """
    def __init__(self, n):
        """
         En aquest apartat inicialitzem les variables del programa
        """
        self.n = n
        self.llista = []
        self.busca()

    def busca(self):
        """
        En el primer if el programa s'inicia amb la llista buida (0)
        de ser aixi comença per el numero 2 .
        En cas d'estar ja iniciada pasarem al elif el qual comprova que la llista
        sigui la llargada indicada per l'usuari.

        Mentres sigui mes petita el programa buscara numeros per aquesta si el residu del
        numero es igual a 0 es sumara 1 i pasara al seguent, en cas de ser diferent a
        0 es guardara el numero i es mostra en la llista.
        """
        if (len(self.llista) == 0): # Si la llista te una llargada de 0 començara amb el numero dos i buscara altres numeros
            self.llista.append(2)
            self.busca()
        elif (len(self.llista) < self.n):# Si la llista està iniciada comprova la llargada si es mes petita que el numero del usuari seguira buscant
            trobat = False
            seguent = self.llista[-1]+1    
            while not trobat:
                for i in self.llista: #si el residu del numero es 0 suma 1 al numero i continua buscant
                    if seguent%i == 0:
                        seguent += 1
                        trobat = False
                        break
                    else: # si el numero te un residu diferent a 0 es guarda i es mostrara a la llista
                        trobat = True
            self.llista.append(seguent)
            self.busca()


if __name__ == '__main__':
    """
    Aqui el programa demana un numero a l'usuari que aquest serà la llargada de la llista
    """
    import doctest
    doctest.testmod()
    #l = llista_primers(int(sys.argv[1])) #l'usuari entra el numero
    #print l.llista
