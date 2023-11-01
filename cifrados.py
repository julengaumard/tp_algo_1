def control_limite(ascii_desplazado, clave, cantidad, limite_menor, limite_mayor):

    ascii_desplazado += clave % cantidad

    if ascii_desplazado > limite_mayor:
        ascii_desplazado -= cantidad
    elif ascii_desplazado < limite_menor:
        ascii_desplazado += cantidad

    return ascii_desplazado

# No considera letras con tildes
def desplazar(letra, clave):
    # Desplaza los caracteres a la posicion determinada por la clave. Tanto para encriptar como desencriptar
    # Autor: Julen Gaumard

    ascii_desplazado = ord(letra)
    
    if letra.isnumeric():

        ascii_desplazado = control_limite(ascii_desplazado, clave, 10, 48, 57)

    elif letra.islower():
        
        ascii_desplazado = control_limite(ascii_desplazado, clave, 26, 97, 122)
       
    elif letra.isupper():

        ascii_desplazado = control_limite(ascii_desplazado, clave, 26, 65, 90)
    
    return chr(ascii_desplazado)

def cifrar_cesar(cadena, clave):
    # Recorre toda la cadena y utilizando la funcion desplazar, encripta o desencripta toda la cadena ingresada.
    # Autor: Julen Gaumard

    cadena_cifrada = ""

    for letra in cadena:
        cadena_cifrada += desplazar(letra, clave)

    return cadena_cifrada

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
