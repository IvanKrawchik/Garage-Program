import tkinter as tk
from tkinter import *
import sqlite3

def buscarPatente():
    #Busco patente en BDD
    DB_NAME='Garage.db'
    conn=sqlite3.connect(DB_NAME)
    Cursor=conn.cursor()

    Cursor.execute("select patente,marca,modelo,color,observaciones from movil where patente = (?)",(textPatente.get(),))

    resultado = Cursor.fetchone()
    if resultado:
        print("Datos del auto registrado: ")
        print()
        print("Patente: ", resultado[0], "\nMarca: ", resultado[1], "\nModelo: ", resultado[2], "\nColor: ", resultado[3] , "\nObservacion: ", resultado[4])
    else:
        print("Auto no encontrado")