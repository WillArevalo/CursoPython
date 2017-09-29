from tkinter import *

#Configuracion de la raiz
root = Tk()

#Configuracion de un marco
#frame = Frame(root, width=480, height=320)
#frame.pack()

#label = Label(frame, text='¡Hola mundo!')
#label.place(x=210, y=160)
"""
#Variables dinamicas
texto = StringVar()
texto.set("Un nuevo texto")

Label(root, text="¡Hola mundo!").pack(anchor="nw")
label = Label(root, text="Otra etiqueta")
label.pack(anchor="center")
label.config(bg="blue", fg="yellow", font=("Verdana",16))#fg(color de la letra)
label.config(textvariable=texto)
Label(root, text="¡Ultima etiqueta!").pack(anchor="se")
"""
imagen = PhotoImage(file="Runner99.gif")
Label(root, image=imagen, bd=0).pack(side="left")


#Finalmente bucle de la aplicacion
root.mainloop()