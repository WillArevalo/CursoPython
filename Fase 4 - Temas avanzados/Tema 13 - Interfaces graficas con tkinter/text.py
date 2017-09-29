from tkinter import *

root = Tk()

root.title("Hola mundo") #Titulo
root.resizable(1,1) #No sea redimensionable, bool
root.iconbitmap('hola.ico') #favicon

texto = Text(root)
texto.pack()
texto.config(width=30,height=10, font=("Consolas",12), padx=15, pady=15, selectbackground="orange")#No se mide en pixeles si no en lineas







#Abajo de todo
root.mainloop()

#Nota: cambiando la extension por .pyw (python windows)
		#No se abre la terminal