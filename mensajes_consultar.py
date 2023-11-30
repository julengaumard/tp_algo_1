from usuarios import buscar_usuario
from botones_cifrado import descifrado_atbash, descifrado_cesar
from usuarios import leer_linea
from tkinter import messagebox
import os

def armar_archivo_mensajes_recibidos(archivo,archivo_nuevo):
    # Añade al archivo_nuevo las lineas del archivo, reescritas de forma distinta
    # Autor: Dominguez Lucia Juan Pablo

    linea_mensajes = leer_linea(archivo)

    while linea_mensajes:
        
        remitente, mensaje_descifrado = linea_mensajes
        mensaje = remitente + ',' + mensaje_descifrado + "\n"
        
        archivo_nuevo.write(mensaje)
        
        linea_mensajes = leer_linea(archivo)

    archivo.close()


def buscar_mensajes(usuario):
    # busca en el archivo mensajes.csv solo los mensajes para el destinatario o los generales y los separa en dos archivos
    # Autor: Alessandro Perez y Dominguez Lucia Juan Pablo
    
    with open("mensajes.csv") as ar_mensajes:
        
        ar_mensaje_general = open("mensajes_general.csv", 'w')
        ar_mensaje_privado = open("mensajes_privado.csv", 'w')

        linea_mensajes = leer_linea(ar_mensajes)
        
        while linea_mensajes:
        
            destinatario, remitente, cifrado, mensaje_cifrado = linea_mensajes
            existe_destinatario = False

            if usuario == destinatario or destinatario == "*":
                existe_destinatario = True
            
            if existe_destinatario:

                if cifrado == 'A':
                    mensaje_descifrado = descifrado_atbash(mensaje_cifrado)
                
                else:
                    clave = int(cifrado.replace("C",""))
                    mensaje_descifrado = descifrado_cesar(mensaje_cifrado, clave)
                    
                mensaje_privado = remitente + ',' + mensaje_descifrado + "\n"

                if destinatario == "*":
                    mensaje_general = "*" + mensaje_privado

                    ar_mensaje_general.write(mensaje_general)
                else:
                    ar_mensaje_privado.write(mensaje_privado)

            linea_mensajes = leer_linea(ar_mensajes)
            
    ar_mensaje_general.close()
    ar_mensaje_privado.close()

def juntar_mensajes():
    # junta los dos archivos previamente creados en uno solo
    # Autor: Alessandro Perez y Dominguez Lucia Juan Pablo
    
    ar_mensaje_general = open("mensajes_general.csv")
    ar_mensaje_privado = open("mensajes_privado.csv")
    ar_mensajes_totales = open("mensajes_recibidos.csv", 'w')
    
    armar_archivo_mensajes_recibidos(ar_mensaje_general,ar_mensajes_totales)
    armar_archivo_mensajes_recibidos(ar_mensaje_privado,ar_mensajes_totales)

    os.remove("mensajes_general.csv")
    os.remove("mensajes_privado.csv")

    ar_mensajes_totales.close()

def armar_archivo_mensajes(usuario_ingresado):
    buscar_mensajes(usuario_ingresado)
    juntar_mensajes()

