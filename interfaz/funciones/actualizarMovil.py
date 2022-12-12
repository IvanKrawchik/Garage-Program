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