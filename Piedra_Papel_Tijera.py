#!/usr/bin/env python
# -*-coding:utf-8-*-


import time
from time import sleep
import random

sus = "-"*35
depo = ["piedra","papel", "tijera"]

while True:
    usuario = input("Que elijes ?, piedra, papel o tijera :")
    if usuario not in depo:
        print("No hagas Trampa !!")
        continue
    pc = random.choice(depo)
    sleep(0.5)
    print(("La computadora eligio {}.").format(pc))
    if(usuario == pc):
        print("\nEmapte.")
    elif(usuario == "piedra" and pc == "tijera" ):
        print("\nGanaste.")
    elif(usuario == "papel" and pc == "piedra"):
        print("\nGanaste")
    elif(usuario == "tijera"  and  pc == "papel"):
        print("\n Ganaste")
    else:
        print("Perdiste. {} gana {} \n". format(pc,usuario,))
    print(sus)
