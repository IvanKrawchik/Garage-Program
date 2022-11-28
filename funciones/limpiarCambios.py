import tkinter as tk
from tkinter import *

def limpiarCamposLogin():
    textName.delete(0,"end")
    textPassword.delete(0,"end")

def limpiarCamposRegister():
    textName.delete(0,"end")
    textUserRegister.delete(0,"end")
    textPasswordRegister.delete(0,"end")

def limpiarCampos():
    textPatente.delete(0,"end")
    textMarca.delete(0,"end")
    textModelo.delete(0,"end")
    textColor.delete(0,"end")
    textObservacion.delete(0,"end")
    textEntrada.delete(0,"end")
    textSalida.delete(0,"end")
    textPago.delete(0,"end")

