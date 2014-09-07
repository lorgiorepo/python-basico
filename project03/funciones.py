#!/usr/bin/python2.7

#nuestros dos precios de articulos
articulo1 = 10 # articulo 1 posee un precio de 10
articulo2 = 15 # articulo 2 posee un precio de 15
articulo3 = 40 # articulo 3 posee un precio de 40
articulo4 = 50 # articulo 4 posee un precio de 50

def totalizarCompra(item1, item2):
    costoTotal = item1 + item2
    return costoTotal

total1 = totalizarCompra(articulo2, articulo3)
total2 = totalizarCompra(articulo1, articulo4)

print total1
print total2

