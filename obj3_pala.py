from tkinter import messagebox, StringVar
from tkinter import ttk, Tk
from obj1_pala import cifrar_cesar
from cifrado_atbash import cifrar_atbash

def ventana_error(mensaje, titulo):
    messagebox.showerror(titulo, mensaje)

def chequear_datos(text, clave):
    valido = True

    if text == "":
        valido = False 
        ventana_error("Ingrese un mensaje para procesar", "Datos Incompletos")
    elif clave == "":
        valido = False 
        ventana_error("Ingrese una clave para procesar", "Datos Incompletos")
    elif not clave.isnumeric():
        valido = False 
        ventana_error("La clave debe ser un numero", "Datos Incorrectos")

    return valido


def ejecutar_cezar(text, clave, result, reverse = False):
    if chequear_datos(text, clave):

        if not reverse:
            cifrado = cifrar_cesar(text, int(clave))
        else:
            cifrado = cifrar_cesar(text, -1 * int(clave))

        result.set(cifrado)

def ejecutar_atbash(text, result):
    if chequear_datos(text, "0"):
        cifrado = cifrar_atbash(text)
        result.set(cifrado)

def crear_ventana():
    raiz = Tk()
    # raiz.geometry("500x300")
    raiz.resizable(False,False)
    raiz.title("TP Grupal Parte 1 - Grupo: Pala")
    raiz.iconbitmap("icon.ico")
    style = ttk.Style(raiz)
    style.theme_use('vista')
    return raiz

def menu_screen():
    root.destroy()

    root_2 = crear_ventana()
    ventana_menu(root_2)
    root_2.mainloop()

def ventana_menu(root):
    global_frame = ttk.Frame(root)

    text_var = StringVar(root)
    clave_var = StringVar(root)
    result_var = StringVar(root)

    ttk.Label(global_frame,text="1. Ingrese un mensaje:", font=("Arial", 14)).grid(row=0, column=0, pady=5, sticky="w")
    ttk.Entry(global_frame, textvariable=text_var).grid(row=1, column=0, columnspan=2, ipadx=105, padx=3)

    ttk.Separator(global_frame, orient='horizontal').grid(row=2, column=0, ipady=10)
    ttk.Label(global_frame,text="2. Seleccione una opcion:", font=("Arial", 14)).grid(row=3, column=0, pady=5, sticky="w")
    
    cezar_frame = ttk.Frame(global_frame)
    ttk.Label(cezar_frame,text="Cifrado César", font=("Arial", 12)).grid(row=0, column=0, pady=5, sticky="w", columnspan=4)
    ttk.Label(cezar_frame,text="Clave:", font=("Arial", 10)).grid(row=1, column=0, pady=5, sticky="w")
    ttk.Entry(cezar_frame, textvariable=clave_var).grid(row=1, column=1, padx=3, sticky="w")
    ttk.Button(cezar_frame, text="Cifrar", command = lambda : ejecutar_cezar(text_var.get(), clave_var.get(), result_var)).grid(row=1, column=2, padx=5, sticky="e")
    ttk.Button(cezar_frame, text="Descifrar", command = lambda : ejecutar_cezar(text_var.get(), clave_var.get(), result_var, True)).grid(row=1, column=4, padx=5, sticky="e")
    cezar_frame.grid(row=4, column=0, sticky="w", pady=10)
     
    atbash_frame = ttk.Frame(global_frame)
    ttk.Label(atbash_frame,text="Cifrado Atbash", font=("Arial", 12)).grid(row=0, column=0, pady=5, sticky="w", columnspan=4)
    ttk.Button(atbash_frame, text="Cifrar", command = lambda : ejecutar_atbash(text_var.get(), result_var)).grid(row=1, column=0, sticky="e")
    ttk.Button(atbash_frame, text="Descifrar", command = lambda : ejecutar_atbash(text_var.get(), result_var)).grid(row=1, column=1, padx=5, sticky="e")
    atbash_frame.grid(row=5, column=0, sticky="w")
     
    ttk.Separator(global_frame, orient='horizontal').grid(row=6, column=0, ipady=10)
    ttk.Label(global_frame,text="3. Resultado:", font=("Arial", 14)).grid(row=7, column=0, pady=5, sticky="w")
    ttk.Label(global_frame,text="", font=("Arial", 10, "italic"), textvariable = result_var).grid(row=8, column=0, pady=5, sticky="w")
    result_var.set("El resultado se mostrara aqui.")

    global_frame.pack(padx=15, pady=15)

def ventana_bienvenida(root):
    global_frame = ttk.Frame(root)

    ttk.Label(global_frame,text="Bienvenido!", font=("Arial", 20)).grid(row=0, column=0, padx=5, pady=5, sticky="w")
    ttk.Label(global_frame,text="A la aplicación de mensajes secretos del grupo Pala.").grid(row=1, column=0, padx=5, sticky="w")
    ttk.Label(global_frame,text="Para continuar presione continuar, de lo contrario cierre la ventana.").grid(row=2, column=0, padx=5, sticky="w")

    ttk.Button(global_frame, text="Continuar", command = menu_screen).grid(row=3, column=0, padx=5, pady=10, sticky="e")

    desarrollado_frame = ttk.Frame(global_frame)
    ttk.Label(desarrollado_frame,text="Construída por:", foreground="grey").grid(row=0, column=0, padx=5, sticky="w")
    ttk.Label(desarrollado_frame,text="Julen Gaumard", foreground="grey").grid(row=0, column=1, padx=5, sticky="w")
    ttk.Label(desarrollado_frame,text="Tomas aprigliano", foreground="grey").grid(row=1, column=1, padx=5, sticky="w")
    ttk.Label(desarrollado_frame,text="Guido Tiscornia", foreground="grey").grid(row=2, column=1, padx=5, sticky="w")
    
    desarrollado_frame.grid(row=5, column=0, sticky="w", columnspan=2)
    global_frame.pack(padx=10, pady=10)


root = crear_ventana()
ventana_bienvenida(root)
root.mainloop()