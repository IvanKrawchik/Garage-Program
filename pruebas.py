from tkinter import *
from tkinter import messagebox
import sqlite3

ventana = Tk()
ventana.title ("------- Login Python Diario -------")
ventana.geometry ("350x150+500+250")
Label(ventana, text = "Usuario:").pack()
caja1 = Entry(ventana)
caja1.pack()

Label(ventana, text = "Contraseña:").pack()
caja2 = Entry(ventana, show = "*")
caja2.pack()

def login():
 # Connect to database
 DB_NAME='Garage.db'
 db = sqlite3.connect(DB_NAME)
 c = db.cursor()
 
 usuario = caja1.get()
 contr = caja2.get()
 
 c.execute('SELECT * FROM usuarios WHERE usuario = ? AND pass = ?', (usuario, contr))
 
 if c.fetchall():
  messagebox.showinfo(title = "Login correcto", message = "Usuario y contraseña correctos")
 else:
  messagebox.showerror(title = "Login incorrecto", message = "Usuario o contraseña incorrecta")
  
 c.close()

Button (text = "Login", command = login).pack()


ventana.mainloop()