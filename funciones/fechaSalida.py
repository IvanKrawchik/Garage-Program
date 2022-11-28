import tkinter as tk
from tkinter import *
import sqlite3
import datetime

def fechaSalida():
    #Busco patente ingresada y marco en movimientos fecha de salida
    DB_NAME='Garage.db'
    conn=sqlite3.connect(DB_NAME)
    buscarID=conn.cursor()
    buscarID.execute("SELECT id FROM movil WHERE patente = ?",(textPatente.get(),))
    respuesta=buscarID.fetchone()
    currentDateTime = datetime.datetime.now().replace(second=0, microsecond=0)
    textPago.insert(0, currentDateTime)
    textPago.config(state=DISABLED)
    insertFecha=conn.cursor()
    insertFecha.execute("UPDATE movimientos SET fecha_salida=? WHERE patente_id=?;",(currentDateTime,respuesta[0]))
    conn.commit()