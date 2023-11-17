from tkinter import * 
from tkinter import ttk
from tkinter import messagebox
from botones_cifrado import boton_atbash, boton_cesar
from usuarios import obtener_preguntas, buscar_usuario, validacion_usuario, validacion_clave, agregar_usuario
from mensajes import enviar_mensaje

def cargar_configuraciones():
    # Devuelve textos y configuraciones
    # Autor: Julen Gaumard

    predeterminados = {
        'nombre_ventanas': {
            'bienvenida': "TP Grupal Parte 2 - Grupo: PALA",
            'principal': "Cifrado y envío de mensajes",
            'identificacion': "Identificación para acceso",
            'creacion': "Creacion de usuario",
            'cesar': "Enviar mensaje Cesar",
            'atbash': "Enviar mensaje Atbash"
        },

        'ventana_bienvenida': {
            'titulo': 'Bienvenido! ',
            'subtitulo': "A la aplicación de mensajes secretos del grupo Pala.",
            'subtitulo_2':"Para continuar presione continuar, de lo contrario cierre la ventana.",
            'desarrolladores': ["Alessandro Perez", "Julen Gaumard", "Juan Pablo Dominguez Lucia"],
            'construida': "Construída por:",
        },

        'ventana_principal': {
            'bienvenida' : "Bienvenido ",
            'ingresar_mensajes' : "\nIngrese mesaje para decifrar:",
            'cesar':"Cifrado cesar",
            'atbash':"Cifrado Atbash",
            'resultado':["Resultado:","el resultado se mostrara aqui"],
            'clave':"Clave:",
            'cifrar':"Cifrar",
            'descifrar':"Descifrar",
            'enviar_cesar':"Enviar mensaje Cifrado Cesar",
            'enviar_atbash':"Enviar mensaje Cifrado Atbash"

        },

        'ventana_mensajes': {
            'ingresar_destinatario' : "Destinatario:",
            'ingresar_usuario' : "Ingrese nombre de usuario: ",
            'cesar' : "Cifrado cesar: ",
            'atbash' : "Cifrado atbash: ",
            'enviar' : "Enviar "

        },
        
        'errores_manejo_usuarios': {
            'incompleto_titulo': "Datos incompletos",
            'incompleto_texto': "Complete los datos para continuar",
            'buscar_titulo': "Usuario Existente",
            'buscar_texto': "Ya existe un usuario con ese nombre.",
            'usuario_titulo': "Usuario invalido",
            'usuario_texto': "El nombre de usuario no es valido.",
            'clave_titulo': "Clave invalida",
            'clave_texto': "La clave no es valida.",
            'incorrectos_titulo': "Identificador inexistente o clave erronea",
            'incorrectos_texto': "Si no se encuentra registrado debe registrarse previamente o si olvidaste la clave presiona el botón recuperar clave",
            'bloquado_titulo': "Atencion",
            'bloquado_texto': "Usuario Bloqueado",
        },

        'ventana_usuarios': {
            'usuario': "Usuario:",
            'clave': "Clave:",
            'pregunta': "Pregunta:",
            'respuesta': "Respuesta:",
            'ingresar': "Ingreso Usuario",
            'crear': "Crear Usuario",
            'olvide': "Olvide Clave",
            'iniciar': "Ingresar"
        }

    }

    return predeterminados


