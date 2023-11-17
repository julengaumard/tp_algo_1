from cifrados import cifrar_atbash, cifrar_cesar
from tkinter import messagebox

def buscar_error_atbash(texto): 
    # Autor: Dominguez Lucia Juan Pablo
    error = False
    if texto == "":
        messagebox.showerror("Datos incompletos","Debes ingresar un texto y una clave")
        error = True

    return error

def buscar_error_cesar(texto,clave): 
    # Autor: Dominguez Lucia Juan Pablo
    error = False
    if texto == "" and clave == "":
        messagebox.showerror("Datos incompletos","Debes ingresar un texto y una clave")
        error = True
    elif texto == "" and clave != "":
        messagebox.showerror("Datos incompletos","Debes ingresar un texto")
        error = True
    elif texto != "" and clave == "":
        messagebox.showerror("Datos incompletos","Debes ingresar una clave")
        error = True
    elif not clave.isnumeric():
        messagebox.showerror("Datos incorrectos","la clave debe ser numerica")
        error = True
    return error

def boton_atbash(texto,resultado):
    # Autor: Dominguez Lucia Juan Pablo
    error = buscar_error_atbash(texto)
    if error == False:
        cifrar = cifrar_atbash(texto)

        resultado.set(cifrar)

def boton_cesar(texto,clave,resultado,boton):
    # Autor: Dominguez Lucia Juan Pablo

    error = buscar_error_cesar(texto,clave)
    if error == False:
        if boton == 1:
            cifrar = cifrar_cesar(texto,int(clave))

            resultado.set(cifrar)

        elif boton == 2:
            negativo = -int(clave)
            cifrar = cifrar_cesar(texto,negativo)

            resultado.set(cifrar)

# FUNCIONES PARA EL APARTADO DE MENSAJES.CSV 

def descifrado_atbash(mensaje):
    # Autor: Alessandro Perez y Dominguez Lucia Juan Pablo
    
    cifrar = cifrar_atbash(mensaje)
    
    return cifrar

def descifrado_cesar(mensaje, clave):
    
    # Autor: Alessandro Perez y Dominguez Lucia Juan Pablo

    negativo = -int(clave)
    cifrar = cifrar_cesar(mensaje,negativo)
    
    return cifrar
