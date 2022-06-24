from tkinter import *
from math import *

w4=Tk()
w4.title("CALCULADORA")
w4.geometry("392x600")
w4.configure(background="SkyBlue4")
color_boton=("gray77")
 
#Funciones
def btnClik(num):
    global operador
    operador=operador+str(num)
    input_text.set(operador)

def resultado():
    global operador
    try:
        opera=str(eval(operador))
        input_text.set(opera)
    except:
        input_text.set("ERROR")
    operador = ""

def clear():
    global operador
    operador=("")
    input_text.set("0")

def salir():
    w4.destroy()
    import ventanaA

ancho_boton=11
alto_boton=3
input_text=StringVar()
operador=""
 
Salida=Entry(w4,font=('arial',20,'bold'),width=22,
textvariable=input_text,bd=20,insertwidth=4,bg="powder blue",justify="right")
Salida.place(x=10,y=60)
 
#AÑADIR BOTONES.
Button(w4,text="0",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(0)).place(x=17,y=180)
Button(w4,text="1",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(1)).place(x=107,y=180)
Button(w4,text="2",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(2)).place(x=197,y=180)
Button(w4,text="3",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(3)).place(x=287,y=180)
Button(w4,text="4",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(4)).place(x=17,y=240)
Button(w4,text="5",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(5)).place(x=107,y=240)
Button(w4,text="6",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(6)).place(x=197,y=240)
Button(w4,text="7",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(7)).place(x=287,y=240)
Button(w4,text="8",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(8)).place(x=17,y=300)
Button(w4,text="9",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(9)).place(x=107,y=300)
Button(w4,text="π",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("pi")).place(x=197,y=300)
Button(w4,text=",",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(".")).place(x=287,y=300)
Button(w4,text="+",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("+")).place(x=17,y=360)
Button(w4,text="-",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("-")).place(x=107,y=360)
Button(w4,text="*",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("*")).place(x=197,y=360)
Button(w4,text="/",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("/")).place(x=287,y=360)
Button(w4,text="√",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("sqrt(")).place(x=17,y=420)
Button(w4,text="(",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("(")).place(x=17,y=480)
Button(w4,text=")",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(")")).place(x=107,y=480)
Button(w4,text="%",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("%")).place(x=197,y=480)
Button(w4,text="ln",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("log(")).place(x=287,y=480)
Button(w4,text="C",bg=color_boton,width=ancho_boton,height=alto_boton,command=clear).place(x=107,y=420)
Button(w4,text="EXP",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("**")).place(x=197,y=420)
Button(w4,text="=",bg=color_boton,width=ancho_boton,height=alto_boton,command=resultado).place(x=287,y=420)
Button(w4, text="Salir",bg=color_boton,width=ancho_boton,height=alto_boton,command=salir).place(x=150,y=540)
 
clear()
 
w4.mainloop()