def validacion_usuario(cadena):
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

def pruebas_validacion_usuario():
    '''
    >>> validacion_usuario("megauser")
    True
    >>> validacion_usuario("me@gauser")
    False
    >>> validacion_usuario("megausersuperlargo")
    False
    >>> validacion_usuario("user")
    False
    >>> validacion_usuario("user122")
    True
    >>> validacion_usuario("USER99")
    True
    >>> validacion_usuario("USER_1")
    True
    >>> validacion_usuario("Pedro-lopez")
    True
    >>> validacion_usuario("Juan.Miguel")
    True
    >>> validacion_usuario("Ju4n.Migu3l")
    True
    '''

def validacion_clave(cadena):
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

def pruebas_validacion_clave():
    '''
    >>> validacion_clave("superlargapass")
    False
    >>> validacion_clave("Pablo1#")
    True
    >>> validacion_clave("Pablo1@")
    False
    >>> validacion_clave("pablo1-")
    False
    >>> validacion_clave("pass1")
    False
    >>> validacion_clave("Pabl1#P")
    True
    >>> validacion_clave("Pabl11#")
    False
    >>> validacion_clave("Pa1bl__")
    False
    >>> validacion_clave("--Algo1")
    False
    >>> validacion_clave("-ALGO1")
    False
    '''

def leer_linea(ar):
    # Lee una linea del archivo ingresado
    # Autor: Julen Gaumard

    linea = ar.readline()

    result = False
    if linea:
        result = linea.rstrip("\n").split(",")

    return result

def obtener_preguntas():
    # Obtiene la lista de preguntas del archivo
    # Autor: Julen Gaumard

    preguntas = []

    with open("preguntas.csv") as ar_preguntas:

        pregunta = leer_linea(ar_preguntas)

        while pregunta:
            preguntas.append(pregunta[1])
            pregunta = leer_linea(ar_preguntas)

    return preguntas

def obtener_indice_preguntas(opcion):
    # Obtiene el indice que corresponde para la pregunta seleccionada
    # Autor: Julen Gaumard

    valor = -1

    with open("preguntas.csv") as ar_preguntas:

        pregunta = leer_linea(ar_preguntas)

        while pregunta and valor == -1:
            
            if pregunta[1] == opcion:
                valor = pregunta[0]

            pregunta = leer_linea(ar_preguntas)

    return valor

def buscar_usuario(nombre_usuario):
    # Busca si existe el usuario en el archivo de usuarios
    # Autor: Julen Gaumard

    coincidencia = False

    try:
        with open("usuarios.csv") as ar_usuario:
            
            usuario = leer_linea(ar_usuario)

            while usuario:

                if nombre_usuario == usuario[0]:
                    coincidencia = usuario

                usuario = leer_linea(ar_usuario)
    except:
        pass

    return coincidencia

def agregar_usuario(nombre_usuario, clave, opcion, respuesta):
    # Agrega un usuario al archivo
    # Autor: Julen Gaumard

    with open("usuarios.csv", "a") as ar_usuarios:
         
        # preguntas = obtener_preguntas()
        # indice_pregunta = preguntas.index(opcion)
        indice_pregunta = obtener_indice_preguntas(opcion)

        usuario = nombre_usuario + "," + clave + "," + str(indice_pregunta) + "," + respuesta + "," + "0" "\n"

        ar_usuarios.write(usuario)

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())