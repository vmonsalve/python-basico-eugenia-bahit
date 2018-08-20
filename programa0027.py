#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 00:21:06 2018

@author: vmonsalve
"""

class Antena(object):
    color    = ""
    longitud = ""

class Pelo(object):
    color   = ""
    textura = ""

class Ojo(object):
    forma   = ""
    color   = ""
    tamanio = ""

class Objeto(object):
    color   = ""
    tamanio = ""
    aspecto = ""
    antenas = Antena()
    ojos    = Ojo()
    pelo    = Pelo()
    
    def flotar(self):
        print("Flotó 2 metros")
        pass
    
class Dedo(object):
    longitud = ""
    forma    = ""
    color    = ""
    
class Pie(object):
    forma = ""
    color = ""
    dedos = Dedo()

# NuevoObjeto si hereda de otra clase: Objeto.
class NuevoObjeto(Objeto):
    pie = Pie()
    
    def saltar(self):
        print("saltó 12 metros")
        pass


digimon = NuevoObjeto()

digimon.color = "Gris"

print(digimon.saltar())
print(digimon.flotar())
print(digimon.color)    