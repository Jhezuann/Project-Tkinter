from tkinter import *
from tkinter import messagebox

wn3=Tk()
wn3.title("Ventana principal")
wn3.iconbitmap("img/logo.ico")

#calculadora
def calculadora():
    wn3.destroy()
    import calculadora

def salir():
    wn3.destroy()

#Frame
frame3=Frame(wn3)
frame3.pack()
frame3.config(width=340, height=480, bg="cyan")

#botones
btn1=Button(frame3, text="Calculadora", command=calculadora)
btn1.grid(column=0,row=0, columnspan=2)

button=Button(frame3, text="Salir", command=salir)
button.grid(column=0,row=5, columnspan=2)

if __name__ == "__main__":
    wn3.mainloop()