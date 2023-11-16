from usuarios import buscar_usuario
from cifrados import cifrar_atbash, cifrar_cesar
from tkinter import messagebox

def enviar_mensaje(destinatario, remitente, cifrado, clave, mensaje_cifrado):

    if buscar_usuario(destinatario) == destinatario:
    
        with open('mensajes.csv', 'a') as mensajes:
            
            if cifrado == 3:
                cifrado = "C"
                clave = str(clave)

                mensaje = destinatario + "," + remitente + "," + cifrado+clave + "," + mensaje_cifrado + "\n" 
            
            elif cifrado == 4:
                cifrado = "A"
                
                mensaje = destinatario + "," + remitente + "," + cifrado + "," + mensaje_cifrado + "\n" 
        
        mensajes.write(mensaje)

    else:
        messagebox.showerror("Datos incorrentos","El usuario no existe")
