# -*- coding: utf-8 -*-

def funcion(nombre):
    return "Hola "+nombre

def llamada_de_retorno(func=""):
    if func in globals():
        if callable(globals()[func]):
            return globals()[func]("Vicente")
    else:
        return "Funcion no encontrada"

print llamada_de_retorno("funcion")

nombre_de_la_funcion = "funcion"
if nombre_de_la_funcion in locals():
    if callable(locals()[nombre_de_la_funcion]):
        print locals()[nombre_de_la_funcion]("Vicente 2")
else:
    print "Funcion no encontrada"
