import tkinter as tk
from tkinter import *
import sqlite3

def pagarServicio():
    #Busco patente ingresada y marco en movimientos como pagado
    DB_NAME='Garage.db'
    conn=sqlite3.connect(DB_NAME)
    buscarID=conn.cursor()
    buscarID.execute("SELECT id FROM movil WHERE patente = ?",(textPatente.get(),))
    respuesta=buscarID.fetchone()
    textPago.insert(0, "Pagado")
    textPago.config(state=DISABLED)
    insertPago=conn.cursor()
    insertPago.execute("UPDATE movimientos SET pago=? WHERE patente_id=?;",("Pagado",respuesta[0]))
    conn.commit()
