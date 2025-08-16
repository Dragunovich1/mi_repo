# Importa el módulo tkinter, que proporciona las funciones para crear interfaces gráficas de usuario (GUI) en Python.
import tkinter as tk

# Importa el módulo tkinter.ttk, que proporciona widgets de estilo ttk para crear interfaces gráficas de usuario (GUI) en Python.
from tkinter import ttk

# Importa los módulos tkinter.filedialog, tkinter.simpledialog y tkinter.messagebox, que proporcionan funciones para trabajar con archivos, diálogos de entrada de usuario y cuadros de diálogo de mensajes en Python.
from tkinter import filedialog, simpledialog, messagebox

# Importa el módulo os, que proporciona funciones para trabajar con el sistema de archivos en Python.
import os

# Importa los modulos para manejo de wim
import subprocess

class ConfigApp:
    # Inicialización de la ventana principal
    def __init__(self, root):
        self.root = root
        self.root.title("DN Config - Herramienta para configuración de equipos - Tech Software Support")
        # Creación de frames para la interfaz
        self.frame_lateral = tk.Frame(self.root, bg="lightgray")
        self.frame_lateral.pack(side=tk.LEFT, fill=tk.Y)
        #Barra de estado
        self.barra_estado = tk.Label(self.root, text="Menú Principal", bd=0, relief=tk.FLAT, anchor=tk.W, bg="lightgray", fg="black")
        self.barra_estado.pack(side=tk.BOTTOM, fill=tk.X)
        #Frame central para contenido de las opciones
        self.frame_contenido = ttk.Frame(self.root, padding=10)
        self.frame_contenido.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        # Inicializa la ventana.
        self.inicializar_ventana()

    def inicializar_ventana(self):
        #Inicializa la ventana de la aplicación.
        # Obtiene el ancho y la altura de la pantalla.
        ancho_pantalla = self.root.winfo_screenwidth()
        alto_pantalla = self.root.winfo_screenheight()
        # Establece el tamaño de la ventana al 60% del ancho y alto de la pantalla.
        ancho_ventana = int(ancho_pantalla * 0.6)
        alto_ventana = int(alto_pantalla * 0.6)
        x_pos = (ancho_pantalla - ancho_ventana) // 2
        y_pos = (alto_pantalla - alto_ventana) // 2
        self.root.geometry(f"{ancho_ventana}x{alto_ventana}+{x_pos}+{y_pos}")
        # Establece el icono de la ventana.
        icono = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "dn.ico")
        self.root.iconbitmap(icono)
        # Crea la interfaz de usuario de la ventana.
        self.crear_interfaz()

    def crear_interfaz(self):
        #Crea la interfaz de usuario de la ventana.
        estilo_boton = {
            "relief": tk.FLAT,
            "width": 20,
            "bg": "lightgray",
            "activebackground": "gray",
        }
        # Crea la barra de menú.
        self.barra_menu = tk.Menu(self.root)
        self.root.config(menu=self.barra_menu)
        # Crea el menú Archivo.
        menu_archivo = tk.Menu(self.barra_menu, tearoff=0)
        menu_ayuda = tk.Menu(self.barra_menu, tearoff=0)
        # Crea el menú lateral, con botones sin borde, con hover de gris a gris oscuro
        opciones = ["Configuracion de S.O", "DNSeries", "Cineo/Procash Family", "Legacy Diebold", "Instructivos"]
        for opcion in opciones:
            estilo_boton["text"] = opcion
            estilo_boton["command"] = lambda opcion=opcion: self.mostrar_seccion(opcion)
            btn = tk.Button(self.frame_lateral, **estilo_boton)
            btn.pack(pady=5)
            btn.bind("<Enter>", self.cambiar_color)
            btn.bind("<Leave>", self.restaurar_color)
        # Crea el submenú Guardar registros.
        self.barra_menu.add_cascade(label="Archivo", menu=menu_archivo)
        submenu_guardar_logs = tk.Menu(menu_archivo, tearoff=0)
        submenu_guardar_logs.add_command(label="PBReport", command=lambda: self.guardar_reporte("PBReport"))
        submenu_guardar_logs.add_command(label="WNReport", command=lambda: self.guardar_reporte("WNReport"))
        submenu_guardar_logs.add_command(label="CCSupport", command=lambda: self.guardar_reporte("CCSupport"))
        submenu_guardar_logs.add_command(label="Support", command=lambda: self.guardar_reporte("Support"))
        submenu_guardar_logs.add_command(label="UDB", command=lambda: self.guardar_reporte("UDB"))
        submenu_guardar_logs.add_command(label="PNF", command=lambda: self.guardar_reporte("PNF"))
        submenu_guardar_logs.add_command(label="SBX", command=lambda: self.guardar_reporte("SBX"))
        submenu_guardar_logs.add_command(label="TPM", command=lambda: self.guardar_reporte("TPM"))
        submenu_guardar_logs.add_command(label="VersionInfo", command=lambda: self.guardar_reporte("VersionInfo"))
        submenu_guardar_logs.add_command(label="Trazas JAM", command=lambda: self.guardar_reporte("logs_jam"))
        submenu_guardar_logs.add_command(label="SilentDebug", command=lambda: self.guardar_reporte("SilentDebug"))
        submenu_guardar_logs.add_command(label="Eventos de Windows", command=lambda: self.guardar_reporte("WinEvt"))
        submenu_guardar_logs.add_command(label="Registro de Windows", command=lambda: self.guardar_reporte("RegExtract"))
        submenu_guardar_logs.add_command(label="Datos TCP/IP", command=lambda: self.guardar_reporte("tcpip"))
        #crea la cascada guardar logs
        menu_archivo.add_cascade(label="Guardar Logs", menu=submenu_guardar_logs)
        #crea las sub opciones de manejo de wim
        submenu_manjeo_wim = tk.Menu(menu_archivo, tearoff=0)
        submenu_manjeo_wim.add_command(label="Capturar WIM", command=lambda: self.funcion_protegida("Capturar WIM"))
        submenu_manjeo_wim.add_command(label="Deployar WIM", command=lambda: self.funcion_protegida("Deployar WIM"))
        submenu_manjeo_wim.add_command(label="Hacer SysPrep", command=lambda: self.funcion_protegida("Hacer SysPrep"))
        menu_archivo.add_cascade(label="Manejo de WIM", menu=submenu_manjeo_wim)
        #opcion salir
        menu_archivo.add_separator()
        menu_archivo.add_command(label="Salir", command=self.root.quit)
        #cascada ayuda y sus opciones
        self.barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)
        menu_ayuda.add_command(label="Mostrar ayuda", command=self.mostrar_ayuda)
        menu_ayuda.add_command(label="Acerca de", command=self.mostrar_acerca_de)

    def mostrar_seccion(self, seccion):
        #funcion de mostrar la seccion actual en barra de estado
        if self.barra_estado.cget("text") != seccion:
            self.actualizar_barra_estado(seccion)
            self.mostrar_contenido_seccion(seccion)

    def actualizar_barra_estado(self, texto):
        #funcion de actualizar la barra de estado
        self.barra_estado.config(text=texto)

    def cambiar_color(self, event):
        #funcion para el hover
        event.widget.config(bg="gray")

    def restaurar_color(self, event):
        #funcion para el hover
        event.widget.config(bg="lightgray")
        
    def mostrar_contenido_seccion(self, seccion):
        # limpia frame
        for widget in self.frame_contenido.winfo_children():
            widget.destroy()

        if seccion == "Configuracion de S.O":
            self.mostrar_configuracion_so()
        elif seccion == "DNSeries":
            self.mostrar_dn_series()
        elif seccion == "Cineo/Procash Family":
            self.mostrar_cineo_procash_family()
        elif seccion == "Legacy Diebold":
            self.mostrar_legacy_diebold()
        elif seccion == "Instructivos":
            self.mostrar_instructivos()
        elif seccion == "Capturar WIM":
            self.mostrar_capturar_wim()
        elif seccion == "Deployar WIM":
            self.mostrar_deployar_wim()
        elif seccion == "Hacer SysPrep":
            self.mostrar_hacer_sysprep()
        # agregar secciones aqui arriba, recordar reemplazar por diccionario para no tener tantos elif

    def mostrar_configuracion_so(self):
        label = tk.Label(self.frame_contenido, text="Contenido de la sección 'Configuracion de S.O'")
        label.pack()

    def mostrar_dn_series(self):
        label = tk.Label(self.frame_contenido, text="Contenido de la sección 'DNSeries'")
        label.pack()

    def mostrar_cineo_procash_family(self):
        label = tk.Label(self.frame_contenido, text="Contenido de la sección 'Cineo/Procash Family'")
        label.pack()

    def mostrar_legacy_diebold(self):
        label = tk.Label(self.frame_contenido, text="Contenido de la sección 'Legacy Diebold'")
        label.pack()

    def mostrar_instructivos(self):
        label = tk.Label(self.frame_contenido, text="Contenido de la sección 'Instructivos'")
        label.pack()

    def mostrar_capturar_wim(self):
        label = tk.Label(self.frame_contenido, text="Contenido de la sección 'Capturar WIM'")
        label.pack()

    def mostrar_deployar_wim(self):
        label = tk.Label(self.frame_contenido, text="Contenido de la sección 'Deployar WIM'")
        label.pack()

    def mostrar_hacer_sysprep(self):
        label = tk.Label(self.frame_contenido, text="Contenido de la sección 'Hacer SysPrep'")
        label.pack()

    # agregar mas funciones aqui arriba jeje

    def guardar_reporte(self, tipo_reporte):
        ruta_archivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt")])
        if ruta_archivo:
            contenido = ""  # solo a modo de esqueleto de seccion.
            with open(ruta_archivo, "w") as archivo:
                archivo.write(contenido)

    def funcion_protegida(self, accion):
        contraseña = simpledialog.askstring("Función Protegida", "Ingrese la contraseña:", show='*', parent=self.root)
        if contraseña == "TechSoft2023":
            self.mostrar_contenido_seccion(accion)
            # Agrega aquí el código de la función protegida si es necesario
        elif contraseña is not None:  # Caso negativo, contraseña invalida
            messagebox.showerror("Error", "Contraseña incorrecta")
            self.mostrar_seccion(self.barra_estado.cget("text"))  # Restaurar la sección actual

    def mostrar_ayuda(self):
        pass  # agregar ventana emergente con ayuda respecto a la aplicación

    def mostrar_acerca_de(self):
        pass  # agregar ventana de acerca de con creditos y demas

def main():
    root = tk.Tk()
    app = ConfigApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