#--------------------------Ventana principal-----------------------------
def crear_ventana_principal(configuracion,usuario_ingresado):
    # Autor: Dominguez Lucia Juan Pablo
    #Parametros iniciales de la ventana principal

    Ventana = crear_raiz(configuracion["nombre_ventanas"]["principal"])
    
    Frame_principal = ttk.Frame(Ventana)

    var_texto = StringVar(Ventana)
    var_resultado = StringVar(Ventana)
    var_clave = StringVar(Ventana)

    Bienvenida = ttk.Label(Frame_principal,text=configuracion["ventana_principal"]["bienvenida"] + usuario_ingresado + "!", font= ("bahnschrift",12,"underline"), foreground="grey").grid(row=0,sticky = "w")
    Ingreso_mensaje = ttk.Label(Frame_principal,text=configuracion["ventana_principal"]["ingresar_mensajes"], font= ("bahnschrift",14,"underline")).grid(row=1,sticky = "w")
    cuadro_de_ingreso_mensaje = ttk.Entry(Frame_principal,textvariable=var_texto, width=50).grid(row=2,column=0,padx=5,pady=10)

    ttk.Separator(Frame_principal, orient='horizontal').grid(row=3,pady=10)

    #Apartado para el cifrado cesar

    frame_cesar = ttk.Frame(Frame_principal)
    frame_cesar.grid(row=4,column=0,sticky="w")


    Titulo_cesar = ttk.Label(frame_cesar,text=configuracion["ventana_principal"]["cesar"], font= ("bahnschrift",11,"underline")).grid(row=1,sticky = "w",columnspan=2)
    texto_aclaracion = ttk.Label(frame_cesar,text=configuracion["ventana_principal"]["clave"], font= ("bahnschrift",10)).grid(row=2,sticky = "w",padx=10,pady=10)
    cuadro_de_ingreso_clave = ttk.Entry(frame_cesar,width=10,textvariable= var_clave).grid(row=2,column=1,pady=10)
    boton_cifrar_cesar = ttk.Button(frame_cesar, text=configuracion["ventana_principal"]["cifrar"],width=8,command= lambda: boton_cesar(var_texto.get(),var_clave.get(),var_resultado,1)).grid(row=2,column=2,padx=10,pady=10)
    boton_descifrar_cesar = ttk.Button(frame_cesar, text=configuracion["ventana_principal"]["descifrar"],width=8,command= lambda: boton_cesar(var_texto.get(),var_clave.get(),var_resultado,2)).grid(row=2,column=3,pady=10)

    ttk.Separator(Frame_principal, orient='horizontal').grid(row=5,pady=10)

    #Apartado para el cifrado atbash

    frame_atbash = ttk.Frame(Frame_principal)
    frame_atbash.grid(row=6,column=0,sticky="w")

    Titulo_atbash = ttk.Label(frame_atbash,text= configuracion["ventana_principal"]["atbash"], font= ("bahnschrift",11,"underline")).grid(row=1,sticky = "w",columnspan=2)
    boton_cifrar_atbash = ttk.Button(frame_atbash, text=configuracion["ventana_principal"]["cifrar"],width=8,command= lambda : boton_atbash(var_texto.get(),var_resultado)).grid(row=2,column=0,padx=10,pady=10)
    boton_descifrar_atbash = ttk.Button(frame_atbash, text=configuracion["ventana_principal"]["descifrar"],width=8,command= lambda : boton_atbash(var_texto.get(),var_resultado)).grid(row=2,column=1,pady=10)

    ttk.Separator(Frame_principal, orient='horizontal').grid(row=7,pady=10)

    #Apartado para el Resultado
    frame_resul = ttk.Frame(Frame_principal)
    frame_resul.grid(row=8,column=0,sticky="w")

    Titulo_resultado = ttk.Label(frame_resul,text=configuracion["ventana_principal"]["resultado"][0], font= ("bahnschrift",14,"underline")).grid(row=0,sticky = "w")
    Resultado = ttk.Label(frame_resul, font=("bahnschrift", 10), textvariable = var_resultado).grid(row=1, column=0, padx = 10, pady=5, sticky="w") 
    var_resultado.set(configuracion["ventana_principal"]["resultado"][1])

    ttk.Separator(Frame_principal, orient='horizontal').grid(row=9,pady=5)

    #Envio de mensajes
    Envio_cifrado_cesar = ttk.Button(Frame_principal,text=configuracion["ventana_principal"]["enviar_cesar"],command= lambda :generar_siguiente_ventana("", 3, configuracion,usuario_ingresado),width=30).grid(row=10,padx=10,pady=5)
    Envio_cifrado_atbash = ttk.Button(Frame_principal,text=configuracion["ventana_principal"]["enviar_atbash"],command= lambda :generar_siguiente_ventana("", 4, configuracion,usuario_ingresado), width=30).grid(row=11,padx=10,pady=5)
 
    Frame_principal.pack(padx=10, pady=10)
    Ventana.mainloop()


#--------------------------Ventana de bienvenida-----------------------------

