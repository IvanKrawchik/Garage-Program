import sqlite3
import tkinter as tk

def register():
    registerWindow=tk.Tk()
    registerWindow.geometry('300x200')
    registerWindow.resizable(0,0)
    registerWindow.title('Nuevo Usuario')
    registerWindow.configure(bg='grey')

    nameRegister = tk.Label(registerWindow, text="Nombre:")
    textName=tk.Entry(registerWindow,border=4)

    userRegister = tk.Label(registerWindow, text="Usuario:")
    textUserRegister=tk.Entry(registerWindow,border=4)

    passwordRegister = tk.Label(registerWindow, text="Contraseña:")
    textPasswordRegister=tk.Entry(registerWindow,border=4,show="*")

    def crearUsuario():
        DB_NAME='Garage.db'
        conn=sqlite3.connect(DB_NAME)
        Cursor=conn.cursor()
        print((textName.get(),textUserRegister.get(),textPasswordRegister.get(),"user"))

        #TODO Siguientes 2 lineas generan error
        Cursor.execute("INSERT INTO usuarios (nombre,user,password,tipo_usuario) VALUES (?,?,?,?)",(textName.get(),textUserRegister.get(),textPasswordRegister.get(),"user"))
        # conn.commit()
        print("Usuario creado correctamente")
    
    loginRegister=tk.Button(registerWindow, text="Crear usuario",command=crearUsuario)

    nameRegister.place(x=30, y=40)
    textName.place(x=120,y=40)
    userRegister.place(x=30, y=70)
    textUserRegister.place(x=120,y=70)
    passwordRegister.place(x=30, y=100)
    textPasswordRegister.place(x=120,y=100)
    loginRegister.place(x=115,y=150)
