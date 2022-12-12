import tkinter as tk
from tkinter import *
from tkinter import messagebox
import sqlite3
import datetime
from interfaz.funciones.exportarCsv import exportarCsv
from interfaz.funciones.importarCsv import importarCsv

def mainPageAdmin():
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

    def limpiarCampos():
        textMarca.config(state=NORMAL)
        textModelo.config(state=NORMAL)
        textColor.config(state=NORMAL)
        textObservacion.config(state=NORMAL)
        textEntrada.config(state=NORMAL)
        textSalida.config(state=NORMAL)
        textPago.config(state=NORMAL)
        textPatente.delete(0,"end")
        textMarca.delete(0,"end")
        textModelo.delete(0,"end")
        textColor.delete(0,"end")
        textObservacion.delete(0,"end")
        textEntrada.delete(0,"end")
        textSalida.delete(0,"end")
        textPago.delete(0,"end")

    def fechaSalida():
        #Busco patente ingresada y marco en movimientos fecha de salida
        DB_NAME='Garage.db'
        conn=sqlite3.connect(DB_NAME)
        buscarID=conn.cursor()
        buscarID.execute("SELECT id FROM vehiculos WHERE patente = ?",(textPatente.get(),))
        respuesta=buscarID.fetchone()
        currentDateTime = datetime.datetime.now().replace(second=0, microsecond=0)
        textSalida.insert(0,currentDateTime)
        textSalida.config(state=DISABLED)
        insertFecha=conn.cursor()
        insertFecha.execute("UPDATE movimientos SET fecha_salida=? WHERE patente_id=?;",(currentDateTime,respuesta[0]))
        conn.commit()

    def pagarServicio():
        #Busco patente ingresada y marco en movimientos como pagado
        DB_NAME='Garage.db'
        conn=sqlite3.connect(DB_NAME)
        buscarID=conn.cursor()
        buscarID.execute("SELECT id FROM vehiculos WHERE patente = ?",(textPatente.get(),))
        respuesta=buscarID.fetchone()
        textPago.insert(0, "Pagado")
        textPago.config(state=DISABLED)
        insertPago=conn.cursor()
        insertPago.execute("UPDATE movimientos SET pago=? WHERE patente_id=?;",("Pagado",respuesta[0]))
        conn.commit()

    def buscarPatenteAdmin():
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
            if resultado2[1] != None:
                textSalida.insert(0, resultado2[1])
            if resultado2[2] != None:
                textPago.insert(0, resultado2[2])
            textPago.config(state=DISABLED)
        else:
            tk.messagebox.showerror(title='Error', message="Auto no encontrado")
            limpiarCampos()

    def actualizarMovil():
        DB_NAME='Garage.db'
        conn=sqlite3.connect(DB_NAME)
        cursorBuscar=conn.cursor()
        cursorBuscar.execute("SELECT id FROM vehiculos WHERE patente = ?",(textPatente.get(),))
        resultado = (cursorBuscar.fetchone())

        #Resultado de la busqueda y muestra
        if (resultado):
            buscarFecha=conn.cursor()
            buscarFecha.execute("SELECT fecha_entrada,fecha_salida,pago FROM movimientos WHERE patente_id = ?",(resultado[0],))
            resultado2 = (buscarFecha.fetchone())
            if (textEntrada.get()!=resultado2[0]) or (textSalida.get()!=resultado2[1]):
                actualizarMovil=conn.cursor()
                actualizarMovil.execute("UPDATE movimientos SET fecha_entrada=?, fecha_salida=? WHERE patente_id =?",(textEntrada.get(),textSalida.get(),resultado[0]))
                conn.commit()
                tk.messagebox.showinfo(title='Movil Actualizado', message="Auto actualizado")
                limpiarCampos()
            else:
                tk.messagebox.showerror(title='Error', message="Auto no actualizado, modificar fechas de ingreso/egreso")
                limpiarCampos()

    def agregarMovil():
        DB_NAME='Garage.db'
        conn=sqlite3.connect(DB_NAME)
        Cursor=conn.cursor()
        cursorPatente=conn.cursor()
        cursorPatente.execute("SELECT patente FROM vehiculos WHERE patente=?",(textPatente.get(),))
        resultadoPatente = (cursorPatente.fetchone())

        #Obtener fecha actual del sistema
        currentDateTime = datetime.datetime.now().replace(second=0, microsecond=0)

        #Agregar movil y movimiento de entrada
        if((textPatente.get()!="" and textMarca.get()!="" and textModelo.get()!="" and textColor.get()!="") and (resultadoPatente==False or resultadoPatente==None)):
            Cursor.execute("INSERT INTO vehiculos (patente,marca,modelo,color,observaciones) VALUES (?,?,?,?,?);",(textPatente.get(),textMarca.get(),textModelo.get(),textColor.get(),textObservacion.get()))
            conn.commit()
            Cursor.execute("SELECT id FROM vehiculos WHERE patente = ?",(textPatente.get(),))
            resultado=(Cursor.fetchone())
            Cursor.execute("INSERT INTO movimientos (fecha_entrada,patente_id) VALUES (?,?);",(currentDateTime,resultado[0]))
            conn.commit()
            tk.messagebox.showinfo(title='Login', message="Auto registrado")
            limpiarCampos()
        else:
            tk.messagebox.showerror(title='Login', message="Auto no registrado")

    buttonPatente=tk.Button(raiz, text="Buscar", width=10,command=buscarPatenteAdmin)
    buttonSalida=tk.Button(raiz, text="Salida", width=10, command=fechaSalida)
    buttonPagar=tk.Button(raiz, text="Pagar", width=10, command=pagarServicio)
    ingresar=tk.Button(raiz, text="Ingresar vehiculo", width=15,command=agregarMovil)
    actualizar=tk.Button(raiz, text="Actualizar vehiculo", width=15,command=actualizarMovil)
    importar=tk.Button(raiz, text="Importar CSV", width=15,command=importarCsv)
    exportar=tk.Button(raiz, text="Exportar en CSV", width=15, command=exportarCsv)
    limpiar=tk.Button(raiz, text="Limpiar campos", width=15, command=limpiarCampos)
    buttonPatente.place(x=270, y=40)
    buttonSalida.place(x=270,y=230)
    buttonPagar.place(x=270,y=270)
    ingresar.place(x=180,y=330)
    actualizar.place(x=50,y=330)
    importar.place(x=50,y=370)
    exportar.place(x=180,y=370)
    limpiar.place(x=240,y=415)

    raiz.mainloop()

if __name__ == '__main__':
    mainPageAdmin()

