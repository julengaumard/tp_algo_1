from cifrados import cifrar_atbash, cifrar_cesar
from tkinter import messagebox

def buscar_error_atbash(texto,configuracion): 
    # Autor: Dominguez Lucia Juan Pablo
    error = False
    if texto == "":
        messagebox.showerror(configuracion['errores_cifrado']['datos_incompletos'],configuracion['errores_cifrado']['error_texto'])
        error = True

    return error

def buscar_error_cesar(texto,clave,configuracion): 
    # Autor: Dominguez Lucia Juan Pablo
    error = False
    if texto == "" and clave == "":
        messagebox.showerror(configuracion['errores_cifrado']['datos_incompletos'],configuracion['errores_cifrado']['error_texto_clave'])
        error = True
    elif texto == "" and clave != "":
        messagebox.showerror(configuracion['errores_cifrado']['datos_incompletos'],configuracion['errores_cifrado']['error_texto'])
        error = True
    elif texto != "" and clave == "":
        messagebox.showerror(configuracion['errores_cifrado']['datos_incompletos'],configuracion['errores_cifrado']['error_clave'][0])
        error = True
    elif not clave.isnumeric():
        messagebox.showerror(configuracion['errores_cifrado']['datos_incorrectos'],configuracion['errores_cifrado']['error_clave'][1])
        error = True
    return error

def boton_atbash(texto,resultado,configuracion):
    # Autor: Dominguez Lucia Juan Pablo
    error = buscar_error_atbash(texto,configuracion)
    if error == False:
        cifrar = cifrar_atbash(texto)

        resultado.set(cifrar)

def boton_cesar(texto,clave,resultado,boton,configuracion):
    # Autor: Dominguez Lucia Juan Pablo

    error = buscar_error_cesar(texto,clave,configuracion)
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