def generar_siguiente_ventana(raiz, opcion, configuracion,usuario_ingresado):
    # Crea la ventana correspondiente, segun la opcion recibida.
    # Autor: Julen Gaumard y Dominguez Lucia Juan Pablo

    if opcion == 1:
        raiz.destroy()
        raiz_nueva = crear_raiz(configuracion['nombre_ventanas']['identificacion'])
        crear_ventana_botones(raiz_nueva, opcion, configuracion,usuario_ingresado)

    elif opcion == 2:
        raiz.destroy()
        raiz_nueva = crear_raiz(configuracion['nombre_ventanas']['creacion'])
        crear_ventana_botones(raiz_nueva, opcion, configuracion,usuario_ingresado)
    
    elif opcion == 3:
        raiz_nueva = crear_raiz(configuracion['nombre_ventanas']['cesar'])
        crear_ventana_botones(raiz_nueva, opcion, configuracion,usuario_ingresado)
    
    elif opcion == 4:
        raiz_nueva = crear_raiz(configuracion['nombre_ventanas']['atbash'])
        crear_ventana_botones(raiz_nueva, opcion, configuracion,usuario_ingresado)


def crear_usuario(nombre_user, clave, opcion, respuesta, raiz, configuracion):

    if nombre_user == "" or clave == "" or respuesta == "":
        messagebox.showerror(configuracion['errores_manejo_usuarios']['incompleto_titulo'], configuracion['errores_manejo_usuarios']['incompleto_texto'])
    elif buscar_usuario(nombre_user):
        messagebox.showwarning(configuracion['errores_manejo_usuarios']['buscar_titulo'], configuracion['errores_manejo_usuarios']['buscar_texto'])
    elif not validacion_usuario(nombre_user):
        messagebox.showwarning(configuracion['errores_manejo_usuarios']['usuario_titulo'], configuracion['errores_manejo_usuarios']['usuario_texto'])
    elif not validacion_clave(clave):
        messagebox.showwarning(configuracion['errores_manejo_usuarios']['clave_titulo'], configuracion['errores_manejo_usuarios']['clave_texto'])
    else:
        agregar_usuario(nombre_user, clave, opcion, respuesta)
        raiz.destroy()
        crear_ventana_principal(configuracion,nombre_user)

def iniciar_sesion(nombre_user, clave, raiz, configuracion):
    # Chequea si el usuario existe y si la clave ingresa coincide
    # Autor: Julen Gaumard

    usuario = buscar_usuario(nombre_user)

    if nombre_user == "" or clave == "":
        messagebox.showerror(configuracion['errores_manejo_usuarios']['incompleto_titulo'], configuracion['errores_manejo_usuarios']['incompleto_texto'])
    elif not usuario: 
        messagebox.showerror(configuracion['errores_manejo_usuarios']['incorrectos_titulo'], configuracion['errores_manejo_usuarios']['incorrectos_texto'])
    elif int(usuario[4]) > 2:
        messagebox.showerror(configuracion['errores_manejo_usuarios']['bloquado_titulo'], configuracion['errores_manejo_usuarios']['bloquado_texto'])
    elif usuario[1] == clave:
        raiz.destroy()
        crear_ventana_principal(configuracion,nombre_user)
    else:
        messagebox.showerror(configuracion['errores_manejo_usuarios']['incorrectos_titulo'], configuracion['errores_manejo_usuarios']['incorrectos_texto'])


def crear_raiz(nombre_ventana):
    # Crea una ventana generica, a la cual mediante otra funcion se le agregan los elementos necesarios
    # Autor: Julen Gaumard

    raiz = Tk()
    raiz.resizable(False,False)
    raiz.title(nombre_ventana)
    raiz.iconbitmap("icon.ico")
    estilo = ttk.Style(raiz)
    estilo.theme_use('vista')
    return raiz


