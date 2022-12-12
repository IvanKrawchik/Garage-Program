import tkinter as tk
from tkinter import *
from tkinter import messagebox
import sqlite3
from interfaz.registrar import register
from interfaz.mainPageAdmin import mainPageAdmin
from interfaz.mainPageUser import mainPageUser


def login():
    raiz = tk.Tk()
    raiz.geometry('300x200')
    raiz.resizable(0,0)
    raiz.title('Login')
    raiz.configure(bg='grey')

    user = tk.Label(raiz, text="Usuario:")
    textUser=tk.Entry(raiz,border=4)

    password = tk.Label(raiz, text="Contraseña:")
    textPassword=tk.Entry(raiz,border=4,show="*")

    create_user=tk.Button(raiz, text="No tenes cuenta? Registrate",command=register)

    user.place(x=30, y=40)
    textUser.place(x=120,y=40)
    password.place(x=30, y=80)
    textPassword.place(x=120,y=80)
    create_user.place(x=75,y=120)

    #Limpia campos al loguearse correctamente
    def limpiarCamposLogin():
        textUser.delete(0,"end")
        textPassword.delete(0,"end")

    def validarUsuario():
        DB_NAME='Garage.db'
        conn=sqlite3.connect(DB_NAME)
        cursorValidar=conn.cursor()
        cursorValidar.execute("SELECT tipo_usuario FROM usuarios WHERE user=? AND password=?",(textUser.get(),textPassword.get()))
        resultado=(cursorValidar.fetchone())
        if resultado:
            # Al loguearse corectamente se corre mainPage y se cierra el login
            tipoDeUsuario=resultado[0].upper()
            if (tipoDeUsuario=='ADMIN'):
                tk.messagebox.showinfo(title='Login', message="Logueado correctamente como Admin")
                raiz.destroy()
                mainPageAdmin()
            else:
                tk.messagebox.showinfo(title='Login', message="Logueado correctamente como User")
                raiz.destroy()
                mainPageUser()
        else:
            tk.messagebox.showerror(title='Login', message="Usuario/contraseña incorrectos")
            limpiarCamposLogin()

    login=tk.Button(raiz, text="Login",command=validarUsuario)
    login.place(x=125,y=150)

    raiz.mainloop()

if __name__ == '__main__':
    login()