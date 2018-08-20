# -*- coding: utf-8 -*-

def recorrer_parametros_arbritriarios(parametro_fijo, *arbitrarios):
    print parametro_fijo
    for argumento in arbitrarios:
        print argumento

recorrer_parametros_arbritriarios('fijo', 'arbitrario_uno', 'arbitrario_dos', 'arbitrario_tres')