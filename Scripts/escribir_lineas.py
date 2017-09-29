import sys 
# el primer argumento [0] es el del nombre del script
if len(sys.argv) == 3: # Aseguro que se ingresen los 3 argumentos
	texto = sys.argv[1] #primer argumento 
	repeticiones = int(sys.argv[2]) # segundo argumento
	for r in range(repeticiones):
		print(texto)
else:
	print("""No se han ingresado los argumentos de manera adecuada.
		Ex. python script.py 'texto' #lineas""")
