from tkinter import * 
from tkinter import ttk
from tkinter import messagebox
from cifrados import cifrar_atbash, cifrar_cesar
from usuarios import obtener_preguntas, buscar_usuario, validacion_user, validacion_pass, agregar_usuario

def buscar_error_atbash(texto): 
    error = False
    if texto == "":
        messagebox.showerror("Datos incompletos","Debes ingresar un texto y una clave")
        error = True

    return error

def buscar_error_cesar(texto,clave): 
    error = False
    if texto == "" and clave == "":
        messagebox.showerror("Datos incompletos","Debes ingresar un texto y una clave")
        error = True
    elif texto == "" and clave != "":
        messagebox.showerror("Datos incompletos","Debes ingresar un texto")
        error = True
    elif texto != "" and clave == "":
        messagebox.showerror("Datos incompletos","Debes ingresar una clave")
        error = True
    elif not clave.isnumeric():
        messagebox.showerror("Datos incorrectos","la clave debe ser numerica")
        error = True
    return error
    
#Se ejecuta al presionar el boton de cifrado y descrifrado atbash
def boton_atbash(texto,resultado):
    error = buscar_error_atbash(texto)
    if error == False:
        cifrar = cifrar_atbash(texto)

        resultado.set(cifrar)

#Se ejecuta al presionar el boton de cifrado Cesar
def boton_cesar_cifrado(texto,clave,resultado):
    error = buscar_error_cesar(texto,clave)
    if error == False:
        cifrar = cifrar_cesar(texto,int(clave))

        resultado.set(cifrar)

#Se ejecuta al presionar el boton de descifrado Cesar

def boton_cesar_descifrado(texto,clave,resultado):
    error = buscar_error_cesar(texto,clave)
    if error == False:
        negativo = -int(clave)
        cifrar = cifrar_cesar(texto,negativo)

        resultado.set(cifrar)


#--------------------------Ventana principal-----------------------------
def Ventana_principal():
    #--Parametros iniciales de la ventana principal--

    ventana2 = crear_ventana("TP Grupal Parte 1 - Grupo: Pala")
    
    Frame_principal_2 = ttk.Frame(ventana2)

    text_var = StringVar(ventana2)
    result_var = StringVar(ventana2)
    clave_var = StringVar(ventana2)

    #--Contenido de la ventana principal--

    Ingreso_mensaje = ttk.Label(Frame_principal_2,text="\nIngrese mesaje para decifrar:", font= ("bahnschrift",14,"underline")).grid(row=0,sticky = "w")
    cuadro_de_ingreso_mensaje = ttk.Entry(Frame_principal_2,textvariable=text_var, width=50).grid(row=1,column=0,padx=5,pady=10)

    ttk.Separator(Frame_principal_2, orient='horizontal').grid(row=3,pady=10)

    #Apartado para el cifrado cesar

    frame_cesar = ttk.Frame(Frame_principal_2)
    frame_cesar.grid(row=4,column=0,sticky="w")


    Titulo_cesar = ttk.Label(frame_cesar,text="Cifrado cesar", font= ("bahnschrift",11,"underline")).grid(row=1,sticky = "w",columnspan=2)
    texto_aclaracion = ttk.Label(frame_cesar,text="Clave:", font= ("bahnschrift",10)).grid(row=2,sticky = "w",padx=10,pady=10)
    cuadro_de_ingreso_clave = ttk.Entry(frame_cesar,width=10,textvariable= clave_var).grid(row=2,column=1,pady=10)
    boton_cifrar_cesar = ttk.Button(frame_cesar, text="Cifrar",width=8,command= lambda: boton_cesar_cifrado(text_var.get(),clave_var.get(),result_var)).grid(row=2,column=2,padx=10,pady=10)
    boton_descifrar_cesar = ttk.Button(frame_cesar, text="Descifrar",width=8,command= lambda: boton_cesar_descifrado(text_var.get(),clave_var.get(),result_var)).grid(row=2,column=3,pady=10)

    ttk.Separator(Frame_principal_2, orient='horizontal').grid(row=5,pady=10)

    #Apartado para el cifrado atbash

    frame_atbash = ttk.Frame(Frame_principal_2)
    frame_atbash.grid(row=6,column=0,sticky="w")

    Titulo_atbash = ttk.Label(frame_atbash,text="Cifrado atbash", font= ("bahnschrift",11,"underline")).grid(row=1,sticky = "w",columnspan=2)
    boton_cifrar_atbash = ttk.Button(frame_atbash, text="Cifrar",width=8,command= lambda : boton_atbash(text_var.get(),result_var)).grid(row=2,column=0,padx=10,pady=10)
    boton_descifrar_atbash = ttk.Button(frame_atbash, text="Descifrar",width=8,command= lambda : boton_atbash(text_var.get(),result_var)).grid(row=2,column=1,pady=10)

    ttk.Separator(Frame_principal_2, orient='horizontal').grid(row=7,pady=10)

    #Apartado para el Resultado
    Titulo_resultado = ttk.Label(Frame_principal_2,text="Resultado:", font= ("bahnschrift",14,"underline")).grid(row=8,sticky = "w")
    Resultado = ttk.Label(Frame_principal_2, font=("bahnschrift", 10), textvariable = result_var).grid(row=9, column=0, padx = 10, pady=5, sticky="w") 
    result_var.set("El resultado se mostrara aqui.")

    Frame_principal_2.pack(padx=10, pady=10)

    ventana2.mainloop()


