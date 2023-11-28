from usuarios import buscar_usuario
from tkinter import messagebox

def enviar_mensaje(destinatario, remitente, cifrado, clave, mensaje_cifrado):
    # Agrega los mensajes al archivo.
    # Autor: Alessandro Perez, Dominguez Lucia Juan Pablo y Julen Gaumard

    existe_destinatario = False

    if destinatario == '*':
        existe_destinatario = True

    else:
        usuario = buscar_usuario(destinatario)

        if not usuario:
            messagebox.showerror("Datos incorrentos","El usuario no existe")
        else:
            existe_destinatario = True


    if existe_destinatario:

        with open('mensajes.csv', 'a') as ar_mensajes:
    
            data_cifrado = cifrado

            if cifrado == "C":
                data_cifrado = cifrado + str(clave)
    
            mensaje = destinatario + "," + remitente + "," + data_cifrado + "," + mensaje_cifrado + "\n" 
            ar_mensajes.write(mensaje)
            messagebox.showinfo("Éxito", "El mensaje se envió correctamente")
