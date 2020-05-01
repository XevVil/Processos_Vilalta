# -*- coding: utf-8 -*-
import hashlib
import json
import base64

from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
from base64 import b64decode, b64encode
from Crypto.Util.Padding import unpad
from Crypto.Random import random
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto import Random

#---------------------1-------------------

def GeneraClau():


    clau = RSA.generate(2048)
    return clau

#---------------------2-------------------

def ExportaClau(path, clau):

    exporta = clau.exportKey('PEM')
    exportaFitxer = open(path+ ".pem", "wb")
    exportaFitxer.write(exporta)
    exportaFitxer.close()

#---------------------3-------------------

def ImportaClau(path):

#Importa la clau
    return RSA.import_key(open(path).read())

#---------------------4-------------------

def EncriptaClauRSA(data,key):

# Encripta la clau RSA
    cipher = PKCS1_OAEP.new(key)
#Retorna el missatge encriptat
    return cipher.encrypt(data.encode())

#---------------------5-------------------

def DesencriptaClauRSA(msgEncriptado, key):


    cipher = PKCS1_OAEP.new(key)
#Retorna el missatge desencriptat
    return cipher.decrypt(msgEncriptado).decode('utf-8')

#---------------------6-------------------

def GeneraClauSHA256():

#Demana la contrasenya
    password = raw_input("Introdueix la contrasenya: ")
#Crea la clau  SHA256 a partir de la contrasenya
    clau = hashlib.sha256(password.encode("utf-8")).digest()
#Retorba la clau
    return clau

#---------------------7-------------------

def EncriptaMsgAES(data, key):

    length = 16
    data = data + (length - len(data) % length) * chr(length - len(data) % length)

    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv = iv)
    msgEncriptat = cipher.encrypt(data.encode())
    return base64.b64encode(iv + msgEncriptat)

#---------------------8-------------------

def DesencriptaMsgAES(msgEncriptat,clau):

    msgEncriptat = base64.b64decode(msgEncriptat)
    iv = msgEncriptat[:AES.block_size]
    msgExtret = msgEncriptat[AES.block_size:]
    cipher = AES.new(clau, AES.MODE_CBC, iv)
    return cipher.decrypt(msgExtret).decode('utf-8')
