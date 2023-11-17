from usuarios import buscar_usuario
from botones_cifrado import descifrado_atbash, descifrado_cesar
from usuarios import leer_linea
from tkinter import messagebox

def listar_mensaje():
    # Autor: Alessandro Perez y Dominguez Lucia Juan Pablo
    usuario = buscar_usuario(destinatario)
    
    with open("mensajes.csv") as ar_mensajes:
        
        ar_mensaje_general = open("mensajes_general.csv", 'w')
        ar_mensaje_privados = open("mensajes_privado.csv", 'w')
        
        while linea_mensajes:
        
            linea_mensajes = leer_linea(ar_mensajes)
        
            destinatario, remitente, cifrado, mensaje_cifrado = linea_mensajes
        
            if cifrado == 'A':
                mensaje_descifrado = descifrado_atbash(mensaje_cifrado)
                
            else:
                clave = cifrado[1]
                mensaje_descifrado = descifrado_cesar(mensaje_cifrado, clave)
            
            mensaje_general = '*'+ remitente + ':' + mensaje_descifrado
            mensaje_privado = remitente + ':' + mensaje_descifrado
            
            
            if usuario == destinatario:
                
            
            
            elif usuario == '*':
                
            
            linea = leer_linea(ar_mensajes)

    ar_mensaje_general.close()
    ar_mensaje_privados.close()
    