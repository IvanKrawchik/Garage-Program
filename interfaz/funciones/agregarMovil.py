import tkinter as tk
from tkinter import *
import sqlite3

def agregarMovil():
    #Busco patente en BDD
    DB_NAME='Garage.db'
    conn=sqlite3.connect(DB_NAME)
    Cursor=conn.cursor()

    Cursor.execute("INSERT INTO autos (patente,marca,modelo,color,observacion) VALUES (?,?,?,?,?);",())

    # resultado = Cursor.fetchone()
    if Cursor.fetchone():
        print("Datos del auto registrado: ")
        print()
        # print("Patente: ", resultado[0], "\nMarca: ", resultado[1], "\nModelo: ", resultado[2], "\nColor: ", resultado[3] , "\nObservacion: ", resultado[4])
    else:
        print("Auto no registrado")


# Cursor.execute("INSERT INTO movimientos (fecha_entrada,patente_id) VALUES (?,?);",('now',textPatente.get()))