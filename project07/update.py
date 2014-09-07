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

sql = "UPDATE usuarios set ULTIMO_ACCESO = "+str(date(2014, 9, 6))+" WHERE id = 3"

try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

cursor.close()
db.close()