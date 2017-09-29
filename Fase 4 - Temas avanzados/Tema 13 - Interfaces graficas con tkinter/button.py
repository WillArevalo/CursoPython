from tkinter import *

#def hola():
#	print("Hola mundo")
#def crear_label():
#	Label(root, text="Hola soy un label dinamico").pack()
def sumar():
	r.set(float(n1.get()) + float(n2.get()))
	reset()

def restar():
	r.set(float(n1.get()) - float(n2.get()))
	reset()

def multiplicar():
	r.set(float(n1.get()) * float(n2.get()))
	reset()

def dividir():
	r.set(float(n1.get()) / float(n2.get()))
	reset()

def reset():
	n2.set("")
	n1.set("")

#Configuracion de la raiz
root = Tk()
root.config(bd=15)

n1,n2,r = StringVar(), StringVar(), StringVar()

Label(root, text="Número 1").pack()
Entry(root, justify="center", textvariable=n1).pack()  #Primer numero
Label(root, text="Número 2").pack()
Entry(root, justify="center", textvariable=n2).pack()  #Segundo numero
frame = Frame(root, bd=10)
frame.pack()
Button(frame, text="+", bd=5, command=sumar, font=("Verdana",13)).grid(row=0,column=1)
Button(frame, text="-", bd=5, command=restar, font=("Verdana",13)).grid(row=0,column=2)
Button(frame, text="x", bd=5, command=multiplicar, font=("Verdana",13)).grid(row=0,column=3)
Button(frame, text="/", bd=5, command=dividir, font=("Verdana",13)).grid(row=0,column=4)
Entry(root, justify="center", textvariable=r, font=("Verdana",10), state="disabled").pack()  #Resultado
Label(root, text="Resultado").pack()










#Abajo de todo
root.mainloop()

#Nota: cambiando la extension por .pyw (python windows)
		#No se abre la terminal