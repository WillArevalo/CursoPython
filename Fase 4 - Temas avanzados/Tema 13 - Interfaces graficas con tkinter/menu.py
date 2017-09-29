from tkinter import *

root = Tk()

menubar = Menu(root)
root.config(menu=menubar)

filemenu = Menu(menubar, tearoff=0)

filemenu.add_command(label="Nuevo")

filemenu.add_command(label="Abrir")

filemenu.add_command(label="Guardar")

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)


editmenu = Menu(menubar, tearoff=0)

editmenu.add_command(label="Pencil")

editmenu.add_command(label="Pen")

editmenu.add_command(label="Marker")

helpmenu = Menu(menubar, tearoff=0)

helpmenu.add_command(label="Help")

helpmenu.add_command(label="Authors")

helpmenu.add_command(label="Version")


menubar.add_cascade(label="Archivo", menu=filemenu)
menubar.add_cascade(label="Editar", menu=editmenu)
menubar.add_cascade(label="Ayuda", menu=helpmenu)








#Abajo de todo
root.mainloop()

#Nota: cambiando la extension por .pyw (python windows)
		#No se abre la terminal