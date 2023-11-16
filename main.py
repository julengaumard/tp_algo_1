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
def boton_cesar_cifrado(texto,clave,resultado,boton):

    error = buscar_error_cesar(texto,clave)
    if error == False:
        if boton == 1:
            cifrar = cifrar_cesar(texto,int(clave))

            resultado.set(cifrar)

        elif boton == 2:
            negativo = -int(clave)
            cifrar = cifrar_cesar(texto,negativo)

            resultado.set(cifrar)

#Se ejecuta al presionar el boton de descifrado Cesar

#--------------------------Ventana principal-----------------------------
def Ventana_principal():
    #Parametros iniciales de la ventana principal

    Ventana = crear_raiz("Cifrado y envío de mensajes")
    
    Frame_principal = ttk.Frame(Ventana)

    var_texto = StringVar(Ventana)
    var_resultado = StringVar(Ventana)
    var_clave = StringVar(Ventana)

    Ingreso_mensaje = ttk.Label(Frame_principal,text="\nIngrese mesaje para decifrar:", font= ("bahnschrift",14,"underline")).grid(row=0,sticky = "w")
    cuadro_de_ingreso_mensaje = ttk.Entry(Frame_principal,textvariable=var_texto, width=50).grid(row=1,column=0,padx=5,pady=10)

    ttk.Separator(Frame_principal, orient='horizontal').grid(row=3,pady=10)

    #Apartado para el cifrado cesar

    frame_cesar = ttk.Frame(Frame_principal)
    frame_cesar.grid(row=4,column=0,sticky="w")


    Titulo_cesar = ttk.Label(frame_cesar,text="Cifrado cesar", font= ("bahnschrift",11,"underline")).grid(row=1,sticky = "w",columnspan=2)
    texto_aclaracion = ttk.Label(frame_cesar,text="Clave:", font= ("bahnschrift",10)).grid(row=2,sticky = "w",padx=10,pady=10)
    cuadro_de_ingreso_clave = ttk.Entry(frame_cesar,width=10,textvariable= var_clave).grid(row=2,column=1,pady=10)
    boton_cifrar_cesar = ttk.Button(frame_cesar, text="Cifrar",width=8,command= lambda: boton_cesar_cifrado(var_texto.get(),var_clave.get(),var_resultado,1)).grid(row=2,column=2,padx=10,pady=10)
    boton_descifrar_cesar = ttk.Button(frame_cesar, text="Descifrar",width=8,command= lambda: boton_cesar_cifrado(var_texto.get(),var_clave.get(),var_resultado,2)).grid(row=2,column=3,pady=10)

    ttk.Separator(Frame_principal, orient='horizontal').grid(row=5,pady=10)

    #Apartado para el cifrado atbash

    frame_atbash = ttk.Frame(Frame_principal)
    frame_atbash.grid(row=6,column=0,sticky="w")

    Titulo_atbash = ttk.Label(frame_atbash,text="Cifrado atbash", font= ("bahnschrift",11,"underline")).grid(row=1,sticky = "w",columnspan=2)
    boton_cifrar_atbash = ttk.Button(frame_atbash, text="Cifrar",width=8,command= lambda : boton_atbash(var_texto.get(),var_resultado)).grid(row=2,column=0,padx=10,pady=10)
    boton_descifrar_atbash = ttk.Button(frame_atbash, text="Descifrar",width=8,command= lambda : boton_atbash(var_texto.get(),var_resultado)).grid(row=2,column=1,pady=10)

    ttk.Separator(Frame_principal, orient='horizontal').grid(row=7,pady=10)

    #Apartado para el Resultado
    frame_resul = ttk.Frame(Frame_principal)
    frame_resul.grid(row=8,column=0,sticky="w")

    Titulo_resultado = ttk.Label(frame_resul,text="Resultado:", font= ("bahnschrift",14,"underline")).grid(row=0,sticky = "w")
    Resultado = ttk.Label(frame_resul, font=("bahnschrift", 10), textvariable = var_resultado).grid(row=1, column=0, padx = 10, pady=5, sticky="w") 
    var_resultado.set("El resultado se mostrara aqui.")

    ttk.Separator(Frame_principal, orient='horizontal').grid(row=9,pady=5)

    #Envio de mensajes
    Envio_cifrado_cesar = ttk.Button(Frame_principal,text="Enviar mensaje Cifrado Cesar",width=30).grid(row=10,padx=10,pady=5)
    Envio_cifrado_atbash= ttk.Button(Frame_principal,text="Enviar mensaje Cifrado Atbash",width=30).grid(row=11,padx=10,pady=5)

    Frame_principal.pack(padx=10, pady=10)
    Ventana.mainloop()


#--------------------------Ventana de bienvenida-----------------------------

def next_screen(raiz, opcion):
    # Segun el numero de opcion, crea la ventana correspondiente.
    # Autor: Julen Gaumard

    if opcion == 1:
        raiz.destroy()
        titulo = "Identificación para acceso"

        raiz_nueva = crear_raiz(titulo)
        ventana_usuarios(raiz_nueva, opcion)

    elif opcion == 2:
        raiz.destroy()
        titulo = "Creacion de usuario"
    
        raiz_nueva = crear_raiz(titulo)
        ventana_usuarios(raiz_nueva, opcion)
    
    elif opcion == 3:
        titulo = "Enviar mensaje Cesar"
        raiz_nueva = crear_raiz(titulo)
    
    elif opcion == 4:
        titulo = "Enviar mensaje Atbash"
        raiz_nueva = crear_raiz(titulo)



