
# NO considera letras con tildes
def desplazar(letra, clave):

    ascii_desplazado = ord(letra) + clave
    
    if letra.isnumeric():

        while ascii_desplazado > 57:
            ascii_desplazado -= 10

    elif letra.islower():
        
        while ascii_desplazado > 122:
            ascii_desplazado -= 26

    elif letra.isupper():
        
        while ascii_desplazado > 90:
            ascii_desplazado -= 26

    else:
        ascii_desplazado = ord(letra)

    caracter_desplazado = chr(ascii_desplazado)
    return caracter_desplazado

def cifrar_cesar(cadena, clave):

    cadena_cifrada = ""

    for letra in cadena:
        cadena_cifrada += desplazar(letra, clave)

    return cadena_cifrada