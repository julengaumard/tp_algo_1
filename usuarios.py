def validacion_user(cadena):
    # Determina la cadena es un nombre de usuario valido.
    # Autor: Julen Gaumard

    largo_cadena = len(cadena)
    lista_especiales = ["_","-","."]

    es_valido = True

    if not (4 < largo_cadena < 16):
        es_valido = False

    cont = 0
    while cont < largo_cadena and es_valido:

        if not (cadena[cont].isnumeric() or cadena[cont].isalpha() or cadena[cont] in lista_especiales):
            es_valido = False

        cont += 1

    return es_valido

def pruebas_validacion_user():
    '''
    >>> validacion_user("megauser")
    True
    >>> validacion_user("me@gauser")
    False
    >>> validacion_user("megausersuperlargo")
    False
    >>> validacion_user("user")
    False
    >>> validacion_user("user122")
    True
    >>> validacion_user("USER99")
    True
    >>> validacion_user("USER_1")
    True
    >>> validacion_user("Pedro-lopez")
    True
    >>> validacion_user("Juan.Miguel")
    True
    >>> validacion_user("Ju4n.Migu3l")
    True
    '''

def validacion_pass(cadena):
    # Determina la cadena es una pass valida.
    # Autor: Julen Gaumard

    largo_cadena = len(cadena)
    lista_especiales = ["_","-","#", "*"]

    largo_valido = True
    tiene_mayuscula = False
    tiene_minuscula = False
    tiene_especiales = False
    tiene_numero = False
    repite_caracter = False

    if not (3 < largo_cadena < 9):
        largo_valido = False

    cont = 0
    while cont < largo_cadena and largo_valido and not repite_caracter:

        if cadena[cont].islower():
            tiene_minuscula = True
            
        elif cadena[cont].isupper():
            tiene_mayuscula = True
        
        elif cadena[cont].isnumeric():
            tiene_numero = True

        elif cadena[cont] in lista_especiales:
            tiene_especiales = True

        if cadena[cont] == cadena[cont - 1] and not cont == 0:
            repite_caracter = True

        cont += 1

    return tiene_numero and tiene_mayuscula and tiene_minuscula and tiene_especiales and not repite_caracter

def pruebas_validacion_pass():
    '''
    >>> validacion_pass("superlargapass")
    False
    >>> validacion_pass("Pablo1#")
    True
    >>> validacion_pass("Pablo1@")
    False
    >>> validacion_pass("pablo1-")
    False
    >>> validacion_pass("pass1")
    False
    >>> validacion_pass("Pabl1#P")
    True
    >>> validacion_pass("Pabl11#")
    False
    >>> validacion_pass("Pa1bl__")
    False
    >>> validacion_pass("--Algo1")
    False
    >>> validacion_pass("-ALGO1")
    False
    '''

def leer_linea(ar):
    linea = ar.readline()

    result = False
    if linea:
        result = linea.rstrip("\n").split(",")

    return result

def obtener_preguntas():

    preguntas = []

    with open("preguntas.csv") as ar_preguntas:

        pregunta = leer_linea(ar_preguntas)

        while pregunta:
            preguntas.append(pregunta[1])
            pregunta = leer_linea(ar_preguntas)

    return preguntas


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())