# FUNCION PARA CIFRAR EL MENSAJE
def cifrar_atbash(mensaje):
# ALFABETOS EN MINUSCULA Y MAYUSCULA
    alfabeto_min = "abcdefghijklmnopqrstuvwxyz"

    alfabeto_may = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# ALFABETOS INVERTIDOS
    alfabeto_invertido_min = alfabeto_min[::-1]

    alfabeto_invertido_may = alfabeto_may[::-1]

# MENSAJE CIFRADO
    mensaje_cifrado = ""

# ITERACION PARA CIFRAR EL MENSAJE
    for letra in mensaje:
    
        if letra in alfabeto_min:
        
            mensaje_cifrado += alfabeto_invertido_may[alfabeto_min.index(letra)]

        elif letra in alfabeto_may:
        
            mensaje_cifrado += alfabeto_invertido_min[alfabeto_may.index(letra)]
        
        else:

            mensaje_cifrado += letra


    return mensaje_cifrado