#--------------------------Ventana de bienvenida-----------------------------

def next_screen(root, opcion):
    # Destruye la ventana de bienvenida y crea la ventana principal
    # Autor: Julen Gaumard

    root.destroy()

    if opcion == 1:
        titulo = "Identificación para acceso"
    else:
        titulo = "Creacion de usuario"
    
    raiz_nueva = crear_ventana(titulo)
    ventana_usuarios(raiz_nueva, opcion)

    root.mainloop()

def crear_usuario(nombre_user, clave, opcion, respuesta, root):

    if nombre_user == "" or clave == "" or respuesta == "":
        messagebox.showerror("Datos incompletos", "Complete los datos para continuar")
    elif buscar_usuario(nombre_user):
        messagebox.showwarning("Usuario Existente", "Ya existe un usuario con ese nombre.")
    elif not validacion_user(nombre_user):
        messagebox.showwarning("Usuario invalido", "El nombre de usuario no es valido.")
    elif not validacion_pass(clave):
        messagebox.showwarning("Clave invalido", "La clave no es valida.")
    else:
        agregar_usuario(nombre_user, clave, opcion, respuesta)
        root.destroy()
        Ventana_principal()

def iniciar_sesion(nombre_user, clave, root):
    # Chequea si el usuario existe y si la clave ingresa coincide
    # Autor: Julen Gaumard

    usuario = buscar_usuario(nombre_user)

    if nombre_user == "" or clave == "":
        messagebox.showerror("Datos incompletos", "Complete los datos para continuar")
    elif not usuario: 
        messagebox.showwarning("Identificador inexistente o clave erronea", "Si no se encuentra registrado debe registrarse previamente o si olvidaste la clave presiona el botón recuperar clave")
    elif int(usuario[4]) > 2:
        messagebox.showerror("Atencion", "Usuario Bloqueado")
    elif usuario[1] == clave:
        root.destroy()
        Ventana_principal()
    else:
        messagebox.showwarning("Identificador inexistente o clave erronea", "Si no se encuentra registrado debe registrarse previamente o si olvidaste la clave presiona el botón recuperar clave")


def crear_ventana(nombre_ventana):
    # Crea una ventana generica, a la cual mediante otra funcion se le agregan los elementos necesarios
    # Autor: Julen Gaumard

    raiz = Tk()
    raiz.resizable(False,False)
    raiz.title(nombre_ventana)
    raiz.iconbitmap("icon.ico")
    style = ttk.Style(raiz)
    style.theme_use('vista')
    return raiz

