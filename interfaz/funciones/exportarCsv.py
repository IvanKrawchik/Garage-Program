import sqlite3
import pandas as pd

def exportarCsv():
    DB_NAME='Garage.db'
    conn=sqlite3.connect(DB_NAME)

    usuarios = pd.read_sql('SELECT * FROM usuarios' ,conn)
    usuarios.to_csv('interfaz/exportaciones/csvUsuarios.csv', index=False)

    usuarios = pd.read_sql('SELECT * FROM vehiculos' ,conn)
    usuarios.to_csv('interfaz/exportaciones/csvVehiculos.csv', index=False)

    usuarios = pd.read_sql('SELECT * FROM movimientos' ,conn)
    usuarios.to_csv('interfaz/exportaciones/csvMovimientos.csv', index=False)