def crear_ventana_botones(raiz, opcion, configuracion,usuario_ingresado):
    # Crea la interfaz dependiente del boton presionado
    # Autor: Julen Gaumard y Dominguez Lucia Juan Pablo


    if opcion < 3:
        frame_usuarios = ttk.Frame(raiz)

        var_clave = StringVar(raiz)
        var_opcion = StringVar(raiz)
        var_respuesta = StringVar(raiz)
        var_usuario = StringVar(raiz)

        ttk.Label(frame_usuarios, text=configuracion["ventana_usuarios"]["ingresar"], font=("Arial", 20)).grid(row=0, column=0, pady=10, sticky="w", columnspan=2)
        
        ttk.Label(frame_usuarios,text=configuracion["ventana_usuarios"]["usuario"]).grid(row=1, column=0, pady=5, sticky="w")
        ttk.Entry(frame_usuarios,textvariable = var_usuario).grid(row=1, column=1, pady=5, sticky="e")

        ttk.Label(frame_usuarios,text=configuracion["ventana_usuarios"]["clave"]).grid(row=3, column=0, pady=5, sticky="w")
        ttk.Entry(frame_usuarios,textvariable = var_clave, show="*").grid(row=3, column=1, pady=5, sticky="e")

        if opcion == 2:
            opciones = obtener_preguntas()
            var_opcion.set(opciones[0]) 
            
            ttk.Label(frame_usuarios,text=configuracion["ventana_usuarios"]["pregunta"]).grid(row=4, column=0, pady=5, sticky="w")
            ttk.OptionMenu(frame_usuarios, var_opcion, *opciones).grid(row=4, column=1, pady=5, sticky="e")
            
            ttk.Label(frame_usuarios,text=configuracion["ventana_usuarios"]["respuesta"]).grid(row=5, column=0, pady=5, sticky="w")
            ttk.Entry(frame_usuarios,textvariable = var_respuesta).grid(row=5, column=1, pady=5, sticky="e")

            ttk.Button(frame_usuarios, text=configuracion["ventana_usuarios"]["crear"], command = lambda : crear_usuario(var_usuario.get(), var_clave.get(), var_opcion.get(), var_respuesta.get(), raiz, configuracion)).grid(row=9, column=1, pady=10, sticky="e")

        else:
            ttk.Button(frame_usuarios, text=configuracion["ventana_usuarios"]["olvide"], ).grid(row=9, column=0, pady=10, sticky="w")
            ttk.Button(frame_usuarios, text=configuracion["ventana_usuarios"]["iniciar"], command = lambda : iniciar_sesion(var_usuario.get(), var_clave.get(), raiz, configuracion)).grid(row=9, column=1, pady=10, sticky="e")

        frame_usuarios.pack(padx=10)


    else:
        
        frame_mensajes = ttk.Frame(raiz)
        var_usuario = usuario_ingresado
        var_destinatario = StringVar(raiz)
        var_texto = StringVar(raiz)
        var_clave = StringVar(raiz)
        var_resultado = StringVar(raiz)

        Ingreso_mensaje = ttk.Label(frame_mensajes,text=configuracion["ventana_principal"]["ingresar_mensajes"], font= ("bahnschrift",14,"underline")).grid(row=0,sticky = "w")
        cuadro_de_ingreso_mensaje = ttk.Entry(frame_mensajes,textvariable=var_texto, width=50).grid(row=1,column=0,padx=5,pady=10)

        ttk.Separator(frame_mensajes, orient='horizontal').grid(row=2,pady=10)

        if opcion == 3:
            #Apartado para el cifrado cesar

            frame_cesar = ttk.Frame(frame_mensajes)
            frame_cesar.grid(row=3,column=0,sticky="w")

            Titulo_cesar = ttk.Label(frame_cesar,text=configuracion["ventana_mensajes"]["cesar"], font= ("bahnschrift",14,"underline")).grid(row=1,sticky = "w",columnspan=2)
            texto_aclaracion = ttk.Label(frame_cesar,text=configuracion["ventana_principal"]["clave"], font= ("bahnschrift",10)).grid(row=2,sticky = "w",padx=10,pady=10)
            cuadro_de_ingreso_clave = ttk.Entry(frame_cesar,width=10,textvariable= var_clave).grid(row=2,column=1,pady=10)
            boton_cifrar_cesar = ttk.Button(frame_cesar, text=configuracion["ventana_principal"]["cifrar"],width=8,command= lambda: boton_cesar(var_texto.get(),var_clave.get(),var_resultado,1)).grid(row=2,column=2,padx=10,pady=10)
            boton_descifrar_cesar = ttk.Button(frame_cesar, text=configuracion["ventana_principal"]["descifrar"],width=8,command= lambda: boton_cesar(var_texto.get(),var_clave.get(),var_resultado,2)).grid(row=2,column=3,pady=10)

            ttk.Separator(frame_mensajes, orient='horizontal').grid(row=4,pady=5)

        elif opcion == 4:
            #Apartado para el cifrado atbash

            frame_cesar = ttk.Frame(frame_mensajes)
            frame_cesar.grid(row=3,column=0,sticky="w")

            Titulo_cesar = ttk.Label(frame_cesar,text=configuracion["ventana_mensajes"]["atbash"], font= ("bahnschrift",14,"underline")).grid(row=1,sticky = "w",columnspan=2)
            boton_cifrar_atbash = ttk.Button(frame_cesar, text=configuracion["ventana_principal"]["cifrar"],width=8,command= lambda: boton_atbash(var_texto.get(),var_resultado)).grid(row=2,column=0,padx=10,pady=10)
            boton_descifrar_atbash = ttk.Button(frame_cesar, text=configuracion["ventana_principal"]["descifrar"],width=8,command= lambda: boton_atbash(var_texto.get(),var_resultado)).grid(row=2,column=1,pady=10)

            ttk.Separator(frame_mensajes, orient='horizontal').grid(row=4,pady=5)

        #Apartado para el Resultado
        frame_resul = ttk.Frame(frame_mensajes)
        frame_resul.grid(row=5,column=0,sticky="w")

        Titulo_resultado = ttk.Label(frame_resul,text=configuracion["ventana_principal"]["resultado"][0], font= ("bahnschrift",14,"underline")).grid(row=0,sticky = "w")
        Resultado = ttk.Label(frame_resul, font=("bahnschrift", 10), textvariable = var_resultado).grid(row=1, column=0, padx = 10, pady=5, sticky="w") 
        var_resultado.set(configuracion["ventana_principal"]["resultado"][1])

        ttk.Separator(frame_mensajes, orient='horizontal').grid(row=6,pady=5)


        #Apartado Destinatario

        frame_destinatario = ttk.Frame(frame_mensajes)
        frame_destinatario.grid(row=7,column=0,sticky="w")

        Titulo_destinatario = ttk.Label(frame_destinatario,text=configuracion["ventana_mensajes"]["ingresar_destinatario"], font= ("bahnschrift",14,"underline")).grid(row=0,sticky = "w")
        Ingrese_destinatario = ttk.Label(frame_destinatario,text=configuracion["ventana_mensajes"]["ingresar_usuario"], font= ("bahnschrift",10)).grid(row=1,column = 0 ,sticky = "w",padx=10,pady=10)
        cuadro_de_destinatario = ttk.Entry(frame_destinatario,textvariable=var_destinatario, width=20).grid(row=1,column=1,padx=5,pady=10)

        
        boton_enviar = ttk.Button(frame_mensajes, text=configuracion["ventana_mensajes"]["enviar"],command= lambda: enviar_mensaje(var_destinatario.get(),var_usuario,opcion,var_clave.get(),var_resultado.get()) ,width=12).grid(row=9,padx=10,pady=10)
        frame_mensajes.pack(padx=10)


