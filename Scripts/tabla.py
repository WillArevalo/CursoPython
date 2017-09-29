import sys
if len(sys.argv) == 3:
	filas = int(sys.argv[1])
	columnas = int(sys.argv[2])
	if filas < 1 or filas > 9 or columnas < 1 or columnas > 9:
		print("Error - Filas o columnas incorrectos")
		print("Ex. tabla.py [1-9] [1-9]")
	else:
		#Aqui empieza la logica
		for f in range(filas):
			print("") # ejecuta un salto de linea en cada fila
			for c in range(columnas):
				print(" * ", end='')


else:
	print("Error, argumentos incorrectos")
	print("Ex. tabla.py [1-9] [1-9]")