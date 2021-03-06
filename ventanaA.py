from tkinter import *
from tkinter import messagebox

wn3=Tk()
wn3.title("Ventana principal")
wn3.iconbitmap("img/logo.ico")
wn3.geometry("250x300")
wn3.resizable(0,0)
wn3.config(bg="cyan")

#calculadora
def calculadora():
    wn3.destroy()
    from apps import calculadora

def salir():
    wn3.destroy()

def juego():
    from apps import juego

def BaseDeDatos():
    wn3.destroy()
    from apps import cruds

#Label
titulo=Label(wn3, text="Menu principal", font=("Verdana", 20), bg="cyan")
titulo.grid(column=1,row=0)

#espacio entre lineas
espacio1=Label(wn3, text="", bg="cyan")
espacio1.grid(column=2, row=2)

#botones
btn1=Button(wn3, text="Calculadora", command=calculadora)
btn1.grid(column=1,row=3)

#espacio entre lineas
espacio2=Label(wn3, text="", bg="cyan")
espacio2.grid(column=2, row=4)

btn1=Button(wn3, text="juego", command=juego)
btn1.grid(column=1,row=5)

#espacio entre lineas
espacio3=Label(wn3, text="", bg="cyan")
espacio3.grid(column=2, row=6)

btn1=Button(wn3, text="Base de datos", command=BaseDeDatos)
btn1.grid(column=1,row=7)

#espacio entre lineas
espacio4=Label(wn3, text="", bg="cyan")
espacio4.grid(column=2, row=8)

button=Button(wn3, text="Salir", command=salir)
button.grid(column=1,row=9)

if __name__ == "__main__":
    wn3.mainloop()