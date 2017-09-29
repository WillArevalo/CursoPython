from tkinter import *

root = Tk()

root.title("Hola mundo") #Titulo
root.resizable(1,1) #No sea redimensionable, bool
root.iconbitmap('hola.ico') #favicon

frame = Frame(root, width=480,height=320) #El frame va dentro del root,
											#Y se configura el tamaño,
#frame.pack(side="bottom",anchor="w") #Que se distribuya dentro de root, pero en el centro arriba por defecto
										#anchor es orientacion(west, est)
frame.pack(fill='both', expand=1)#Rellena(x,y or both), expande(1,0)
#configuraciones: 
#Cursor
#BackGround
#BorderDimensions(width, height)
#relief(Cambia el tipo de borde)
frame.config(cursor="pirate", bg="lightgray", bd=25, relief="sunken") 
root.config(cursor="arrow", bg="gray", bd=15, relief="ridge") 








#Abajo de todo
root.mainloop()

#Nota: cambiando la extension por .pyw (python windows)
		#No se abre la terminal