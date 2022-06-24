from tkinter import *
from tkinter import messagebox

wn3=Tk()
wn3.title("Base de datos")
wn3.geometry("250x300")
wn3.resizable(0,0)
wn3.config(bg="cyan")

def empleados():
    wn3.destroy()
    from apps import empleados

def estudiantes():
    wn3.destroy()
    from apps import estudiantes

def salir():
    wn3.destroy()
    import ventanaA

#Label
titulo=Label(wn3, text="Menu principal", font=("Verdana", 20), bg="cyan")
titulo.grid(column=1,row=0)

#espacio entre lineas
espacio1=Label(wn3, text="", bg="cyan")
espacio1.grid(column=2, row=2)

#botones
btn1=Button(wn3, text="Base de datos tipo empleados", command=empleados)
btn1.grid(column=1,row=3)

#espacio entre lineas
espacio2=Label(wn3, text="", bg="cyan")
espacio2.grid(column=2, row=4)

btn1=Button(wn3, text="Base de datos tipo estudiantes", command=estudiantes)
btn1.grid(column=1,row=5)

#espacio entre lineas
espacio4=Label(wn3, text="", bg="cyan")
espacio4.grid(column=2, row=8)

button=Button(wn3, text="Salir", command=salir)
button.grid(column=1,row=9)

if __name__ == "__main__":
    wn3.mainloop()