def crear_ventana_bienvenida(raiz, configuracion):
    # Crea la interfaz de la pantalla de bienvenida
    # Autor: Julen Gaumard

    frame_global = ttk.Frame(raiz)

    ttk.Label(frame_global,text=configuracion['ventana_bienvenida']['titulo'], font=("Arial", 20)).grid(row=0, column=0, padx=5, pady=5, sticky="w")
    ttk.Label(frame_global,text=configuracion['ventana_bienvenida']['subtitulo']).grid(row=1, column=0, padx=5, sticky="w")
    ttk.Label(frame_global,text=configuracion['ventana_bienvenida']['subtitulo_2']).grid(row=2, column=0, padx=5, sticky="w")

    botones_frame = ttk.Frame(frame_global)
    ttk.Button(botones_frame, text=configuracion['ventana_usuarios']['crear'], command = lambda : generar_siguiente_ventana(raiz, 2, configuracion,"")).grid(row=3, column=0, padx=5, pady=10, sticky="e")
    ttk.Button(botones_frame, text=configuracion['ventana_usuarios']['ingresar'], command = lambda : generar_siguiente_ventana(raiz, 1, configuracion,"")).grid(row=3, column=1, padx=5, pady=10, sticky="e")
    botones_frame.grid(row=4, column=0, sticky="e")

    desarrollado_frame = ttk.Frame(frame_global)
    ttk.Label(desarrollado_frame,text=configuracion['ventana_bienvenida']['construida'], foreground="grey").grid(row=0, column=0, padx=5, sticky="w")
    for n in range(0, len(configuracion['ventana_bienvenida']['desarrolladores'])):
        ttk.Label(desarrollado_frame,text=configuracion['ventana_bienvenida']['desarrolladores'][n], foreground="grey").grid(row=n, column=1, padx=5, sticky="w")
   
    desarrollado_frame.grid(row=5, column=0, sticky="w", columnspan=2)
    frame_global.pack(padx=10, pady=10)


def main():
    # Comienza la aplicacion, creando la ventana de bienvenida
    # Autor: Julen Gaumard
    configuracion = cargar_configuraciones()
    raiz = crear_raiz(configuracion['nombre_ventanas']['bienvenida'])
    crear_ventana_bienvenida(raiz, configuracion)
    raiz.mainloop()

main()