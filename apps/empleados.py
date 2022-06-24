from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import psycopg2

wn=Tk()
wn.title("Empleados")
wn.geometry("820x350")
wn.resizable(0,0)

#campos
id=StringVar()
nombre=StringVar()
apellido=StringVar()
age=StringVar()
cargo=StringVar()
salario=StringVar()

#Conn , cursor y tree
conn=psycopg2.connect(
        dbname="login",
        user="postgres",
        password="123456p",
        host="localhost",
        port="5432",
    )
cur=conn.cursor()

tree=ttk.Treeview(height=10, columns=('#0', '#1', '#2', '#3', '#4', '#5'))

#funciones
def selectclick(event):
	item=tree.identify('item',event.x,event.y)
	id.set(tree.item(item, "text"))
	nombre.set(tree.item(item, "values")[0])
	apellido.set(tree.item(item, "values")[1])
	age.set(tree.item(item, "values")[2])
	cargo.set(tree.item(item, "values")[3])
	salario.set(tree.item(item, "values")[4])

tree.bind("<Double-1>", selectclick)

def borrarCampos():
    id.set("")
    nombre.set("")
    apellido.set("")
    age.set("")
    cargo.set("")
    salario.set("")

def crear():
    if (len(nombre.get())==0 or len(apellido.get())==0 or len(age.get())==0 or len(cargo.get())==0 or len(salario.get())==0):
        messagebox.showerror("Error", "Todos los campos son obligatorios")
    else:
        cur.execute("INSERT INTO empleados (nombre, apellido, age, cargo, salario) VALUES (%s, %s, %s, %s, %s)", (nombre.get(), apellido.get(), age.get(), cargo.get(), salario.get()))
        conn.commit()
        messagebox.showinfo("Registro", "Empleado registrado correctamente")
        borrarCampos()

def actualizar():
    if (len(id.get())==0):
        messagebox.showerror("Error", "Seleccione un registro")
    elif (len(nombre.get())==0 or len(apellido.get())==0 or len(age.get())==0 or len(cargo.get())==0 or len(salario.get())==0):
        messagebox.showerror("Error", "Todos los campos son obligatorios")
    else:
        cur.execute("UPDATE empleados SET nombre=%s, apellido=%s, age=%s, cargo=%s, salario=%s WHERE ID=%s", (nombre.get(), apellido.get(), age.get(), cargo.get(), salario.get(), id.get()))
        conn.commit()
        messagebox.showinfo("Actualizar", "Empleado actualizado correctamente")
        borrarCampos()

def leer():
    cur.execute("SELECT * FROM empleados")
    rows=cur.fetchall()
    tree.delete(*tree.get_children())
    for row in rows:
        tree.insert("", 0, text=row[0], values=(row[1], row[2], row[3], row[4], row[5]))

def borrar():
    if (len(id.get())==0):
        messagebox.showerror("Error", "Seleccione un registro")
    else:
        cur.execute("DELETE FROM empleados WHERE ID=%s", (id.get(),))
        conn.commit()
        messagebox.showinfo("Borrar", "Empleado borrado correctamente")
        borrarCampos()

def salir():
    wn.destroy()
    import cruds


#Elementos graficos
# Tabla
tree.grid(row=0, column=0, columnspan=2, rowspan=10, padx=0, pady=122)
tree.column("#0", width=30)
tree.heading('#0', text="ID")
tree.heading('#1', text="Nombre")
tree.heading('#2', text="Apellido")
tree.column("#3", width=100)
tree.heading('#3', text="Edad")
tree.heading('#4', text="Cargo")
tree.column("#4", width=100)
tree.heading('#5', text="Salario")

leer()

#Etiquetas y cajas de texto

e=Entry(wn, textvariable=id)

l2=Label(wn, text="Nombre")
l2.place(x=45, y=30)
e2=Entry(wn, textvariable=nombre, width=20)
e2.place(x=95, y=30)

l3=Label(wn, text="Apellido")
l3.place(x=240, y=30)
e3=Entry(wn, textvariable=apellido, width=20)
e3.place(x=295, y=30)

l4=Label(wn, text="Edad")
l4.place(x=430, y=30)
e4=Entry(wn, textvariable=age, width=7)
e4.place(x=460, y=30)

l5=Label(wn, text="Cargo")
l5.place(x=140, y=60)
e5=Entry(wn, textvariable=cargo, width=20)
e5.place(x=185, y=60)

l6=Label(wn, text="Salario")
l6.place(x=360, y=60)
e6=Entry(wn, textvariable=salario, width=7)
e6.place(x=405, y=60)

l7=Label(wn, text="USD")
l7.place(x=460, y=60)

#Botones CRUD

b1=Button(wn, text="Crear", command=crear)
b1.place(x=605, y=0)

b1=Button(wn, text="Actualizar", command=actualizar)
b1.place(x=595, y=55)

b1=Button(wn, text="Actualizar registros", command=leer)
b1.place(x=700, y=0)

b1=Button(wn, text="Borrar", bg="red", command=borrar)
b1.place(x=735, y=55)

b1=Button(wn, text="Salir", command=salir)
b1.place(x=685, y=70)

wn.mainloop()