def ventana_usuarios(root, opcion):
    # Crea la interfaz para el inicio de sesion
    # Autor: Julen Gaumard

    if opcion == 1:
        titulo = "Iniciar Sesion"
    else:
        titulo = "Crear Usuario"

    user_var = StringVar(root)
    clave_var = StringVar(root)
    opcion_var = StringVar(root)
    respuesta_var = StringVar(root)

    global_frame = ttk.Frame(root)

    ttk.Label(global_frame, text= titulo, font=("Arial", 20)).grid(row=0, column=0, pady=10, sticky="w", columnspan=2)
    
    ttk.Label(global_frame,text="Usuario:").grid(row=1, column=0, pady=5, sticky="w")
    ttk.Entry(global_frame,textvariable = user_var).grid(row=1, column=1, pady=5, sticky="e")

    ttk.Label(global_frame,text="Clave:").grid(row=3, column=0, pady=5, sticky="w")
    ttk.Entry(global_frame,textvariable = clave_var, show="*").grid(row=3, column=1, pady=5, sticky="e")

    if opcion == 2:
        options = obtener_preguntas()
        opcion_var.set(options[0]) 
        
        ttk.Label(global_frame,text="Pregunta:").grid(row=4, column=0, pady=5, sticky="w")
        ttk.OptionMenu(global_frame, opcion_var, *options).grid(row=4, column=1, pady=5, sticky="e")
        
        ttk.Label(global_frame,text="Respuesta:").grid(row=5, column=0, pady=5, sticky="w")
        ttk.Entry(global_frame,textvariable = respuesta_var).grid(row=5, column=1, pady=5, sticky="e")

        ttk.Button(global_frame, text="Crear Usuario", command = lambda : crear_usuario(user_var.get(), clave_var.get(), opcion_var.get(), respuesta_var.get(), root)).grid(row=9, column=1, pady=10, sticky="e")

    else:
        ttk.Button(global_frame, text="Olvide Clave", ).grid(row=9, column=0, pady=10, sticky="w")
        ttk.Button(global_frame, text="Ingresar", command = lambda : iniciar_sesion(user_var.get(), clave_var.get(), root)).grid(row=9, column=1, pady=10, sticky="e")

    global_frame.pack(padx=10)

def ventana_bienvenida(root):
    # Crea la interfaz de la pantalla de bienvenida
    # Autor: Julen Gaumard

    global_frame = ttk.Frame(root)

    ttk.Label(global_frame,text="Bienvenido!", font=("Arial", 20)).grid(row=0, column=0, padx=5, pady=5, sticky="w")
    ttk.Label(global_frame,text="A la aplicación de mensajes secretos del grupo Pala.").grid(row=1, column=0, padx=5, sticky="w")
    ttk.Label(global_frame,text="Para continuar presione continuar, de lo contrario cierre la ventana.").grid(row=2, column=0, padx=5, sticky="w")

    botones_frame = ttk.Frame(global_frame)
    ttk.Button(botones_frame, text="Crear Usuario", command = lambda : next_screen(root, 2)).grid(row=3, column=0, padx=5, pady=10, sticky="e")
    ttk.Button(botones_frame, text="Ingreso Usuario", command = lambda : next_screen(root, 1)).grid(row=3, column=1, padx=5, pady=10, sticky="e")
    botones_frame.grid(row=4, column=0, sticky="e")

    desarrollado_frame = ttk.Frame(global_frame)
    ttk.Label(desarrollado_frame,text="Construída por:", foreground="grey").grid(row=0, column=0, padx=5, sticky="w")
    ttk.Label(desarrollado_frame,text="Alessandro Perez", foreground="grey").grid(row=0, column=1, padx=5, sticky="w")
    ttk.Label(desarrollado_frame,text="Julen Gaumard", foreground="grey").grid(row=1, column=1, padx=5, sticky="w")
    ttk.Label(desarrollado_frame,text="Juan Pablo Dominguez Lucia", foreground="grey").grid(row=2, column=1, padx=5, sticky="w")
    ttk.Label(desarrollado_frame,text="Tomás Aprigliano", foreground="grey").grid(row=3, column=1, padx=5, sticky="w")
    
    desarrollado_frame.grid(row=5, column=0, sticky="w", columnspan=2)
    global_frame.pack(padx=10, pady=10)

def main():
    # Comienza la aplicacion, creando la ventana de bienvenida
    # Autor: Julen Gaumard
    root = crear_ventana("TP Grupal Parte 1 - Grupo: Pala")
    ventana_bienvenida(root)
    root.mainloop()

main()