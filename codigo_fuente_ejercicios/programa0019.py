# -*- coding: utf-8 -*-

def recorrer_parametros_arbitrarios(parametro_fijo, *arbitrarios, **kwords):
    print parametro_fijo
    for argumento in arbitrarios:
        print argumento

    for clave in kwords:
        print "El valor de ",clave,"es",kwords[clave]


recorrer_parametros_arbitrarios('Fijo', "arbitrario uno", "arbitrario dos", "arbitrario tres", clave1="valor uno", clave2="valor dos")