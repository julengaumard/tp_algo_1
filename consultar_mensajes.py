from usuarios import buscar_usuario
from botones_cifrado import descifrado_atbash, descifrado_cesar
from usuarios import leer_linea
from tkinter import messagebox

def buscar_mensajes():
    # Autor: Alessandro Perez y Dominguez Lucia Juan Pablo
    usuario = buscar_usuario(destinatario)
    
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
                mensaje_privado = remitente + ':' + mensaje_descifrado
                ar_mensaje_privado.write(mensaje_privado)
            
            
            elif usuario == '*':
                mensaje_general = '*'+ remitente + ':' + mensaje_descifrado
                ar_mensaje_general.write(mensaje_general)

            linea_mensajes = leer_linea(ar_mensajes)
                
    ar_mensaje_general.close()
    ar_mensaje_privado.close()
    
