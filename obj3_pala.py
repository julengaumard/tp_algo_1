
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

#---------------------------Interfaz Gradica------------------------------
from tkinter import * 
from tkinter import ttk
from tkinter import messagebox

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

    ventana2 = crear_ventana()

    # ventana2 = Tk()
    # ventana2.title("TP Grupal Parte 1 - Grupo: Pala")
    # ventana2.iconbitmap("icon.ico")
    # ventana2.resizable(0,0)
    # estilo = ttk.Style(ventana2)
    # estilo.theme_use("vista")
    # ventana2.config(relief="groove",bd = 10)

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

def menu_screen():
    # Destruye la ventana de bienvenida y crea la ventana principal
    # Autor: Julen Gaumard

    root.destroy()
    Ventana_principal()

def crear_ventana():
    # Crea una ventana generica, a la cual mediante otra funcion se le agregan los elementos necesarios
    # Autor: Julen Gaumard

    raiz = Tk()
    raiz.resizable(False,False)
    raiz.title("TP Grupal Parte 1 - Grupo: Pala")
    raiz.iconbitmap("icon.ico")
    style = ttk.Style(raiz)
    style.theme_use('vista')
    return raiz

def ventana_bienvenida(root):
    # Crea la interfaz de la pantalla de bienvenida
    # Autor: Julen Gaumard

    global_frame = ttk.Frame(root)

    ttk.Label(global_frame,text="Bienvenido!", font=("Arial", 20)).grid(row=0, column=0, padx=5, pady=5, sticky="w")
    ttk.Label(global_frame,text="A la aplicación de mensajes secretos del grupo Pala.").grid(row=1, column=0, padx=5, sticky="w")
    ttk.Label(global_frame,text="Para continuar presione continuar, de lo contrario cierre la ventana.").grid(row=2, column=0, padx=5, sticky="w")

    ttk.Button(global_frame, text="Continuar", command = menu_screen).grid(row=3, column=0, padx=5, pady=10, sticky="e")

    desarrollado_frame = ttk.Frame(global_frame)
    ttk.Label(desarrollado_frame,text="Construída por:", foreground="grey").grid(row=0, column=0, padx=5, sticky="w")
    ttk.Label(desarrollado_frame,text="Alessandro Perez", foreground="grey").grid(row=0, column=1, padx=5, sticky="w")
    ttk.Label(desarrollado_frame,text="Guido Tiscornia", foreground="grey").grid(row=1, column=1, padx=5, sticky="w")
    ttk.Label(desarrollado_frame,text="Julen Gaumard", foreground="grey").grid(row=2, column=1, padx=5, sticky="w")
    ttk.Label(desarrollado_frame,text="Tomás Aprigliano", foreground="grey").grid(row=3, column=1, padx=5, sticky="w")
    
    desarrollado_frame.grid(row=5, column=0, sticky="w", columnspan=2)
    global_frame.pack(padx=10, pady=10)

root = crear_ventana()
ventana_bienvenida(root)
root.mainloop()