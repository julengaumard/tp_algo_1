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


# def enviar_mensaje(destinatario, remitente, cifrado, clave, mensaje_cifrado):
#     # Agrega los mensajes al archivo.
#     # Autor: Alessandro Perez y Dominguez Lucia Juan Pablo

#     if destinatario == '*':
#         with open('mensajes.csv', 'a') as ar_mensajes:
                    
#             if cifrado == 3:
#                 cifrado = "C"
#                 clave = str(clave)

#                 mensaje = destinatario + "," + remitente + "," + cifrado+clave + "," + mensaje_cifrado + "\n" 
#                 messagebox.showinfo("Éxito", "El mensaje se envió correctamente")
                
                    
#             elif cifrado == 4:
#                 cifrado = "A"
                        
#                 mensaje = destinatario + "," + remitente + "," + cifrado + "," + mensaje_cifrado + "\n" 
#                 messagebox.showinfo("Éxito", "El mensaje se envió correctamente")
        
#             ar_mensajes.write(mensaje)

#     else:
#         usuario = buscar_usuario(destinatario)

#         if not usuario:
#             messagebox.showerror("Datos incorrentos","El usuario no existe")

#         else:
#             with open('mensajes.csv', 'a') as ar_mensajes:
                    
#                 if cifrado == 3:
#                     cifrado = "C"
#                     clave = str(clave)

#                     mensaje = destinatario + "," + remitente + "," + cifrado+clave + "," + mensaje_cifrado + "\n" 
#                     messagebox.showinfo("Éxito", "El mensaje se envió correctamente")
                
                    
#                 elif cifrado == 4:
#                     cifrado = "A"
                        
#                     mensaje = destinatario + "," + remitente + "," + cifrado + "," + mensaje_cifrado + "\n" 
#                     messagebox.showinfo("Éxito", "El mensaje se envió correctamente")
                
#                 ar_mensajes.write(mensaje)

