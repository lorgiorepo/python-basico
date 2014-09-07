#!/usr/bin/python2.7
import datetime
from datetime import date
import time

#Retorna el numero de segundos desde el 1 de enero de 1970 (UNix Epoch)
print time.time()

#Convierte numero de segundos en un objeto tipo date
print date.fromtimestamp(123456789)
#Podemos combinar las funciones time y fromtimestamp para representar el tiempo
print date.fromtimestamp(time.time())

currentDate = date.fromtimestamp(time.time())
currentDate.strftime("%d%m%y")
print currentDate

#Fecha en formato ISO
print currentDate.isoformat()
