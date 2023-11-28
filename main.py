from tkinter import * 
from tkinter import ttk
from tkinter import messagebox
from botones_cifrado import boton_atbash, boton_cesar, buscar_error_atbash, buscar_error_cesar
from cifrados import cifrar_atbash, cifrar_cesar
from usuarios import obtener_preguntas, buscar_usuario, validacion_usuario, validacion_clave, agregar_usuario, leer_linea, olvide_contraseña
from mensajes import enviar_mensaje
from mensajes_consultar import armar_archivo_mensajes
import os

def cargar_configuraciones():
    # Devuelve textos y configuraciones
    # Autor: Julen Gaumard

    predeterminados = {
        'nombre_ventanas': {
            'bienvenida': "TP Grupal Parte 2 - Grupo: PALA",
            'principal': "Cifrado y envío de mensajes",
            'identificacion': "Identificación para acceso",
            'creacion': "Creacion de usuario",
            'recuperar_clave': "Recuperar contraseña",
            'Destinatario': "Enviar Mensaje",
            'mensajes': "Mensajes recibidos",
            'lista_ventanas': ['identificacion', 'creacion', 'recuperar_clave', 'cesar', 'atbash', 'mensajes']
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
            'enviar_atbash':"Enviar mensaje Cifrado Atbash",
            'recibir_mensajes':"Mensajes recibidos",

        },

        'ventana_mensajes': {
            'ingresar_destinatario' : "Destinatario:",
            'ingresar_usuario' : "Ingrese nombre de usuario: ",
            'cesar' : "Cifrado cesar: ",
            'atbash' : "Cifrado atbash: ",
            'enviar' : "Enviar ",
            'mensajes_recibidos' : "Mensajes recibidos",
            'lista_mensajes' : "lista de mensajes:",
            'no_mensajes' : "no tienes mensajes recibidos",
            'cantidad_mensajes':"Total de mensajes recibidos: "

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

def crear_usuario(usuario_ingresado, clave, opcion, respuesta, raiz, configuracion):
    # Hace las validaciones correspondientes y crea el usuario
    # Autor: Julen Gaumard

    if usuario_ingresado == "" or clave == "" or respuesta == "":
        messagebox.showerror(configuracion['errores_manejo_usuarios']['incompleto_titulo'], configuracion['errores_manejo_usuarios']['incompleto_texto'])
    elif buscar_usuario(usuario_ingresado):
        messagebox.showwarning(configuracion['errores_manejo_usuarios']['buscar_titulo'], configuracion['errores_manejo_usuarios']['buscar_texto'])
    elif not validacion_usuario(usuario_ingresado):
        messagebox.showwarning(configuracion['errores_manejo_usuarios']['usuario_titulo'], configuracion['errores_manejo_usuarios']['usuario_texto'])
    elif not validacion_clave(clave):
        messagebox.showwarning(configuracion['errores_manejo_usuarios']['clave_titulo'], configuracion['errores_manejo_usuarios']['clave_texto'])
    else:
        agregar_usuario(usuario_ingresado, clave, opcion, respuesta)
        generar_siguiente_ventana(raiz,-1,configuracion,usuario_ingresado)

def iniciar_sesion(usuario_ingresado, clave, raiz, configuracion):
    # Chequea si el usuario existe y si la clave ingresa coincide
    # Autor: Julen Gaumard

    usuario = buscar_usuario(usuario_ingresado)

    if usuario_ingresado == "" or clave == "":
        messagebox.showerror(configuracion['errores_manejo_usuarios']['incompleto_titulo'], configuracion['errores_manejo_usuarios']['incompleto_texto'])
    elif not usuario: 
        messagebox.showerror(configuracion['errores_manejo_usuarios']['incorrectos_titulo'], configuracion['errores_manejo_usuarios']['incorrectos_texto'])
    elif int(usuario[4]) > 2:
        messagebox.showerror(configuracion['errores_manejo_usuarios']['bloquado_titulo'], configuracion['errores_manejo_usuarios']['bloquado_texto'])
    elif usuario[1] == clave:
        generar_siguiente_ventana(raiz,-1,configuracion,usuario_ingresado)
    else:
        messagebox.showerror(configuracion['errores_manejo_usuarios']['incorrectos_titulo'], configuracion['errores_manejo_usuarios']['incorrectos_texto'])

def elejir_destinatario(usuario_ingresado,configuracion,texto,tipo,clave= False,raiz=False):
    # Autor: Dominguez Lucia Juan Pablo
    # Cifra el mensaje, y genera ventana para ingresar destinatario

    mensaje_cifrado = False

    if tipo == "C":
        error = buscar_error_cesar(texto,clave)
        if not error:
            mensaje_cifrado = cifrar_cesar(texto,int(clave))
            
    else:
        error = buscar_error_atbash(texto)
        if not error:
            mensaje_cifrado = cifrar_atbash(texto)

             
    if mensaje_cifrado:
        datos = [mensaje_cifrado,tipo,clave]        
        generar_siguiente_ventana(raiz,3,configuracion,usuario_ingresado,datos)

#--------------------------Ventana principal-----------------------------
def crear_ventana_principal(raiz,configuracion,usuario_ingresado):
    # Autor: Dominguez Lucia Juan Pablo
    # Parametros iniciales de la ventana principal
    
    Frame_principal = ttk.Frame(raiz)

    var_texto = StringVar(raiz)
    var_resultado = StringVar(raiz)
    var_clave = StringVar(raiz)

    
    Bienvenida = ttk.Label(Frame_principal,text=configuracion["ventana_principal"]["bienvenida"] + usuario_ingresado + "!", font= ("bahnschrift",12,"underline"), foreground="grey").grid(row=0,sticky = "w")
    boton_recibir_mesajes = ttk.Button(Frame_principal,text=configuracion["ventana_principal"]["recibir_mensajes"],command = lambda:generar_siguiente_ventana(False, 4, configuracion,usuario_ingresado),width=20).grid(row=0,padx=10,pady=5,sticky = "e")
    Ingreso_mensaje = ttk.Label(Frame_principal,text=configuracion["ventana_principal"]["ingresar_mensajes"], font= ("bahnschrift",14,"underline")).grid(row=1,sticky = "w")
    cuadro_de_ingreso_mensaje = ttk.Entry(Frame_principal,textvariable=var_texto, width=50).grid(row=2,column=0,padx=5,pady=10)

    ttk.Separator(Frame_principal, orient='horizontal').grid(row=3,pady=10)

    #Cifrado cesar

    frame_cesar = ttk.Frame(Frame_principal)
    frame_cesar.grid(row=4,column=0,sticky="w")


    Titulo_cesar = ttk.Label(frame_cesar,text=configuracion["ventana_principal"]["cesar"], font= ("bahnschrift",11,"underline")).grid(row=1,sticky = "w",columnspan=2)
    texto_aclaracion = ttk.Label(frame_cesar,text=configuracion["ventana_principal"]["clave"], font= ("bahnschrift",10)).grid(row=2,sticky = "w",padx=10,pady=10)
    cuadro_de_ingreso_clave = ttk.Entry(frame_cesar,width=10,textvariable= var_clave).grid(row=2,column=1,pady=10)
    boton_cifrar_cesar = ttk.Button(frame_cesar, text=configuracion["ventana_principal"]["cifrar"],width=8,command= lambda: boton_cesar(var_texto.get(),var_clave.get(),var_resultado,1)).grid(row=2,column=2,padx=10,pady=10)
    boton_descifrar_cesar = ttk.Button(frame_cesar, text=configuracion["ventana_principal"]["descifrar"],width=8,command= lambda: boton_cesar(var_texto.get(),var_clave.get(),var_resultado,2)).grid(row=2,column=3,pady=10)

    ttk.Separator(Frame_principal, orient='horizontal').grid(row=5,pady=10)

    #Cifrado atbash

    frame_atbash = ttk.Frame(Frame_principal)
    frame_atbash.grid(row=6,column=0,sticky="w")

    Titulo_atbash = ttk.Label(frame_atbash,text= configuracion["ventana_principal"]["atbash"], font= ("bahnschrift",11,"underline")).grid(row=1,sticky = "w",columnspan=2)
    boton_cifrar_atbash = ttk.Button(frame_atbash, text=configuracion["ventana_principal"]["cifrar"],width=8,command= lambda : boton_atbash(var_texto.get(),var_resultado)).grid(row=2,column=0,padx=10,pady=10)
    boton_descifrar_atbash = ttk.Button(frame_atbash, text=configuracion["ventana_principal"]["descifrar"],width=8,command= lambda : boton_atbash(var_texto.get(),var_resultado)).grid(row=2,column=1,pady=10)

    ttk.Separator(Frame_principal, orient='horizontal').grid(row=7,pady=10)

    #Resultado
    frame_resul = ttk.Frame(Frame_principal)
    frame_resul.grid(row=8,column=0,sticky="w")

    Titulo_resultado = ttk.Label(frame_resul,text=configuracion["ventana_principal"]["resultado"][0], font= ("bahnschrift",14,"underline")).grid(row=0,sticky = "w")
    Resultado = ttk.Label(frame_resul, font=("bahnschrift", 10), textvariable = var_resultado).grid(row=1, column=0, padx = 10, pady=5, sticky="w") 
    var_resultado.set(configuracion["ventana_principal"]["resultado"][1])

    ttk.Separator(Frame_principal, orient='horizontal').grid(row=9,pady=5)

    #Envio y recibimiento de mensajes
    Envio_cifrado_cesar = ttk.Button(Frame_principal,text=configuracion["ventana_principal"]["enviar_cesar"],command= lambda : elejir_destinatario(usuario_ingresado,configuracion,var_texto.get(),"C",var_clave.get()),width=30).grid(row=10,padx=10,pady=5)
    Envio_cifrado_atbash = ttk.Button(Frame_principal,text=configuracion["ventana_principal"]["enviar_atbash"],command= lambda :elejir_destinatario(usuario_ingresado,configuracion,var_texto.get(),"A"), width=30).grid(row=11,padx=10,pady=5)

    Frame_principal.pack(padx=10, pady=10)
    raiz.mainloop()

def generar_siguiente_ventana(raiz, opcion, configuracion,usuario_ingresado = False, datos = False):
    # Crea la ventana correspondiente, segun la opcion recibida.
    # Autor: Julen Gaumard y Dominguez Lucia Juan Pablo
    
    # titulo_ventana = configuracion['nombre_ventanas'][configuracion['nombre_ventanas']['lista_ventanas'][opcion]]
    if raiz:
        raiz.destroy()
    
    titulo_ventana = configuracion['nombre_ventanas'][list(configuracion['nombre_ventanas'].keys())[opcion + 2]]
    raiz_nueva = crear_raiz(titulo_ventana)

    if opcion == -1:
        crear_ventana_principal(raiz_nueva,configuracion,usuario_ingresado)

    elif opcion >= 0 and opcion < 2:
        crear_interfaz_identificacion(raiz_nueva, opcion, configuracion)
    
    elif opcion == 2:
        crear_interfaz_recuperacion(raiz_nueva,configuracion)
    
    elif opcion == 3:
        crear_interfaz_destinatario(raiz_nueva,configuracion,usuario_ingresado,datos)
        
    elif opcion == 4:
        # crea ventana de mensajes recibidos segun el usuario
        armar_archivo_mensajes(usuario_ingresado)

        ar_mensajes = open("mensajes_recibidos.csv","r")
        mensaje = leer_linea(ar_mensajes)
        ar_mensajes.close()

        if not mensaje:
            messagebox.showinfo("No se encontraron mensajes", "No has recibido ningun mensaje")

        crear_interfaz_recibir_mensajes(raiz_nueva,configuracion)


# TODO: Revisar y simplificar
def crear_interfaz_destinatario(raiz,configuracion, usuario_ingresado,datos):
    # Crea la interfaz dependiente del boton presionado
    # Autor: Dominguez Lucia Juan Pablo
    
    #Interfaz el envio de mensajes dependiendo del cifrado

    var_usuario = usuario_ingresado
    var_destinatario = StringVar(raiz)
    mensaje_cifrado = datos[0]
    opcion = datos[1]
    clave = datos[2]
    

    frame_destinatario = ttk.Frame(raiz)

    Titulo_destinatario = ttk.Label(frame_destinatario,text=configuracion["ventana_mensajes"]["ingresar_destinatario"], font= ("bahnschrift",14,"underline")).grid(row=0,columnspan=2)
    Ingrese_destinatario = ttk.Label(frame_destinatario,text=configuracion["ventana_mensajes"]["ingresar_usuario"], font= ("bahnschrift",10)).grid(row=1,column = 0 ,sticky = "w",padx=10,pady=10)
    cuadro_de_destinatario = ttk.Entry(frame_destinatario,textvariable=var_destinatario, width=20).grid(row=1,column=1,padx=5,pady=10)

    boton_enviar = ttk.Button(frame_destinatario, text=configuracion["ventana_mensajes"]["enviar"],command= lambda: enviar_mensaje(var_destinatario.get(),var_usuario,opcion,clave,mensaje_cifrado) ,width=12).grid(row=9,padx=10,pady=10,columnspan=2)
    frame_destinatario.pack(padx=10)
    
# enviar_mensaje(var_destinatario.get(),var_usuario,opcion,var_clave.get(),var_resultado.get()

def crear_interfaz_identificacion(raiz, opcion, configuracion):
    # Crea la interfaz tanto para el ingreso o creacion de usuario, segun corresponda
    # Autor: Julen Gaumard

    frame_usuarios = ttk.Frame(raiz)

    var_clave = StringVar(raiz)
    var_opcion = StringVar(raiz)
    var_respuesta = StringVar(raiz)
    var_usuario = StringVar(raiz)

    ttk.Label(frame_usuarios, text=configuracion["ventana_usuarios"]["ingresar"], font=("bahnschrift", 14 ,"underline")).grid(row=0, column=0, pady=10, columnspan=2)
    
    ttk.Label(frame_usuarios,text=configuracion["ventana_usuarios"]["usuario"]).grid(row=1, column=0, pady=5, sticky="w")
    ttk.Entry(frame_usuarios,textvariable = var_usuario).grid(row=1, column=1, pady=5, sticky="e")

    ttk.Label(frame_usuarios,text=configuracion["ventana_usuarios"]["clave"]).grid(row=3, column=0, pady=5, sticky="w")
    ttk.Entry(frame_usuarios,textvariable = var_clave, show="*").grid(row=3, column=1, pady=5, sticky="e")

    if opcion == 1:
        opciones = obtener_preguntas()
        var_opcion.set(opciones[0]) 
        
        ttk.Label(frame_usuarios,text=configuracion["ventana_usuarios"]["pregunta"]).grid(row=4, column=0, pady=5, sticky="w")
        ttk.OptionMenu(frame_usuarios, var_opcion, *opciones).grid(row=4, column=1, pady=5, sticky="e")
        
        ttk.Label(frame_usuarios,text=configuracion["ventana_usuarios"]["respuesta"]).grid(row=5, column=0, pady=5, sticky="w")
        ttk.Entry(frame_usuarios,textvariable = var_respuesta).grid(row=5, column=1, pady=5, sticky="e")

        ttk.Button(frame_usuarios, text=configuracion["ventana_usuarios"]["crear"], command = lambda : crear_usuario(var_usuario.get(), var_clave.get(), var_opcion.get(), var_respuesta.get(), raiz, configuracion)).grid(row=9, column=1, pady=10, sticky="e")

    else:
        ttk.Button(frame_usuarios, text=configuracion["ventana_usuarios"]["olvide"], command = lambda: generar_siguiente_ventana(raiz,2,configuracion) ).grid(row=9, column=0, pady=10, sticky="w")
        ttk.Button(frame_usuarios, text=configuracion["ventana_usuarios"]["iniciar"], command = lambda : iniciar_sesion(var_usuario.get(), var_clave.get(), raiz, configuracion)).grid(row=9, column=1, pady=10, sticky="e")

    frame_usuarios.pack(padx=10)

def crear_interfaz_recuperacion(raiz,configuracion):
    # Autor: Dominguez Lucia Juan Pablo
    # Crea la interfaz para la recuperacion de contraseña
    frame_recuperar = ttk.Frame(raiz)

    var_usuario = StringVar(raiz)
    var_pregunta = StringVar(raiz)
    var_respuesta = StringVar(raiz)

    opciones = obtener_preguntas()
    var_pregunta.set(opciones[0]) 


    ttk.Label(frame_recuperar, text=configuracion["nombre_ventanas"]["recuperar_clave"], font=("bahnschrift", 14 ,"underline")).grid(row=0, column=0, pady=10, columnspan=2)

    ttk.Label(frame_recuperar,text=configuracion["ventana_usuarios"]["usuario"]).grid(row=1, column=0, pady=5, sticky="w")
    ttk.Entry(frame_recuperar,textvariable = var_usuario).grid(row=1, column=1, pady=5, sticky="e")

    ttk.Label(frame_recuperar,text=configuracion["ventana_usuarios"]["pregunta"]).grid(row=2, column=0, pady=5, sticky="w")
    ttk.OptionMenu(frame_recuperar, var_pregunta, *opciones).grid(row=2, column=1, pady=5, sticky="e")

    ttk.Label(frame_recuperar,text=configuracion["ventana_usuarios"]["respuesta"]).grid(row=3, column=0, pady=5, sticky="w")
    ttk.Entry(frame_recuperar,textvariable = var_respuesta).grid(row=3, column=1, pady=5, sticky="e")

    ttk.Button(frame_recuperar, text=configuracion["nombre_ventanas"]["recuperar_clave"],command= lambda: olvide_contraseña(var_usuario.get(),var_pregunta.get(),var_respuesta.get()), width= 20).grid(row=6, column=1, pady=10, sticky="e")

    frame_recuperar.pack(padx=10)

def crear_interfaz_recibir_mensajes(raiz,configuracion):
   # Autor: Dominguez Lucia Juan Pablo
   # Crea la interfaz para recibir los mensajes
    frame_mensajes = ttk.Frame(raiz)
    titulo_mensajes = ttk.Label(frame_mensajes,text=configuracion["ventana_mensajes"]["mensajes_recibidos"], font= ("bahnschrift",14,"underline")).grid(row=0)
    lista_mensajes = ttk.Label(frame_mensajes,text=configuracion["ventana_mensajes"]["lista_mensajes"], font= ("bahnschrift",11,"underline")).grid(row=1,sticky="w")

    with open("mensajes_recibidos.csv") as ar_mensajes:

        linea_mensajes = leer_linea(ar_mensajes)

        ult_renglon = 2
        cant_mensaje = 0

        while linea_mensajes:
                
            remitente,mensaje_descifrado = linea_mensajes

            mensaje = remitente + ": " + mensaje_descifrado

            titulo_mensajes = ttk.Label(frame_mensajes,text="-" *150, font= ("bahnschrift",12)).grid(row=ult_renglon,sticky="w")
            mensaje_recibido = ttk.Label(frame_mensajes,text=mensaje, font= ("bahnschrift",12,"bold")).grid(row=ult_renglon+1,sticky="w")

            ult_renglon += 2
            cant_mensaje += 1

            linea_mensajes = leer_linea(ar_mensajes)

    os.remove("mensajes_recibidos.csv")

    frame_cantidad = ttk.Frame(frame_mensajes)
    frame_cantidad.grid(row=ult_renglon,padx=10,)

    cantidad_mensajes = ttk.Label(frame_cantidad,text=configuracion["ventana_mensajes"]["cantidad_mensajes"],font=("bahnschrift",12)).grid(row=0,sticky="w")
    cantidad_mensajes = ttk.Label(frame_cantidad,text=cant_mensaje,font=("bahnschrift",12,"bold")).grid(row=0,column=1,sticky="w")

    frame_mensajes.pack(padx=10)

def crear_ventana_bienvenida(raiz, configuracion):
    # Crea la interfaz de la pantalla de bienvenida
    # Autor: Julen Gaumard

    frame_global = ttk.Frame(raiz)

    ttk.Label(frame_global,text=configuracion['ventana_bienvenida']['titulo'], font=("bahnschrift",14,"underline")).grid(row=0, column=0, padx=5, pady=5, sticky="w")
    ttk.Label(frame_global,text=configuracion['ventana_bienvenida']['subtitulo']).grid(row=1, column=0, padx=5, sticky="w")
    ttk.Label(frame_global,text=configuracion['ventana_bienvenida']['subtitulo_2']).grid(row=2, column=0, padx=5, sticky="w")

    botones_frame = ttk.Frame(frame_global)
    ttk.Button(botones_frame, text=configuracion['ventana_usuarios']['crear'], command = lambda : generar_siguiente_ventana(raiz, 1, configuracion)).grid(row=3, column=0, padx=5, pady=12, sticky="e")
    ttk.Button(botones_frame, text=configuracion['ventana_usuarios']['ingresar'], command = lambda : generar_siguiente_ventana(raiz, 0, configuracion)).grid(row=3, column=1, padx=5, pady=12, sticky="e")
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