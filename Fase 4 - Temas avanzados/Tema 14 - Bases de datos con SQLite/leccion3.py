import sqlite3

conexion = sqlite3.connect("usuarios_autoincremental.db")
cursor = conexion.cursor()
#Consultas
#cursor.execute("SELECT * FROM usuarios WHERE id=1")

#usuario = cursor.fetchone()
#print(usuario)

#cursor.execute("SELECT * FROM usuarios WHERE edad=19")#Multiples campos

#usuarios = cursor.fetchall()
#print(usuarios)

#Actualizar
cursor.execute("UPDATE usuarios SET nombre='Hector Acosta', edad=19 WHERE dni='11111111A'")

#Borrar
cursor.execute("DELETE usuarios WHERE dni='11111111A'")


conexion.commit()
conexion.close()