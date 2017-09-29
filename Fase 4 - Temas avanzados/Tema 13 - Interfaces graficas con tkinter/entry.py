from tkinter import *

#Configuracion de la raiz
root = Tk()

frame = Frame(root, width=320)
frame.grid(column=0)


label = Label(root, text="Nombre muy largo ")
label.grid(row=0,column=1, sticky="w", padx=5, pady=5)#Sticky orientacion

entry = Entry(root)
entry.grid(row=0,column=2, padx=5, pady=5)
entry.config(justify="right", state="disabled")

label2 = Label(root, text="Contraseña ")
label2.grid(row=1,column=1, sticky="w", padx=5, pady=5)

entry2 = Entry(root)
entry2.grid(row=1,column=2, padx=5, pady=5)
entry2.config(justify="center", state="normal", show="#")

frame2 = Frame(root, width=320)
frame2.grid(column=3, padx=5, pady=5)


#Finalmente bucle de la aplicacion
root.mainloop()