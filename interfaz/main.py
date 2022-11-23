import tkinter as tk
from tkinter import *

raiz = Tk()
raiz.geometry('350x400')
raiz.resizable(0,0)
raiz.title('Garage')
raiz.configure(bg='grey')


patente = tk.Label(raiz, text="Patente:",width=6)
textPatente=tk.Entry(raiz,border=4,width=23)
buttonPatente=tk.Button(raiz, text="Buscar", width=10)

marca = tk.Label(raiz, text="Marca:",width=6)
textMarca=tk.Entry(raiz,border=4,width=23)

modelo = tk.Label(raiz, text="Modelo:",width=6)
textmodelo=tk.Entry(raiz,border=4,width=23)

color = tk.Label(raiz, text="Color:",width=6)
textColor=tk.Entry(raiz,border=4,width=23)

entrada = tk.Label(raiz, text="Entrada:",width=6)
textEntrada=tk.Entry(raiz,border=4,width=23)

salida = tk.Label(raiz, text="Salida:",width=6)
textSalida=tk.Entry(raiz,border=4,width=23)

pago = tk.Label(raiz, text="Pago:",width=6)
textPago=tk.Entry(raiz,border=4,width=23)

ingresar=tk.Button(raiz, text="Ingresar vehiculo", width=15)
importar=tk.Button(raiz, text="Importar datos", width=15)
exportar=tk.Button(raiz, text="Exportar datos", width=15)


patente.place(x=30, y=40)
textPatente.place(x=90,y=40)
buttonPatente.place(x=250, y=40)
marca.place(x=30, y=80)
textMarca.place(x=90,y=80)
modelo.place(x=30, y=110)
textmodelo.place(x=90,y=110)
color.place(x=30, y=140)
textColor.place(x=90,y=140)
entrada.place(x=30, y=170)
textEntrada.place(x=90,y=170)
salida.place(x=30, y=200)
textSalida.place(x=90,y=200)
pago.place(x=30, y=240)
textPago.place(x=90,y=240)
ingresar.place(x=110,y=300)
importar.place(x=50,y=340)
exportar.place(x=180,y=340)

raiz.mainloop()

