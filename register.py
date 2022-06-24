from tkinter import *
from tkinter import messagebox
import psycopg2

wn2=Tk()
wn2.title("Register")
wn2.iconbitmap("img/logo.ico")
wn2.geometry("250x300")
wn2.resizable(0,0)
wn2.config(bg="cyan")

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

#Label
titulo=Label(wn2, text="Register", font=("Verdana", 20), bg="cyan")
titulo.grid(column=0,row=0, columnspan=2)

#espacio entre lineas
espacio1=Label(wn2, text="", bg="cyan")
espacio1.grid(column=1,row=1)

nombreLabel=Label(wn2, text="Nombre:", bg="cyan")
nombreLabel.grid(column=0,row=2)

#espacio entre lineas
espacio2=Label(wn2, text="", bg="cyan")
espacio2.grid(column=1,row=3)

passLabel=Label(wn2, text="Contraseña:", bg="cyan")
passLabel.grid(column=0,row=4)

#espacio entre lineas
espacio3=Label(wn2, text="", bg="cyan")
espacio3.grid(column=1,row=5)

apodoLabel=Label(wn2, text="Apodo:", bg="cyan")
apodoLabel.grid(column=0,row=6)

#Entry
nombreUsuario=StringVar()
nombreEntry=Entry(wn2, textvariable=nombreUsuario)
nombreEntry.grid(column=1,row=2)

contraseñaUsuario=StringVar()
passEntry=Entry(wn2, textvariable=contraseñaUsuario, show="*")
passEntry.grid(column=1,row=4)

apodoUsuario=StringVar()
apodoEntry=Entry(wn2, textvariable=apodoUsuario)
apodoEntry.grid(column=1,row=6)

#espacio entre lineas
espacio4=Label(wn2, text="", bg="cyan")
espacio4.grid(column=1,row=7)

#Botones
registrar=Button(wn2, text="Registrar", command=registrar)
registrar.grid(column=1,row=8)

#espacio entre lineas
espacio5=Label(wn2, text="", bg="cyan")
espacio5.grid(column=0,row=9)

volver=Button(wn2, text="Volver", command=volver)
volver.grid(column=1,row=10)

if __name__ == "__main__":
    wn2.mainloop()