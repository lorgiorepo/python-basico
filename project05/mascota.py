#!/usr/bin/python2.7
class mascota:
    numero_de_patas = 0
    color = "cafe"

    def dormir(self):
        print "zzz"

perro = mascota()
perro.numero_de_patas = 4
perro.color = "blanco"

print "EL perro tiene " + str(perro.numero_de_patas) + " patas y es de color "+ perro.color
perro.dormir()