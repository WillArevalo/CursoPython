import sqlite3

conexion = sqlite3.connect('usuarios_autoincremental.db')
cursor = conexion.cursor()

#cursor.execute('''
#	CREATE TABLE usuarios (
#		dni VARCHAR(9) PRIMARY KEY,
#		nombre VARCHAR(100),
#		edad INTEGER,
#		email VARCHAR(100)
#	)
#	''')

#usuarios = [
#	('11111111A','Hector',30,'mario@ejemplo.com'),
#	('11111112B','Will',23,'will@gmail.com'),
#	('11111113C','Fabian',19,'fabian@mail.com'),
#	('11111114D','Mario',34,'mario@pinchemail.com')
#]
#cursor.executemany('INSERT INTO usuarios VALUES(?,?,?,?)', usuarios)

#cursor.execute("INSERT INTO usuarios VALUES('11111116F','Fabian',19,'fabian@mail.com')")


#Campos autoincrementales
#cursor.execute('''
#	CREATE TABLE productos (
#		id INTEGER PRIMARY KEY AUTOINCREMENT,
#		nombre VARCHAR(100) NOT NULL,
#		marca VARCHAR(50) NOT NULL,
#		precio FLOAT NOT NULL

#	)
#	''')

#productos = [
#	('Teclado', 'Logitech', 12.50),
#	('Pantalla','LG',89.95)
#]

#cursor.executemany("INSERT INTO productos VALUES (null,?,?,?)", productos)
#cursor.execute("SELECT * FROM productos")
#productos = cursor.fetchall()
#for producto in productos:
#	print(producto)

cursor.execute('''
	CREATE TABLE usuarios (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		dni VARCHAR(9) UNIQUE,
		nombre VARCHAR(100),
		edad INTEGER,
		email VARCHAR(100)
	)
	''')

usuarios = [
	('11111111A','Hector',30,'mario@ejemplo.com'),
	('11111112B','Will',23,'will@gmail.com'),
	('11111113C','Fabian',19,'fabian@mail.com'),
	('11111114D','Mario',34,'mario@pinchemail.com')
]
cursor.executemany('INSERT INTO usuarios VALUES(null,?,?,?,?)', usuarios)


conexion.commit()
conexion.close()