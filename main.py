from tkinter import *
from tkinter import messagebox
import psycopg2

#Ventana principal
wn=Tk()
wn.title("Login")
wn.iconbitmap("img/logo.ico")

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
    
#Frame
frame=Frame(wn)
frame.pack()
frame.config(width=10, height=10, bg="cyan")

#Label
titulo=Label(frame, text="Login", font=("Verdana", 20), bg="cyan")
titulo.grid(column=0,row=0, columnspan=2)

nombreLabel=Label(frame, text="Nombre:", bg="cyan")
nombreLabel.grid(column=0,row=1)

passLabel=Label(frame, text="Contraseña:", bg="cyan")
passLabel.grid(column=0,row=2)

#Entry
nombreUsuario=StringVar()
nombreEntry=Entry(frame, textvariable=nombreUsuario)
nombreEntry.grid(column=1,row=1)

contraseñaUsuario=StringVar()
passEntry=Entry(frame, textvariable=contraseñaUsuario, show="*")
passEntry.grid(column=1,row=2)

#Botones
iniciarSeccion=Button(frame, text="Iniciar sección", command=ingresar)
iniciarSeccion.grid(column=0,row=3, columnspan=2)

registrar=Button(frame, text="Registrar", command=registrar)
registrar.grid(column=0,row=4, columnspan=2)

if __name__ == "__main__":
    wn.mainloop()