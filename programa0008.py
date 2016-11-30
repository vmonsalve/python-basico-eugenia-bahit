# -*- coding: utf-8 -*-

import random

total_compra = random.randint(0, 500)

importe_a_pagar = total_compra

if total_compra > 100:
    tasa_descuento = 10
    importe_descuento = total_compra * tasa_descuento / 100
    importe_a_pagar = total_compra - importe_descuento

print total_compra
print importe_a_pagar