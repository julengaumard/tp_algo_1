from tkinter import messagebox
import os

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

            while usuario and not coincidencia:

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

        usuario = nombre_usuario + "," + clave + "," + str(indice_pregunta) + "," + respuesta + "," + "0" + "\n"

        ar_usuarios.write(usuario)

def crear_nuevo_archivo_usuario(usuario_ingresado,tipo_intento):
    # Crea un nuevo archivo usuarios.csv dependiendo de si el intento de recuperacion fue un existo o si fue fallido
    # Autor: Dominguez lucia Juan Pablo

    ar_usuarios = open("usuarios.csv","r")
    ar_intentos = open("usuario_actualizado","w")

    linea = leer_linea(ar_usuarios)

    usuario,clave,pregunta,respuesta,intento = linea

    while linea:

        if usuario_ingresado == usuario:

            if tipo_intento == "intento_fallido":
                intento= str(int(intento) + 1)
            elif tipo_intento == "intento_exitoso":
                intento = str(0)

        nueva_linea = usuario + "," + clave + "," + pregunta + "," + respuesta + "," + intento + "\n"
        ar_intentos.write(nueva_linea)

        linea = leer_linea(ar_usuarios)

        if linea:
            usuario,clave,pregunta,respuesta,intento = linea


    ar_usuarios.close()
    os.remove("usuarios.csv")

    ar_intentos.close()
    os.rename("usuario_actualizado","usuarios.csv")


def olvide_contraseña(usuario_ingresado,pregunta_ingresada,respuesta_ingresada,configuracion):
    # Verifica que la respuesta ingresada sea la correcta para devolver la contraseña, de no ser asi, agrega un intento fallido al usuario.
    # Autor: Dominguez lucia Juan Pablo
    
    pregunta_ingresada = obtener_indice_preguntas(pregunta_ingresada)

    if usuario_ingresado and respuesta_ingresada:
        ar_usuarios = open("usuarios.csv","r")
        linea = leer_linea(ar_usuarios)
        usuario_encontrado = False
        intentos_fallidos = False
        bloqueado = False

        while linea and not usuario_encontrado:

            usuario,clave,pregunta,respuesta,intentos = linea

            if usuario == usuario_ingresado:
                usuario_encontrado = True
                intentos = int(intentos)

                if intentos >= 3:
                    bloqueado = True

                elif respuesta == respuesta_ingresada and pregunta == pregunta_ingresada:
                    messagebox.showinfo(configuracion['exitoso']['respuesta_correcta'],configuracion['exitoso']['recuperacion_exitosa'] + clave)

                else:
                    intentos_fallidos = True
                    messagebox.showerror(configuracion['errores_manejo_usuarios']['respuesta_incorrecta'],configuracion['errores_manejo_usuarios']['recuperacion_fallida'])

            linea = leer_linea (ar_usuarios)
        
        ar_usuarios.close()

        if intentos_fallidos:
            crear_nuevo_archivo_usuario(usuario_ingresado,"intento_fallido")
        elif bloqueado:
            messagebox.showerror(configuracion['errores_manejo_usuarios']['bloqueado_titulo'],configuracion['errores_manejo_usuarios']['bloqueado_texto'])
        else:
            crear_nuevo_archivo_usuario(usuario_ingresado,"intento_exitoso")
    
    elif not usuario_ingresado:
        messagebox.showerror(configuracion['errores_manejo_usuarios']['error'],configuracion['errores_manejo_usuarios']['usuario_texto'])
    
    elif not respuesta_ingresada:
        messagebox.showerror(configuracion['errores_manejo_usuarios']['error'],configuracion['errores_manejo_usuarios']['sin_respuesta'])


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())

