# -*- coding: utf-8 -*-

from GeneraKey import *

#---------------------1-------------------


clau = GeneraClau()
print(clau.exportKey())

#---------------------2-------------------


#cLAU privada
ExportaClau("Clau Privada", clau)

#Key publica
ExportaClau("Clau Publica", clau.publickey())

#---------------------3-------------------

#importa la clau privada
clauPrivada = ImportaClau("clauPrivada.pem")
#muestra la key privada
print("CLau Privada ->>" + str(clauPrivada))

#importa la clau publica
clauPublica = ImportaClau("clauPublica.pem")
#muestra la clau publica
print("Clau Publica ->>" + str(clauPublica))

#---------------------4-------------------

#Encripta
msgEncriptat = EncriptaClauRSA('Bon dia, que tal', clauPublica)
#Muestra l'encriptació
print("missatge encriptat ->> " +str(msgEncriptat))

#---------------------5-------------------

#Desencripta
msgDesencriptat = DesencriptaClauRSA(msgEncriptat,clauPrivada)
#Muestra la desencriptacion
print("missatge desencriptat ->> " + str(msgDesencriptat))

#---------------------6-------------------

#Genera clau

ClauSHA = GeneraClauSHA256()
#Muestar KeySHA
print("password encriptada: ", ClauSHA)

#---------------------7-------------------
#Encripta data AES
DataEncriptadaAES = EncriptaMsgAES("Provant si funciona", ClauSHA)
#Mostra l'encriptació AES
print("Data Encriptada AES ->>" + str(DataEncriptadaAES))

#---------------------8-------------------
#Desencripta la data AES
msgDesencriptat = DesencriptaMsgAES(DataEncriptadaAES , ClauSHA)
#Mostra la desencriptació AES
print("El missatge desencriptat ->> " + msgDesencriptat)
