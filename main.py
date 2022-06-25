from tkinter import *

def seleccionar():
    monitor.config(text="{}".format(opcion.get()))
def reset():
    opcion.set(None)
    monitor.config(text="")

root = Tk()
opcion = StringVar()
opcion.set(None)
Radiobutton(root, text="Peugeot", variable=opcion,
            value='Peugeot', command=seleccionar).pack(anchor=W)

Radiobutton(root, text="Opel", variable=opcion,
            value='Opel', command=seleccionar).pack(anchor=W)
Radiobutton(root, text="Renault", variable=opcion,
            value='Renault', command=seleccionar).pack(anchor=W)
Radiobutton(root, text="Seat", variable=opcion,
            value='Seat', command=seleccionar).pack(anchor=W)

monitor = Label(root)
monitor.pack()
Button(root, text="Reiniciar", command=reset).pack()

root.mainloop()

master = Tk()
elemento = StringVar()
listbox = Listbox(master)
for item in ["Pepe", "María", "Ernesto", "Ruben", "Carlos", "Laura", "Ana", "Lorena"]:
 listbox.insert(END, item)
listbox.pack()
label = Label(text="Lista de nombres de personas")
label.pack()
master.mainloop()