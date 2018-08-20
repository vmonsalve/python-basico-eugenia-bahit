# -*- coding: utf-8 -*-
import random

semaforo = ['verde', 'amarillo', 'rojo']
color = random.choice(semaforo)

if color == "verde":
    print color
    print "Cruzar la calle"
else:
    print color
    print "Esperar"