
# No considera letras con tildes
def desplazar(letra, clave):
    # Desplaza los caracteres a la posicion determinada por la clave. Tanto para encriptar como desencriptar
    # Autor: Julen Gaumard

    ascii_desplazado = ord(letra)
    
    if letra.isnumeric():

        ascii_desplazado += clave%10

        if ascii_desplazado > 57:
            ascii_desplazado -= 10
        elif ascii_desplazado < 48:
            ascii_desplazado += 10

    elif letra.islower():
        
        ascii_desplazado += clave%26

        if ascii_desplazado > 122:
            ascii_desplazado -= 26
        elif ascii_desplazado < 97:
            ascii_desplazado += 26

    elif letra.isupper():

        ascii_desplazado += clave%26
        
        if ascii_desplazado > 90:
            ascii_desplazado -= 26
        elif ascii_desplazado < 65:
            ascii_desplazado += 26

    return chr(ascii_desplazado)

def cifrar_cesar(cadena, clave):
    # Recorre toda la cadena y utilizando la funcion desplazar, encripta o desencripta toda la cadena ingresada.
    # Autor: Julen Gaumard

    cadena_cifrada = ""

    for letra in cadena:
        cadena_cifrada += desplazar(letra, clave)

    return cadena_cifrada

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

import doctest
print(doctest.testmod())