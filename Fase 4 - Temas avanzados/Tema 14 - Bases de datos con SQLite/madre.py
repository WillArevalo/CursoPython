from tkinter import *
from io import open


root = Tk()

root.title("OLX Feed - Madre") #Titulo
root.resizable(1,1) #No sea redimensionable, bool

container = Frame(root, width=800,height=600) 
container.pack(fill='both', expand=1)

Label(container, text='OLX FEED', bg="lightgray", fg="orange", padx=15, pady=15, font=("Verdana",9)).pack()

Label(container, text='ID', font=("Verdana",9)).pack()
id = Entry(container, justify="center", width=100 )
id.pack()

Label(container, text='Titulo', font=("Verdana",9)).pack()
titulo = Entry(container, justify="center", width=100 )
titulo.pack()

Label(container, text='Descripcion', font=("Verdana",9)).pack()
descripcion = Text(container, width=75, height=5, selectbackground="orange"  )
descripcion.pack()

frame = Frame(container, width=800, height=600, padx=15, pady=15)
frame.pack(fill='both', expand=1)

Label(frame, text='Correo del contacto', padx=5, pady=3, font=("Verdana",9)).grid(row=0,column=0)
email = Entry(frame, justify="center", width=40 )
email.grid(row=0,column=1)

Label(frame, text='Tel del contacto', padx=5, pady=3, font=("Verdana",9)).grid(row=0,column=2)
phone = Entry(frame, justify="center", width=40 )
phone.grid(row=0,column=3)

Label(frame, text='Nombre del contacto', padx=5, pady=3, font=("Verdana",9)).grid(row=1,column=0)
nombre = Entry(frame, justify="center", width=40 )
nombre.grid(row=1,column=1)

Label(frame, text='Categoria', padx=5, pady=3, font=("Verdana",9)).grid(row=1,column=2)
categoria = Entry(frame, justify="center", width=40 )
categoria.grid(row=1,column=3)

Label(frame, text='Precio', padx=5, pady=3, font=("Verdana",9)).grid(row=2,column=0)
precio = Entry(frame, justify="center", width=40 )
precio.grid(row=2,column=1)

Label(frame, text='Nro Habitaciones', padx=5, pady=3, font=("Verdana",9)).grid(row=2,column=2)
n_habitacion = Entry(frame, justify="center", width=40 )
n_habitacion.grid(row=2,column=3)

Label(frame, text='Nro baños', padx=5, pady=3, font=("Verdana",9)).grid(row=3,column=0)
n_banos = Entry(frame, justify="center", width=40 )
n_banos.grid(row=3,column=1)

Label(frame, text='Metros cuadrados', padx=5, pady=3, font=("Verdana",9)).grid(row=3,column=2)
metros2dos = Entry(frame, justify="center", width=40 )
metros2dos.grid(row=3,column=3)

Label(frame, text='tipo de apartamento', padx=5, pady=3, font=("Verdana",9)).grid(row=4,column=0)
apartamentotipo = Entry(frame, justify="center", width=40 )
apartamentotipo.grid(row=4,column=1)

Label(frame, text='Antiguedad', padx=5, pady=3, font=("Verdana",9)).grid(row=4,column=2)
antiguedad = Entry(frame, justify="center", width=40 )
antiguedad.grid(row=4,column=3)

#Imagenes

frame2 = Frame(container, width=800, padx=15, pady=15)
frame2.pack(fill='both', expand=1)

Label(frame2, text='Url Imagenes', font=("Verdana",9)).grid(row=5,column=0)
Url_Imagen1 = Entry(frame2, width=75, selectbackground="orange"  )
Url_Imagen1.grid(row=0,column=1)
Url_Imagen2 = Entry(frame2, width=75, selectbackground="orange"  )
Url_Imagen2.grid(row=1,column=1)
Url_Imagen3 = Entry(frame2, width=75, selectbackground="orange"  )
Url_Imagen3.grid(row=2,column=1)
Url_Imagen4 = Entry(frame2, width=75, selectbackground="orange"  )
Url_Imagen4.grid(row=3,column=1)
Url_Imagen5 = Entry(frame2, width=75, selectbackground="orange"  )
Url_Imagen5.grid(row=4,column=1)
Url_Imagen6 = Entry(frame2, width=75, selectbackground="orange"  )
Url_Imagen6.grid(row=5,column=1)
Url_Imagen7 = Entry(frame2, width=75, selectbackground="orange"  )
Url_Imagen7.grid(row=6,column=1)
Url_Imagen8 = Entry(frame2, width=75, selectbackground="orange"  )
Url_Imagen8.grid(row=7,column=1)
Url_Imagen9 = Entry(frame2, width=75, selectbackground="orange"  )
Url_Imagen9.grid(row=8,column=1)
Url_Imagen10 = Entry(frame2, width=75, selectbackground="orange"  )
Url_Imagen10.grid(row=9,column=1)






footer = Frame(container, width=800, padx=15, pady=15)
footer.pack(fill='both', expand=1)
#Abajo de todo
root.mainloop()

#Nota: cambiando la extension por .pyw (python windows)
		#No se abre la terminal