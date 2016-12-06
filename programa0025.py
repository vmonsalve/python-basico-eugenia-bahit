# -*- coding: utf-8 -*-

def jugar(intento = 1):
    respuesta = raw_input("¿De qué color es una naranja?")
    if respuesta != "naranja":
        if intento < 3:
            print "\n Fallaste intentalo de nuevo"
            intento += 1
            jugar(intento)
        else:
            print "\n Perdiste"
    else:
         print "\n Ganaste"

jugar()