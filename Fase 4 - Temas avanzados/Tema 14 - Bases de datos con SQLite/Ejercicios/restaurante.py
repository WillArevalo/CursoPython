import sqlite3
import os

def crear_db():
	conexion = sqlite3.connect("restaurante.db")
	cursor = conexion.cursor()

	try:
		cursor.execute('''CREATE TABLE categoria(
				id INTEGER PRIMARY KEY AUTOINCREMENT,
				nombre VARCHAR(100) UNIQUE NOT NULL)''')

	except sqlite3.OperationalError:
		print("La tabla de Categorias ya ha sido creada")
	else:
		print("La tabla de Categorias se ha creado con exito")

	try:
		cursor.execute('''CREATE TABLE plato(
				id INTEGER PRIMARY KEY AUTOINCREMENT,
				nombre VARCHAR(100) UNIQUE NOT NULL,
				categoria_id INTEGER NOT NULL,
				FOREIGN KEY(categoria_id) REFERENCES categoria(id))''')
	except sqlite3.OperationalError:
		print("La tabla de Platos ya ha sido creada")
	else:
		print("La tabla de Platos se ha creado con exito")

	conexion.close()


def agregar_categoria():
	categoria = input("¿Nombre de la nueva categoria?\n> ")

	conexion = sqlite3.connect("restaurante.db")
	cursor = conexion.cursor()

	try:
		cursor.execute("INSERT INTO categoria VALUES (null, '{}')".format(categoria))	
	except sqlite3.IntegrityError:
		print("La categoria '{}' ya existe".format(categoria))
	else:
		print("Categoria '{}' creada correctamente".format(categoria))

	conexion.commit()
	conexion.close()

	input("\nDale enter para continuar...")
	os.system('cls')

def agregar_plato():

	conexion = sqlite3.connect("restaurante.db")
	cursor = conexion.cursor()

	categorias = cursor.execute("SELECT * FROM categoria").fetchall()
	print("\nSelecciona una categoria para añadir el plato:")
	for categoria in categorias:
		print("[{}] {}".format(categoria[0], categoria[1]))

	categoria_usuario = int(input("> "))

	plato = input("\n¿Nombre del nuevo plato?\n> ")

	try:
		cursor.execute("INSERT INTO plato VALUES (null, '{}', {})".format(plato, categoria_usuario))	
	except sqlite3.IntegrityError:
		print("El plato '{}' ya existe".format(plato))
	else:
		print("Plato '{}' creada correctamente".format(plato))


	conexion.commit()
	conexion.close()

	input("\nDale enter para continuar...")
	os.system('cls')

def mostrar_menu():

	conexion = sqlite3.connect("restaurante.db")
	cursor = conexion.cursor()

	categorias = cursor.execute("SELECT * FROM categoria").fetchall()	
	for categoria in categorias:
		print("\n"+categoria[1]+":")
		platos = cursor.execute("SELECT * FROM plato WHERE categoria_id={}".format(categoria[0])).fetchall()
		for plato in platos:
			print("\t{}".format(plato[1]))

	conexion.close()

	input("\nDale enter para continuar...")
	os.system('cls')

#Crear la base de datos
crear_db()

# Menu de opciones del programa
while True:
	print("\nBienvenido al gestor del restaurante!")
	opcion = input("\nIntroduce una opcion:\n[1] Agregar una categoria\n[2] Agregar un plato\n[3] Mostrar menu\n[4] Salir del programa \n> ")

	if opcion == "1":
		agregar_categoria()

	elif opcion == "2":
		agregar_plato()

	elif opcion == "3":
		mostrar_menu()

	elif opcion == "4":
		input("Nos vemos!")
		os.system('cls')
		break

	else:
		print("Opcion incorrecta")
		input("\nDale enter para continuar...")
		os.system('cls')