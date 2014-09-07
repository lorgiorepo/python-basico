#!/usr/bin/python2.7
import MySQLdb
import sys, traceback
from datetime import date

# Establecemos la conexion con la base de datos
db = MySQLdb.connect(host='localhost', user='bcochile', passwd='bcochile', db='bancochile', port=3306)
print "Conexion realizada"

# Preparamos el cursos que nos va a ayudar a realizar las operaciones con la base de datos
cursor = db.cursor()

print "cursor iniciado"

sql = "SELECT * FROM usuarios"

try:
    cursor.execute(sql)
    resultados = cursor.fetchall()

    for registro in resultados:
        id = registro[0]
        usuario = registro[1]
        nombre = registro[3]
        apellido = registro[4]
        fechaAcceso = registro[5]
        estado = registro[6]
        print "id=%s, usuario=%s, nombre=%s, apellido=%s, fechaAcceso=%s, estado=%s" % (id, usuario, nombre, apellido, fechaAcceso, estado)
except:
    print "Error: No se pudo obtener la data"

cursor.close()
db.close()
