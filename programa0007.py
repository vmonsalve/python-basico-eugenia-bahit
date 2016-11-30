#-*- coding: utf-8 -*-
import random

compra = random.randint(0, 500)

if compra <= 100:
    print compra
    print "Pago en efectivo"
elif compra > 100 and compra < 300:
    print compra
    print "Pago con tarjeta de débito"
else:
    print compra
    print "Pago con tarjeta de crédito"