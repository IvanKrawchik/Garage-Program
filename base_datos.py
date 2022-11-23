import sqlite3

DB_NAME='Garage.db'

def init_db():
    conn=sqlite3.connect(DB_NAME)
    conn.execute('''CREATE TABLE IF NOT EXISTS movil
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                        patente TEXT,
                        marca TEXT,
                        modelo TEXT,
                        color TEXT,
                        observaciones TEXT)''')
    conn.execute('''CREATE TABLE IF NOT EXISTS usuarios
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre TEXT,
                        user TEXT,
                        password TEXT,
                        tipo_usuario TEXT)''')
    conn.execute('''CREATE TABLE IF NOT EXISTS movimientos
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                        fecha_entrada DATETIME,
                        fecha_salida DATETIME
                        lugar TEXT,
                        patente_id TEXT,
                        FOREIGN KEY(patente_id) REFERENCES movil(patente))''')

    conn=sqlite3.connect(DB_NAME)
    usuario_admin="Admin"
    qry_admin=f"""
                INSERT INTO usuarios
                    (id,
                    nombre,
                    user,
                    password,
                    tipo_usuario)
                VALUES(
                    '1',
                    '{usuario_admin}',
                    '{usuario_admin}',
                    '{usuario_admin}',
                    '{usuario_admin}')"""
    conn.execute(qry_admin)
    conn.commit()
    conn.close()