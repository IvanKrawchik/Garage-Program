import tkinter as tk
from tkinter import *
import sqlite3
import registrar

def login():
    raiz = tk.Tk()
    raiz.geometry('300x200')
    raiz.resizable(0,0)
    raiz.title('Login')
    raiz.configure(bg='grey')


    user = tk.Label(raiz, text="Usuario:")
    textUser=tk.Entry(raiz,border=4)

    password = tk.Label(raiz, text="Contraseña:")
    textPassword=tk.Entry(raiz,border=4)

    def validarUsuario():
        DB_NAME='Garage.db'
        conn=sqlite3.connect(DB_NAME)
        cursorValidar=conn.cursor()

        cursorValidar.execute("SELECT * FROM usuarios WHERE user=? AND password=?",(textUser.get(),textPassword.get()))
        if cursorValidar.fetchone():
            print("Logueado correctamente")
            print(textUser.get(),textPassword.get())
        else:
            print("Usuario/contraseña incorrectos")
            print(textUser.get(),textPassword.get())
        cursorValidar.close()

    login=tk.Button(raiz, text="Login",command=validarUsuario)

    user.place(x=30, y=40)
    textUser.place(x=120,y=40)
    password.place(x=30, y=80)
    textPassword.place(x=120,y=80)
    login.place(x=125,y=150)

    create_user=tk.Button(raiz, text="No tenes cuenta? Registrate",command=registrar.register)
    create_user.place(x=75,y=120)

    raiz.mainloop()

login()