from usuarios import buscar_usuario
from tkinter import messagebox

def enviar_mensaje(destinatario, remitente, cifrado, clave, mensaje_cifrado,configuracion):
    # Agrega los mensajes al archivo.
    # Autor: Alessandro Perez, Dominguez Lucia Juan Pablo y Julen Gaumard

    existe_destinatario = False

    if destinatario == '*':
        existe_destinatario = True

    else:
        usuario = buscar_usuario(destinatario)

        if not usuario:
            messagebox.showerror(configuracion['errores_manejo_usuarios']['usuario_titulo'],configuracion['errores_manejo_usuarios']['usuario_texto'])
        else:
            existe_destinatario = True


    if existe_destinatario:

        with open('mensajes.csv', 'a') as ar_mensajes:
    
            data_cifrado = cifrado

            if cifrado == "C":
                data_cifrado = cifrado + str(clave)
    
            mensaje = destinatario + "," + remitente + "," + data_cifrado + "," + mensaje_cifrado + "\n" 
            ar_mensajes.write(mensaje)
            messagebox.showinfo(configuracion['exitoso']['exito'],configuracion['exitoso']['mensaje_enviado'])


def es_usuario_valido(destinatario, configuracion):
    # Chequea que el usuario sea valido para enviar un mensaje
    # Autor: Alessandro Perez, Dominguez Lucia Juan Pablo y Julen Gaumard

    existe_destinatario = False

    if destinatario == '*':
        existe_destinatario = True

    else:
        usuario = buscar_usuario(destinatario)

        if not usuario:
            messagebox.showerror(configuracion['errores_manejo_usuarios']['usuario_titulo'],configuracion['errores_manejo_usuarios']['usuario_texto'])
        else:
            existe_destinatario = True

    return existe_destinatario