def palindromo(palabra):
	"""
	La funcion palindromo(palabra) recibe una palabra.
	Si la palabra es un palindromo devuelve True, si no False

	Un palindromo es una palabra o frase que se lee igual
	tanto de izquierda a derecha  como de derecha a izquierda


	>>> palindromo("radar")
	True

	>>> palindromo("somos")
	True

	>>> palindromo("holah")
	False

	>>> palindromo("Ana")
	True

	>>> palindromo("atar a la rata")
	True
	"""

	if palabra.lower().replace(" ","") == palabra[::-1].lower().replace(" ",""):
		return True
	else:
		return False

if __name__ == "__main__":
	import doctest
	doctest.testmod()