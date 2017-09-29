import sqlite3

#conexcion con la base de datos, si no existe se crea
conexion = sqlite3.connect("ejemplo.db")

#Se utiliza para trabajar sobre la BD
cursor = conexion.cursor()

#A el se le pasa la consulta, la consulta solo puede ir en una linea
#cursor.execute("CREATE TABLE usuarios (nombre VARCHAR(100),edad INTEGER, email VARCHAR(100))")

#Insertar un usuario en la tabla usuarios
#cursor.execute("INSERT INTO usuarios VALUES ('William','27','hector@ejemplo.com')")

#cursor.execute("SELECT * FROM usuarios")
#print(cursor)

#Para convertirlo en campos legibles
#Si se hace fetchone mas de una vez se van recorriendo los registros
#usuario = cursor.fetchone()
#print(usuario)
#Si quiero solo un dato 
#usuario_nombre = usuario[0]
#print(usuario_nombre)

#Agregar varios usuarios a la vez
#usuarios = [
#	('Will',23,'will@gmail.com'),
#	('Fabian',19,'fabian@mail.com'),
#	('Mario',34,'mario@pinchemail.com')
#]
#cursor.executemany('INSERT INTO usuarios VALUES(?,?,?)', usuarios)

#recupera multiples registros en forma de lista
cursor.execute('SELECT * FROM usuarios')
usuarios = cursor.fetchall()
#print(usuarios)
for usuario in usuarios:
	print("Nombre:",usuario[0],"Edad:",usuario[1])

#confirmar todos los cambios
conexion.commit()
#Se cierra la conexion
conexion.close()