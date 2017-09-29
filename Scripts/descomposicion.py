import sys
if len(sys.argv) == 2:
	numero = int(sys.argv[1])
	
	if numero < 0 or numero > 9999:
		print("Error, argumentos incorrectos")
		print("Ex. descomposicion.py #Numero")
	else:
		#Aqui empieza la logica
		cadena = str(numero)
		longitud = len(cadena)
		for i in range(longitud):
			print("{:04d}".format(int(cadena[longitud-1-i])*10 ** i))



else:
	print("Error, argumentos incorrectos")
	print("Ex. descomposicion.py #Numero")