def crear_usuario(nombre_user, clave, opcion, respuesta, raiz):

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
        raiz.destroy()
        Ventana_principal()

def iniciar_sesion(nombre_user, clave, raiz):
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
        raiz.destroy()
        Ventana_principal()
    else:
        messagebox.showwarning("Identificador inexistente o clave erronea", "Si no se encuentra registrado debe registrarse previamente o si olvidaste la clave presiona el botón recuperar clave")


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

def ventana_usuarios(raiz, opcion):
    # Crea la interfaz para el inicio de sesion
    # Autor: Julen Gaumard

    if opcion == 1:
        titulo = "Iniciar Sesion"
    else:
        titulo = "Crear Usuario"

    user_var = StringVar(raiz)
    clave_var = StringVar(raiz)
    opcion_var = StringVar(raiz)
    respuesta_var = StringVar(raiz)

    frame_global = ttk.Frame(raiz)

    ttk.Label(frame_global, text= titulo, font=("Arial", 20)).grid(row=0, column=0, pady=10, sticky="w", columnspan=2)
    
    ttk.Label(frame_global,text="Usuario:").grid(row=1, column=0, pady=5, sticky="w")
    ttk.Entry(frame_global,textvariable = user_var).grid(row=1, column=1, pady=5, sticky="e")

    ttk.Label(frame_global,text="Clave:").grid(row=3, column=0, pady=5, sticky="w")
    ttk.Entry(frame_global,textvariable = clave_var, show="*").grid(row=3, column=1, pady=5, sticky="e")

    if opcion == 2:
        opciones = obtener_preguntas()
        opcion_var.set(opciones[0]) 
        
        ttk.Label(frame_global,text="Pregunta:").grid(row=4, column=0, pady=5, sticky="w")
        ttk.OptionMenu(frame_global, opcion_var, *opciones).grid(row=4, column=1, pady=5, sticky="e")
        
        ttk.Label(frame_global,text="Respuesta:").grid(row=5, column=0, pady=5, sticky="w")
        ttk.Entry(frame_global,textvariable = respuesta_var).grid(row=5, column=1, pady=5, sticky="e")

        ttk.Button(frame_global, text="Crear Usuario", command = lambda : crear_usuario(user_var.get(), clave_var.get(), opcion_var.get(), respuesta_var.get(), raiz)).grid(row=9, column=1, pady=10, sticky="e")

    else:
        ttk.Button(frame_global, text="Olvide Clave", ).grid(row=9, column=0, pady=10, sticky="w")
        ttk.Button(frame_global, text="Ingresar", command = lambda : iniciar_sesion(user_var.get(), clave_var.get(), raiz)).grid(row=9, column=1, pady=10, sticky="e")

    frame_global.pack(padx=10)


def ventana_bienvenida(raiz):
    # Crea la interfaz de la pantalla de bienvenida
    # Autor: Julen Gaumard

    frame_global = ttk.Frame(raiz)

    ttk.Label(frame_global,text="Bienvenido!", font=("Arial", 20)).grid(row=0, column=0, padx=5, pady=5, sticky="w")
    ttk.Label(frame_global,text="A la aplicación de mensajes secretos del grupo Pala.").grid(row=1, column=0, padx=5, sticky="w")
    ttk.Label(frame_global,text="Para continuar presione continuar, de lo contrario cierre la ventana.").grid(row=2, column=0, padx=5, sticky="w")

    botones_frame = ttk.Frame(frame_global)
    ttk.Button(botones_frame, text="Crear Usuario", command = lambda : next_screen(raiz, 2)).grid(row=3, column=0, padx=5, pady=10, sticky="e")
    ttk.Button(botones_frame, text="Ingreso Usuario", command = lambda : next_screen(raiz, 1)).grid(row=3, column=1, padx=5, pady=10, sticky="e")
    botones_frame.grid(row=4, column=0, sticky="e")

    desarrollado_frame = ttk.Frame(frame_global)
    ttk.Label(desarrollado_frame,text="Construída por:", foreground="grey").grid(row=0, column=0, padx=5, sticky="w")
    ttk.Label(desarrollado_frame,text="Alessandro Perez", foreground="grey").grid(row=0, column=1, padx=5, sticky="w")
    ttk.Label(desarrollado_frame,text="Julen Gaumard", foreground="grey").grid(row=1, column=1, padx=5, sticky="w")
    ttk.Label(desarrollado_frame,text="Juan Pablo Dominguez Lucia", foreground="grey").grid(row=2, column=1, padx=5, sticky="w")
    
    desarrollado_frame.grid(row=5, column=0, sticky="w", columnspan=2)
    frame_global.pack(padx=10, pady=10)

    raiz.mainloop()

def main():
    # Comienza la aplicacion, creando la ventana de bienvenida
    # Autor: Julen Gaumard
    raiz = crear_raiz("TP Grupal Parte 1 - Grupo: Pala")
    ventana_bienvenida(raiz)

main()