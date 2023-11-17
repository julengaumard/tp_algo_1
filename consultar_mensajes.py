from usuarios import buscar_usuario
from botones_cifrado import descifrado_atbash, descifrado_cesar
from usuarios import leer_linea
from tkinter import messagebox

def buscar_mensajes(usuario):
    # Autor: Alessandro Perez y Dominguez Lucia Juan Pablo
    
    with open("mensajes.csv") as ar_mensajes:
        
        ar_mensaje_general = open("mensajes_general.csv", 'w')
        ar_mensaje_privado = open("mensajes_privado.csv", 'w')

        linea_mensajes = leer_linea(ar_mensajes)
        
        while linea_mensajes:
        
            destinatario, remitente, cifrado, mensaje_cifrado = linea_mensajes
        
            if cifrado == 'A':
                mensaje_descifrado = descifrado_atbash(mensaje_cifrado)
                
            else:
                clave = cifrado[1]
                mensaje_descifrado = descifrado_cesar(mensaje_cifrado, clave)
            
            
            if usuario == destinatario:
                mensaje_privado = remitente + ',' + ':' + ','+ mensaje_descifrado
                ar_mensaje_privado.write(mensaje_privado)
            
            
            elif usuario == '*':
                mensaje_general = '*' + remitente + ',' + ':' + ','+ mensaje_descifrado
                ar_mensaje_general.write(mensaje_general)

            linea_mensajes = leer_linea(ar_mensajes)
            
    ar_mensaje_general.close()
    ar_mensaje_privado.close()

def juntar_mensajes():
    # Autor: Alessandro Perez
    
    ar_mensaje_general = open("mensajes_general.csv")
    ar_mensaje_privado = open("mensajes_privado.csv")
    ar_mensajes_totales = open("mensajes_totales", 'w')
    
    linea_mensajes_general = leer_linea(ar_mensaje_general)
    linea_mensaje_privado = leer_linea(ar_mensaje_privado)
    
    while linea_mensajes_general:
        
        remitente, separador, mensaje_descifrado = linea_mensajes_general
        mensaje_general = '*' + remitente + ',' + ':' + ','+ mensaje_descifrado
        
        ar_mensajes_totales.write(mensaje_general)
        
        linea_mensajes_general = leer_linea(ar_mensaje_general)
    
    while linea_mensaje_privado:
        
        remitente, separador, mensaje_descifrado = linea_mensajes_general
        mensaje_privado = remitente + ',' + ':' + ','+ mensaje_descifrado
        
        ar_mensajes_totales.write(mensaje_privado)
        
        linea_mensaje_privado = leer_linea(ar_mensaje_privado)
    
    ar_mensaje_general.close()
    ar_mensaje_privado.close()
    ar_mensajes_totales.close()

def leer_mensajes(usuario_ingresado):
    buscar_mensajes(usuario_ingresado)
    juntar_mensajes()
