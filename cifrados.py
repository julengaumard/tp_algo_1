def control_limite(caracter_desplazado, clave, cantidad_caracteres, limite_menor):

    caracter_desplazado += clave % cantidad_caracteres

    if caracter_desplazado > limite_menor + cantidad_caracteres - 1:
        caracter_desplazado -= cantidad_caracteres
    elif caracter_desplazado < limite_menor:
        caracter_desplazado += cantidad_caracteres

    return caracter_desplazado

# No considera letras con tildes
def desplazar(letra, clave):
    # Desplaza los caracteres a la posicion determinada por la clave. Tanto para encriptar como desencriptar
    # Autor: Julen Gaumard

    LISTA_DESPLAZAR = [['a','z'], ['A','Z'], ['0','9']]

    caracter_desplazado = ord(letra)
    
    cont = 0
    while cont < len(LISTA_DESPLAZAR):

        caracter_inicial = ord(LISTA_DESPLAZAR[cont][0])
        caracter_final = ord(LISTA_DESPLAZAR[cont][1])
        cantidad_caracteres = caracter_final - caracter_inicial + 1

        if  caracter_inicial <= caracter_desplazado <= caracter_final: 
            
            caracter_desplazado = control_limite(caracter_desplazado, clave, cantidad_caracteres, caracter_inicial)
            cont = len(LISTA_DESPLAZAR)

        cont += 1

    return chr(caracter_desplazado)

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