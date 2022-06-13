from tkinter import *
from tkinter import messagebox
import psycopg2

wn2=Tk()
wn2.title("Register")
wn2.iconbitmap("img/logo.ico")

#---
conn = psycopg2.connect(
		dbname="login",
		user="postgres",
		password="123456p",
		host="localhost",
		port="5432",
	)
cur=conn.cursor()

#Funciones
def registrar():
    cur.execute("SELECT * FROM register WHERE name=%s", (nombreUsuario.get(),))
    if cur.fetchone():
        messagebox.showerror("Error", "El usuario ya existe")
        borrarCampos()

    elif (len(nombreUsuario.get())==0 or len(contraseñaUsuario.get())==0 or len(apodoUsuario.get())==0):
        messagebox.showerror("Error", "Todos los campos son obligatorios")
        borrarCampos()

    elif nombreUsuario.get()==apodoUsuario.get():
        messagebox.showerror("Error", "El nombre de usuario y el apodo no pueden ser iguales")
        borrarCampos()

    else:
        cur.execute("INSERT INTO register (name, password, apodo) VALUES (%s, %s, %s)", (nombreUsuario.get(), contraseñaUsuario.get(), apodoUsuario.get()))
        conn.commit()
        messagebox.showinfo("Registro", "Usuario registrado correctamente")
        borrarCampos()

def borrarCampos():
    nombreUsuario.set("")
    contraseñaUsuario.set("")
    apodoUsuario.set("")

def volver():
    wn2.destroy()
    import main

#Frame
frame2=Frame(wn2)
frame2.pack()
frame2.config(width=340, height=480)#, bg="cyan")

#Label
titulo=Label(frame2, text="Register", font=("Verdana", 20))
titulo.grid(column=0,row=0, columnspan=2)

nombreLabel=Label(frame2, text="Nombre:")
nombreLabel.grid(column=0,row=1)

passLabel=Label(frame2, text="Contraseña:")
passLabel.grid(column=0,row=2)

passLabel=Label(frame2, text="Apodo:")
passLabel.grid(column=0,row=3)

#Entry
nombreUsuario=StringVar()
nombreEntry=Entry(frame2, textvariable=nombreUsuario)
nombreEntry.grid(column=1,row=1)

contraseñaUsuario=StringVar()
passEntry=Entry(frame2, textvariable=contraseñaUsuario, show="*")
passEntry.grid(column=1,row=2)

apodoUsuario=StringVar()
apodoEntry=Entry(frame2, textvariable=apodoUsuario)
apodoEntry.grid(column=1,row=3)

#Botones
registrar=Button(frame2, text="Registrar", command=registrar)
registrar.grid(column=0,row=4, columnspan=2)

volver=Button(frame2, text="Volver", command=volver)
volver.grid(column=0,row=5, columnspan=2)

wn2.mainloop()