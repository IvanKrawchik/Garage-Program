import tkinter as tk
from tkinter import *

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

    login=tk.Button(raiz, text="Login")

    user.place(x=30, y=40)
    textUser.place(x=120,y=40)
    password.place(x=30, y=80)
    textPassword.place(x=120,y=80)
    login.place(x=125,y=150)

    create_user=tk.Button(raiz, text="No tenes cuenta? Registrate",command=register)
    create_user.place(x=75,y=120)

    raiz.mainloop()

def register():
    registerWindow=Toplevel()
    registerWindow.geometry('300x200')
    registerWindow.resizable(0,0)
    registerWindow.title('Nuevo Usuario')
    registerWindow.configure(bg='grey')

    nameRegister = tk.Label(registerWindow, text="Nombre:")
    textName=tk.Entry(registerWindow,border=4)

    userRegister = tk.Label(registerWindow, text="Usuario:")
    textUserRegister=tk.Entry(registerWindow,border=4)

    passwordRegister = tk.Label(registerWindow, text="Contraseña:")
    textPasswordRegister=tk.Entry(registerWindow,border=4)

    loginRegister=tk.Button(registerWindow, text="Crear usuario")

    nameRegister.place(x=30, y=40)
    textName.place(x=120,y=40)
    userRegister.place(x=30, y=70)
    textUserRegister.place(x=120,y=70)
    passwordRegister.place(x=30, y=100)
    textPasswordRegister.place(x=120,y=100)
    loginRegister.place(x=115,y=150)

login()