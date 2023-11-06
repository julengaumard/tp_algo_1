def control_limite(ascii_desplazado, clave, cantidad, limite_menor):

    ascii_desplazado += clave % cantidad

    if ascii_desplazado > limite_menor + cantidad - 1:
        ascii_desplazado -= cantidad
    elif ascii_desplazado < limite_menor:
        ascii_desplazado += cantidad

    return ascii_desplazado

# No considera letras con tildes
def desplazar(letra, clave):
    # Desplaza los caracteres a la posicion determinada por la clave. Tanto para encriptar como desencriptar
    # Autor: Julen Gaumard

    LISTA_DESPLAZAR = [['a',26], ['A',26], ['0',10]]

    ascii_desplazado = ord(letra)
    
    cont = 0
    while cont < len(LISTA_DESPLAZAR):

        ascii_inicial = ord(LISTA_DESPLAZAR[cont][0])
        cantidad_ascii = LISTA_DESPLAZAR[cont][1]

        if  ascii_inicial <= ascii_desplazado < ascii_inicial + cantidad_ascii: 
            
            ascii_desplazado = control_limite(ascii_desplazado, clave, cantidad_ascii, ascii_inicial)
            cont = len(LISTA_DESPLAZAR)

        cont += 1

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

def pruebas_cifrar_cesar():
    '''
    >>> cifrar_cesar("HOLA mundo",3)
    'KROD pxqgr'
    >>> cifrar_cesar("KROD pxqgr",-3)
    'HOLA mundo'
    >>> cifrar_cesar("$ 195",3)
    '$ 428'
    >>> cifrar_cesar("# 129",-3)
    '# 896'
    >>> cifrar_cesar("HOLA mundo #2", 81)
    'KROD pxqgr #3'
    >>> cifrar_cesar("333",-23)
    '000'
    >>> cifrar_cesar("!000",-5)
    '!555'
    >>> cifrar_cesar("aaZZ",-1)
    'zzYY'
    >>> cifrar_cesar("numero1",10)
    'xewoby1'
    >>> cifrar_cesar("xewoby1",-10)
    'numero1'
    '''

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())