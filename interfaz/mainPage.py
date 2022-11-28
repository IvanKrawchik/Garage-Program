import tkinter as tk
from tkinter import *
import sqlite3
import datetime

def mainPage():
    raiz = Tk()
    raiz.geometry('350x450')
    raiz.resizable(0,0)
    raiz.title('Garage')
    raiz.configure(bg='grey')


    patente = tk.Label(raiz, text="Patente:",width=11)
    textPatente=tk.Entry(raiz,border=4,width=23)

    marca = tk.Label(raiz, text="Marca:",width=11)
    textMarca=tk.Entry(raiz,border=4,width=23)

    modelo = tk.Label(raiz, text="Modelo:",width=11)
    textModelo=tk.Entry(raiz,border=4,width=23)

    color = tk.Label(raiz, text="Color:",width=11)
    textColor=tk.Entry(raiz,border=4,width=23)

    observacion = tk.Label(raiz, text="Observaciones:",width=11)
    textObservacion=tk.Entry(raiz,border=4,width=23)

    entrada = tk.Label(raiz, text="Entrada:",width=11)
    textEntrada=tk.Entry(raiz,border=4,width=23)

    salida = tk.Label(raiz, text="Salida:",width=11)
    textSalida=tk.Entry(raiz,border=4,width=23)

    pago = tk.Label(raiz, text="Pago:",width=11)
    textPago=tk.Entry(raiz,border=4,width=23)

    patente.place(x=15, y=40)
    textPatente.place(x=115,y=40)
    marca.place(x=15, y=80)
    textMarca.place(x=115,y=80)
    modelo.place(x=15, y=110)
    textModelo.place(x=115,y=110)
    color.place(x=15, y=140)
    textColor.place(x=115,y=140)
    observacion.place(x=15, y=170)
    textObservacion.place(x=115,y=170)
    entrada.place(x=15, y=200)
    textEntrada.place(x=115,y=200)
    salida.place(x=15, y=230)
    textSalida.place(x=115,y=230)
    pago.place(x=15, y=270)
    textPago.place(x=115,y=270)

    def buscarPatente():
        #Busco patente en BDD
        DB_NAME='Garage.db'
        conn=sqlite3.connect(DB_NAME)
        cursorBuscar=conn.cursor()
        cursorBuscar.execute("SELECT * FROM movil WHERE patente = ?",(textPatente.get(),))
        resultado = (cursorBuscar.fetchone())

        if (resultado):
            print("Datos del auto registrado: ")
            print("Patente: ", resultado[1], "\nMarca: ", resultado[2], "\nModelo: ", resultado[3], "\nColor: ", resultado[4] , "\nObservacion: ", resultado[5])
        else:
            print("Auto no encontrado")
            print("Patente: ",textPatente.get())

    def agregarMovil():
        #Agregar movil en BDD
        DB_NAME='Garage.db'
        conn=sqlite3.connect(DB_NAME)
        Cursor=conn.cursor()

        #Obtener fecha actual del sistema
        currentDateTime = datetime.datetime.now()

        if(textPatente.get()!="" and textMarca.get()!="" and textModelo.get()!="" and textColor.get()!=""):
            Cursor.execute("INSERT INTO movil (patente,marca,modelo,color,observaciones) VALUES (?,?,?,?,?);",(textPatente.get(),textMarca.get(),textModelo.get(),textColor.get(),textObservacion.get()))
            conn.commit()
            Cursor.execute("SELECT id FROM movil WHERE patente = ?",(textPatente.get(),))
            resultado=(Cursor.fetchone())
            Cursor.execute("INSERT INTO movimientos (fecha_entrada,patente_id) VALUES (?,?);",(currentDateTime,resultado[0]))
            conn.commit()
            print("auto registrado")
        else:
            print("Auto no registrado")

    buttonPatente=tk.Button(raiz, text="Buscar", width=10,command=buscarPatente)
    ingresar=tk.Button(raiz, text="Ingresar vehiculo", width=15,command=agregarMovil)
    importar=tk.Button(raiz, text="Importar datos", width=15)
    exportar=tk.Button(raiz, text="Exportar datos", width=15)
    buttonPatente.place(x=270, y=40)
    ingresar.place(x=110,y=330)
    importar.place(x=50,y=370)
    exportar.place(x=180,y=370)

    raiz.mainloop()

if __name__ == '__main__':
    mainPage()

