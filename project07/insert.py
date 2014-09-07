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

# Preparamos el query SQL Para insertar un registro en la BD
##sql = "INSERT INTO USUARIOS (ID, USUARIO, CLAVE, NOMBRE, APELLIDO, ULTIMO_ACCESO, ESTADO) VALUES(2, 'ltrinidad', '123456', 'Lorgio', 'Trinidad', NOW(), 1)"
add_usuario = ("INSERT INTO usuarios (ID, USUARIO, CLAVE, NOMBRE, APELLIDO, ULTIMO_ACCESO, ESTADO) VALUES (%s, %s, %s, %s, %s, %s, %s)")

data_usuario = (4, 'etrinidad', '123456', 'Emanuel', 'Trinidad', date(2014, 9, 6), 1)



try:
    print "try iniciado"
    cursor.execute(add_usuario, data_usuario)
    print "cursor ejecutado"
    db.commit()
    print "commit hecho"
except:
    traceback.print_exc(file=sys.stdout)
    print "rollback"
    db.rollback()

cursor.close()
db.close()
