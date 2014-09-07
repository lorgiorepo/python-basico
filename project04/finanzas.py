#!/usr/bin/python2.7
def calcularImpuesto(precio, impuesto):
    precioNuevo = precio / 100 * (100 + impuesto)
    return precioNuevo
