import tkinter as tk
from tkinter import *
import sqlite3

def buscarPatente():
    #Busco patente en BDD
    DB_NAME='Garage.db'
    conn=sqlite3.connect(DB_NAME)
    cursorBuscar=conn.cursor()
    cursorBuscar.execute("SELECT * FROM vehiculos WHERE patente = ?",(textPatente.get(),))
    resultado = (cursorBuscar.fetchone())

    #Resultado de la busqueda y muestra
    if (resultado):
        buscarID=conn.cursor()
        buscarID.execute("SELECT id FROM vehiculos WHERE patente = ?",(textPatente.get(),))
        resultado1 = (buscarID.fetchone())

        buscarFecha=conn.cursor()
        buscarFecha.execute("SELECT fecha_entrada,fecha_salida,pago FROM movimientos WHERE patente_id = ?",(resultado1[0],))
        resultado2 = (buscarFecha.fetchone())
        limpiarCampos()

        textPatente.insert(0, resultado[1])
        textMarca.insert(0, resultado[2])
        textModelo.insert(0, resultado[3])
        textColor.insert(0, resultado[4])
        textObservacion.insert(0, resultado[5])
        textEntrada.insert(0, resultado2[0])
        textMarca.config(state=DISABLED)
        textModelo.config(state=DISABLED)
        textColor.config(state=DISABLED)
        textObservacion.config(state=DISABLED)
        textEntrada.config(state=DISABLED)
        
        #TODO (error) se deberia validar si existe una fecha de salida y un estado de pago (no afecta)
        textSalida.insert(0, resultado2[1])
        textPago.insert(0, resultado2[2])
        textSalida.config(state=DISABLED)
        textPago.config(state=DISABLED)
    else:
        tk.messagebox.showerror(title='Error', message="Auto no encontrado")
        limpiarCampos()