import csv
import sqlite3
import datetime

#Importa Vehiculos y cuand hay un nuevo vehiculo agrega el movimiento
def importarVehiculos():
    # read the csv file
    with open('interfaz/exportaciones/csvVehiculos.csv' , 'r') as csvfile:
        # create the object of csv.reader()
        csv_file_reader = csv.reader(csvfile,delimiter=',')
        # skip the header 
        next(csv_file_reader,None)
        # create fileds 
        id =''
        patente=''
        marca=''
        modelo=''
        color = ''
        observaciones= ''
        
        # 2. connect database
        DB_NAME='Garage.db'
        conn=sqlite3.connect(DB_NAME)
        cursorEliminar=conn.cursor()
        cursor=conn.cursor()
        cursorMovimiento=conn.cursor()
        cursorId=conn.cursor()

        deleteQuery=f"DELETE FROM vehiculos"
        cursorEliminar.execute(deleteQuery)

        # 4. pase csv data
        for row in csv_file_reader:
            # skip the first row
            for i in range(len(row)):
                # assign each field its value
                id=row[0]
                patente=row[1]
                marca=row[2]
                modelo=row[3]
                color = row[4]
                observaciones= row[5]

            InsertQuery=f"INSERT OR IGNORE INTO vehiculos VALUES ('{id}','{patente}','{marca}','{modelo}','{color}','{observaciones}')"
            cursor.execute(InsertQuery)

            selectId=f"SELECT COUNT(*) FROM movimientos WHERE patente_id='{id}'"
            cursorId.execute(selectId)
            resultado=(cursorId.fetchone())
            if (int(resultado[0])<1):
                currentDateTime = datetime.datetime.now().replace(second=0, microsecond=0)
                insertMovimiento=f"INSERT INTO movimientos (fecha_entrada,patente_id) VALUES ('{currentDateTime}','{id}');"
                cursorMovimiento.execute(insertMovimiento)
        conn.commit()
        conn.close()

def importarUsuarios():
    # read the csv file
    with open('interfaz/exportaciones/csvUsuarios.csv' , 'r') as csvfile:
        # create the object of csv.reader()
        csv_file_reader = csv.reader(csvfile,delimiter=',')
        # skip the header 
        next(csv_file_reader,None)
        # create fileds 
        id =''
        nombre=''
        user=''
        password=''
        tipo_usuario = ''
        
        # 2. connect database
        DB_NAME='Garage.db'
        conn=sqlite3.connect(DB_NAME)
        cursorEliminar=conn.cursor()
        cursor=conn.cursor()

        deleteQuery=f"DELETE FROM usuarios"
        cursorEliminar.execute(deleteQuery)

        # 4. pase csv data
        for row in csv_file_reader:
            # skip the first row
            for i in range(len(row)):
                # assign each field its value
                id=row[0]
                nombre=row[1]
                user=row[2]
                password=row[3]
                tipo_usuario = row[4]

            InsertQuery=f"INSERT OR IGNORE INTO usuarios VALUES ('{id}','{nombre}','{user}','{password}','{tipo_usuario}')"
            cursor.execute(InsertQuery)

        conn.commit()
        conn.close()

#Actualizar movimientos
def importarMovimientos():
    # read the csv file
    with open('interfaz/exportaciones/csvMovimientos.csv' , 'r') as csvfile:
        # create the object of csv.reader()
        csv_file_reader = csv.reader(csvfile,delimiter=',')
        # skip the header 
        next(csv_file_reader,None)
        # create fileds 
        id =''
        fecha_entrada=''
        fecha_salida=''
        pago=''
        patente_id = ''
        
        # 2. connect database
        DB_NAME='Garage.db'
        conn=sqlite3.connect(DB_NAME)
        cursorEliminar=conn.cursor()
        cursor=conn.cursor()

        deleteQuery=f"DELETE FROM movimientos"
        cursorEliminar.execute(deleteQuery)

        # 4. pase csv data
        for row in csv_file_reader:
            # skip the first row
            for i in range(len(row)):
                # assign each field its value
                id=row[0]
                fecha_entrada=row[1]
                fecha_salida=row[2]
                pago=row[3]
                patente_id = row[4]

            InsertQuery=f"INSERT OR IGNORE INTO movimientos VALUES ('{id}','{fecha_entrada}','{fecha_salida}','{pago}','{patente_id}')"
            cursor.execute(InsertQuery)

        conn.commit()
        conn.close()

def importarCsv():
    importarUsuarios()
    importarMovimientos()
    importarVehiculos()