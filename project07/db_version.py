#!/usr/bin/python2.7

import MySQLdb

# Establecemos la conexion con la base de datos
db = MySQLdb.connect("localhost", "bcochile", "bcochile", "bancochile", 3306)

# Preparamos el cursos que nos va a ayudar a realizar las operaciones con la base de datos
cursor = db.cursor()

# Ejecutamos un query SQL usando el metodo execute() que nos proporciona el cursor
cursor.execute("SELECT VERSION()")

# Extraemos una sola fila usando el metodo fetchone()
data = cursor.fetchone()

print "Version Base de datos : %s " % data

# Nos desconectamos de la base de datos
db.close()
