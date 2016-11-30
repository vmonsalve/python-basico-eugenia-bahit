# -*- coding: utf-8 -*-

#Tupla
def calcular(importe, descuento):
    return importe - (importe * descuento / 100)

datos = [1500, 10]
print "Tupla"
print calcular(*datos)

#Diccionario
datos = {"descuento": 10, "importe": 1500}
print "Diccionario"
print calcular(**datos)