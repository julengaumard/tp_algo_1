from usuarios import buscar_usuario
from tkinter import messagebox

def enviar_mensaje(destinatario, remitente, cifrado, clave, mensaje_cifrado):

    # Autor: Alessandro Perez y Dominguez Lucia Juan Pablo

    if destinatario == '*':
        with open('mensajes.csv', 'a') as ar_mensajes:
                    
            if cifrado == 3:
                cifrado = "C"
                clave = str(clave)

                mensaje = destinatario + "," + remitente + "," + cifrado+clave + "," + mensaje_cifrado + "\n" 
                messagebox.showinfo("Éxito", "El mensaje se envió correctamente")
                
                    
            elif cifrado == 4:
                cifrado = "A"
                        
                mensaje = destinatario + "," + remitente + "," + cifrado + "," + mensaje_cifrado + "\n" 
                messagebox.showinfo("Éxito", "El mensaje se envió correctamente")
        
            ar_mensajes.write(mensaje)

    else:
        usuario = buscar_usuario(destinatario)

        if not usuario:
            messagebox.showerror("Datos incorrentos","El usuario no existe")

        else:
            with open('mensajes.csv', 'a') as ar_mensajes:
                    
                if cifrado == 3:
                    cifrado = "C"
                    clave = str(clave)

                    mensaje = destinatario + "," + remitente + "," + cifrado+clave + "," + mensaje_cifrado + "\n" 
                    messagebox.showinfo("Éxito", "El mensaje se envió correctamente")
                
                    
                elif cifrado == 4:
                    cifrado = "A"
                        
                    mensaje = destinatario + "," + remitente + "," + cifrado + "," + mensaje_cifrado + "\n" 
                    messagebox.showinfo("Éxito", "El mensaje se envió correctamente")
                
                ar_mensajes.write(mensaje)

