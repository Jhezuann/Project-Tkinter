from tkinter import *
from tkinter import messagebox
import psycopg2

#Ventana principal
wn=Tk()
wn.title("Login")
wn.iconbitmap("img/logo.ico")
wn.geometry("250x300")
wn.resizable(0,0)
wn.config(bg="cyan")

#----
conn = psycopg2.connect(
		dbname="login",
		user="postgres",
		password="123456p",
		host="localhost",
		port="5432",
	)
cur=conn.cursor()

#Funciones
def ingresar():
    if (len(nombreUsuario.get())==0 or len(contraseñaUsuario.get())==0):
        messagebox.showinfo("Error", "Todos los campos son obligatorios")
        borrarCampos()
    else:
        cur.execute("SELECT * FROM register WHERE name=%s AND password=%s", (nombreUsuario.get(), contraseñaUsuario.get()))
        if cur.fetchone():
            wn.destroy()
            import ventanaA
            messagebox.showinfo("Login", "Usuario correcto, CONECTADO")
            borrarCampos()
        else:
            messagebox.showinfo("Error", "Usuario o contraseña incorrecto")
            borrarCampos()

def registrar():
    wn.destroy()
    import register

def borrarCampos():
    nombreUsuario.set("")
    contraseñaUsuario.set("")

def salir():
    wn.destroy()
    
#Label
titulo=Label(wn, text="Login", font=("Verdana", 20), bg="cyan")
titulo.grid(column=1,row=0, columnspan=2)

#espacio entre lineas
espacio1=Label(wn, text="", bg="cyan")
espacio1.grid(column=1,row=1)

nombreLabel=Label(wn, text="Nombre:", bg="cyan")
nombreLabel.grid(column=0,row=2)

#espacio entre lineas
espacio2=Label(wn, text="", bg="cyan")
espacio2.grid(column=3,row=3)

passLabel=Label(wn, text="Contraseña:", bg="cyan")
passLabel.grid(column=0,row=4)

#Entry
nombreUsuario=StringVar()
nombreEntry=Entry(wn, textvariable=nombreUsuario)
nombreEntry.grid(column=2,row=2)

contraseñaUsuario=StringVar()
passEntry=Entry(wn, textvariable=contraseñaUsuario, show="*")
passEntry.grid(column=2,row=4)

#espacio entre lineas
espacio3=Label(wn, text="", bg="cyan")
espacio3.grid(column=1,row=5)

#Botones
iniciarSeccion=Button(wn, text="Iniciar sección", command=ingresar)
iniciarSeccion.grid(column=2,row=6)

#espacio entre lineas
espacio4=Label(wn, text="", bg="cyan")
espacio4.grid(column=1,row=7)

registrar=Button(wn, text="Registrar", command=registrar)
registrar.grid(column=2,row=8)

#espacio entre lineas
espacio5=Label(wn, text="", bg="cyan")
espacio5.grid(column=1,row=9)

salir=Button(wn, text="Salir", command=salir)
salir.grid(column=2,row=10)

if __name__ == "__main__":
    wn.mainloop()