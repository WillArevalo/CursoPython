from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import colorchooser as ColorChosser
from tkinter import filedialog as FileDialog


root = Tk()

def test():
	#MessageBox.showinfo("Hola","Hola Mundo")#Minimo dos argumentos, titulo, mensaje
	#MessageBox.showwarning("Alerta","Sección solo para administradores.")#Minimo dos argumentos, titulo, mensaje
	#MessageBox.showerror("Error!","Ha ocurrido un error inesperado.")
	#resultado = MessageBox.askquestion("Salir","¿Esta seguro que desea salir sin guardar?")
	#if resultado == "yes":
	#	root.destroy()
	#resultado = MessageBox.askokcancel("Salir","¿Sobreescribir el fichero actual?")
	#if resultado: #bool
	#	root.destroy()
	#resultado = MessageBox.askquestion("Salir","¿Esta seguro que desea salir sin guardar?")
	#if resultado: #bool
	#	root.destroy()
	#resultado = MessageBox.askretrycancel("Reintentar", "No se puede conectar")
	#if resultado:
	#	root.destroy()
	#color = ColorChosser.askcolor(title="Elige un pinchi color")
	#print(color)
	#ruta = FileDialog.askopenfilename(title="Abrir un pinchi fichero", initialdir="C:", filetypes=(("Ficheros de texto","*.txt"),("Fichero de texto avanzado","*.txt2"),("Todos los ficheros","*.*")))#Opc:initialdir,exttype
	#print(ruta)
	fichero = FileDialog.asksaveasfile(title="Guardar un pinchoo fichero", mode="r+", defaultextension=".txt")
	#Equivale a open("ruta","w")
	#Opc:Mode(w,r,a,w+,r+,a+); defaultextension(Como se guardara al finalizar)
	if fichero is not None:
		fichero.write("Hola escribi aqui desde popups.py")
		fichero.close()


Button(root, text="clickeame", command=test).pack()


#Abajo de todo
root.mainloop()

#Nota: cambiando la extension por .pyw (python windows)
		#No se abre la terminal