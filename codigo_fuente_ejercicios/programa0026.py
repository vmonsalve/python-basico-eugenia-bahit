#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 00:00:35 2018

@author: vmonsalve
"""
# Clases.

class Antena:
    color    = ""
    longitud = ""

class Pelo:
    color   = ""
    textura = ""

class Ojo:
    forma   = ""
    color   = ""
    tamanio = ""

class Objeto:
    color   = "Verde"
    tamanio = "Grande"
    aspecto = "Feo"
    antenas = Antena()
    ojos    = Ojo()
    pelos   = Pelo()
    
    def flotar(self):
        print(12)

et = Objeto()
print(et.color)
print(et.tamanio)
print(et.aspecto)
et.color = "Rosa"
print(et.color)
print(et.flotar())
    