def cifrar_atbash(mensaje):
# ALFABETOS EN MINUSCULA Y MAYUSCULA
    alfabeto_min = "abcdefghijklmnopqrstuvwxyz"
    alfabeto_may = alfabeto_min.upper()
    numeros = "0123456789"

# ALFABETOS INVERTIDOS
    alfabeto_invertido_min = alfabeto_min[::-1]
    alfabeto_invertido_may = alfabeto_may[::-1]
    numeros_invertidos = numeros[::-1]

# MENSAJE CIFRADO
    mensaje_cifrado = ""

# ITERACION PARA CIFRAR EL MENSAJE
    for caracter in mensaje:
    
        if caracter in alfabeto_min:
            mensaje_cifrado += alfabeto_invertido_may[alfabeto_min.index(caracter)]

        elif caracter in alfabeto_may:
            mensaje_cifrado += alfabeto_invertido_min[alfabeto_may.index(caracter)]

        elif caracter in numeros:
            mensaje_cifrado += numeros_invertidos[numeros.index(caracter)]

        else:
            mensaje_cifrado += caracter


    return mensaje_cifrado