import tkinter as tk

# Variable global para la barra de estado
barra_estado = None

# Lista para llevar el registro de las opciones seleccionadas
opciones_seleccionadas = []

# Estructura de árbol para las opciones del menú
opciones_arbol = {
    "Inicio": {
        "Funcion": None,
        "Subopciones": {}
    },
    "Configuracion de S.O": {
        "Funcion": None,
        "Subopciones": {
            "Configuracion TCP/IP": None,
            "Configuracion de Proxy": None
        }
    },
    "DNSeries": {
        "Funcion": None,
        "Subopciones": {
            "Opcion 1": None,
            "Opcion 2": None
        }
    },
    "Cineo/Procash Family": {
        "Funcion": None,
        "Subopciones": {
            "Opcion A": None,
            "Opcion B": None
        }
    },
    "Legacy Diebold": {
        "Funcion": None,
        "Subopciones": {
            "Opcion X": None,
            "Opcion Y": None
        }
    }
}

# Función global para actualizar la barra de estado
def actualizar_barra_estado(texto):
    global opciones_seleccionadas
    if texto == "Inicio":
        opciones_seleccionadas = []
    elif texto in opciones_seleccionadas:
        opciones_seleccionadas = opciones_seleccionadas[:opciones_seleccionadas.index(texto) + 1]
    else:
        opciones_seleccionadas.append(texto)
    texto_barra = " -> ".join(opciones_seleccionadas)
    barra_estado.config(text=texto_barra)

# Funciones para mostrar el contenido de las opciones del menú (a completar con tu código)
def mostrar_menu_principal():
    # Aquí colocarías el código para mostrar el menú principal
    print("Mostrando menú principal")
    actualizar_barra_estado("Inicio")

def mostrar_configuracion_de_so():
    # Aquí colocarías el código para mostrar la configuración del S.O
    print("Mostrando configuracion de S.O")
    actualizar_barra_estado("Configuración de S.O")

# Resto de funciones para mostrar subopciones (a completar con tu código)

# Función para mostrar el contenido de las subopciones
def mostrar_contenido(opcion):
    global frame_opciones
    frame_opciones.pack_forget()
    frame_opciones = tk.Frame(frame_contenido, bg="white")
    frame_opciones.pack(fill=tk.BOTH, expand=True)

    subopciones = opciones_arbol
    for subopcion in opciones_seleccionadas[1:]:
        subopciones = subopciones[subopcion]["Subopciones"]

    if subopciones:
        for subopcion in subopciones:
            btn_subopcion = tk.Button(frame_opciones, text=subopcion, relief=tk.FLAT, bg="lightgray",
                                      activebackground="gray", width=20, command=lambda opt=subopcion: mostrar_subopcion(opt))
            btn_subopcion.pack(pady=5)
    else:
        # Aquí deberías mostrar el contenido específico de la opción seleccionada
        # Por ejemplo, puedes utilizar etiquetas, campos de entrada, etc.
        pass

def mostrar_subopcion(subopcion):
    global opciones_seleccionadas
    opciones_seleccionadas.append(subopcion)
    actualizar_barra_estado(subopcion)
    mostrar_contenido(subopcion)

# Función para crear y mostrar la ventana principal
def crear_ventana_principal():
    ventana = tk.Tk()
    ventana.title("DN Config - Herramienta para configuracion de equipos")

    # Obtener las dimensiones de la pantalla
    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()

    # Establecer las dimensiones de la ventana
    ancho_ventana = int(ancho_pantalla * 0.6)  # 60% del ancho de la pantalla
    alto_ventana = int(alto_pantalla * 0.6)    # 60% del alto de la pantalla
    x_pos = (ancho_pantalla - ancho_ventana) // 2
    y_pos = (alto_pantalla - alto_ventana) // 2
    ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x_pos}+{y_pos}")

    # Establecer el estilo para los botones
    estilo_boton = {
        "relief": tk.FLAT,  # Eliminar el borde
        "width": 20,        # Ancho fijo para todos los botones
        "bg": "lightgray",  # Color de fondo normal
        "activebackground": "gray",  # Color de fondo cuando el cursor pasa por encima
    }

    # Crear la barra lateral con los botones
    barra_lateral = tk.Frame(ventana, bg="lightgray")
    barra_lateral.pack(side=tk.LEFT, fill=tk.Y)

    # Botón de inicio para ir al menú principal
    estilo_boton["text"] = "Inicio"
    estilo_boton["command"] = mostrar_menu_principal
    btn_inicio = tk.Button(barra_lateral, **estilo_boton)
    btn_inicio.pack(pady=5)

    # Botones para las diferentes secciones
    opciones = ["Configuracion de S.O", "DNSeries", "Cineo/Procash Family", "Legacy Diebold"]
    for opcion in opciones:
        estilo_boton["text"] = opcion
        estilo_boton["command"] = lambda opt=opcion: mostrar_contenido(opt)
        btn = tk.Button(barra_lateral, **estilo_boton)
        btn.pack(pady=5)

    # Crear la barra de estado (label sin border y mismo color que la barra lateral)
    global barra_estado
    barra_estado = tk.Label(ventana, text="Inicio", bd=0, relief=tk.FLAT, anchor=tk.W, bg="lightgray", fg="black")
    barra_estado.pack(side=tk.BOTTOM, fill=tk.X)

    global frame_contenido
    frame_contenido = tk.Frame(ventana)
    frame_contenido.pack(fill=tk.BOTH, expand=True)

    global frame_opciones
    frame_opciones = tk.Frame(frame_contenido, bg="white")
    frame_opciones.pack(fill=tk.BOTH, expand=True)

    ventana.mainloop()

# Crear y mostrar la ventana principal
crear_ventana_principal()
