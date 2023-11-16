from usuarios import buscar_usuario
from cifrados import cifrar_atbash, cifrar_cesar

def enviar_mensaje(destinatario, remitente, cifrado, clave, mensaje_cifrado):

    if buscar_usuario(destinatario) == destinatario:
    
        with open('mensajes.csv', 'a') as mensajes:
            
            if cifrar_cesar(cifrado) == cifrado:
            
                mensaje = destinatario + "," + remitente + "," + cifrado+clave + "," + mensaje_cifrado + "\n" 
            
            elif cifrar_atbash(cifrado) == cifrado:
                
                mensaje = destinatario + "," + remitente + "," + cifrado + "," + mensaje_cifrado + "\n" 
        
        mensajes.write(mensaje)

