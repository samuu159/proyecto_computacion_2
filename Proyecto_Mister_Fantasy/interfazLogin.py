import tkinter as tk
import csv
import hashlib
import re
from tkinter import ttk


ruta_archivo_usuarios = './Data/usuarios.csv'
#Leer datos de usuarios registrados
def leer_datos_usuarios(ruta_archivo_usuarios):
    with open(ruta_archivo_usuarios, mode='r', encoding='utf-8-sig') as archivo:
        lector_csv = csv.DictReader(archivo)
        return list(lector_csv)
    
#Commprobar si el correo tiene el formato valido
def es_correo_valido(correo):
    patron = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
    if re.match(patron, correo):
        return True
    return False
#Verificar que esten todos los campos
def validar_entrada(correo, contraseña, nombre, equipo):
    if not correo or not contraseña or not nombre or not equipo:
        return False, "Todos los campos son obligatorios."
    if not es_correo_valido(correo):
        return False, "El correo electrónico no es válido."
    return True, ""  

#Creacion de ventana registro, pasamos la ventana_login como parametro para poder abrirla
def ventana_registro(ventana_login):
    # Ocultar la ventana de login, en lugar de destruirla
    ventana_login.withdraw()
    ventana_registro = tk.Toplevel()
    ventana_registro.title("Registro de Usuario")
    ventana_registro.geometry("800x600")
    # Cabecera
    cabecera = tk.Label(ventana_registro, text="Regístrate con tus credenciales de MrFantasy", font=("Helvetica", 14))
    cabecera.pack(pady=10)
    
    # Campos para ingresar datos de usuario
    etiqueta_correo = tk.Label(ventana_registro, text="Correo Electrónico:")
    entrada_correo = tk.Entry(ventana_registro, width=20)
    etiqueta_contraseña = tk.Label(ventana_registro, text="Contraseña:")
    entrada_contraseña = tk.Entry(ventana_registro, width=20, show="*")
    etiqueta_verificar_contraseña = tk.Label(ventana_registro, text="Verificar Contraseña:")
    entrada_verificar_contraseña = tk.Entry(ventana_registro, width=20, show="*")
    etiqueta_nombre = tk.Label(ventana_registro, text="Nombre:")
    entrada_nombre = tk.Entry(ventana_registro, width=20)
    etiqueta_equipo = tk.Label(ventana_registro, text="Equipo Favorito:")
    entrada_equipo = tk.Entry(ventana_registro, width=20)

    # Empaquetar los widgets
    etiqueta_correo.pack()
    entrada_correo.pack()
    etiqueta_contraseña.pack()
    entrada_contraseña.pack()
    etiqueta_verificar_contraseña.pack()
    entrada_verificar_contraseña.pack() 
    etiqueta_nombre.pack()
    entrada_nombre.pack()
    etiqueta_equipo.pack()
    entrada_equipo.pack()
    
    def registro_exitoso():
        ventana_registro.destroy()
        ventana_login.deiconify()  # Muestra nuevamente la ventana de login
        
    def confirmar_registro():
        correo = entrada_correo.get()
        contraseña = entrada_contraseña.get()
        verificar_contraseña = entrada_verificar_contraseña.get()
        nombre = entrada_nombre.get()
        equipo = entrada_equipo.get()

        valido, mensaje = validar_entrada(correo, contraseña, nombre, equipo)
        if valido:
            if contraseña == verificar_contraseña:
                guardar_usuario(correo, contraseña, nombre, equipo)
            else:
                tk.messagebox.showerror("Error", "Las contraseñas no coinciden.")
        else:
            tk.messagebox.showerror("Error", mensaje)


     
    def cerrar_ventana_registro():
        ventana_registro.destroy()
        ventana_login.deiconify()  # Muestra nuevamente la ventana de login

    ventana_registro.protocol("WM_DELETE_WINDOW", cerrar_ventana_registro)
    
    
    def guardar_usuario(correo, contraseña, nombre, equipo):
        # Hashear contraseña para mayor seguridad del usuario
        contraseña_hash = hash_contraseña(contraseña)
        nuevo_usuario = {'correo': correo, 'contraseña': contraseña_hash, 'nombre': nombre, 'equipo_favorito': equipo}
        with open(ruta_archivo_usuarios, mode='a', newline='', encoding='utf-8') as archivo:
            escritor_csv = csv.DictWriter(archivo, fieldnames=['correo', 'contraseña', 'nombre', 'equipo_favorito'])
            escritor_csv.writerow(nuevo_usuario)
        registro_exitoso()  # Llamar a registro_exitoso después de guardar el usuario
        
    boton_confirmar_registro = tk.Button(ventana_registro, text="Confirmar Registro", command=confirmar_registro)
    boton_confirmar_registro.pack()
    
    
#Creación de ventana login.
def ventana_login():
    ventana_login = tk.Tk()
    ventana_login.title("Login")
    ventana_login.geometry("800x600")
    encabezado_login = tk.Label(ventana_login, text="PREDITECH INSIGHTS", bg="green2", fg="black", font=("Georgia", 16))
    encabezado_login.pack(fill="x")
    # Campos para ingresar correo y contraseña
    etiqueta_correo = tk.Label(ventana_login, text="Correo Electrónico:")
    entrada_correo = tk.Entry(ventana_login, width=20)
    etiqueta_contraseña = tk.Label(ventana_login, text="Contraseña:")
    entrada_contraseña = tk.Entry(ventana_login, width=20, show="*")

    etiqueta_correo.pack()
    entrada_correo.pack()
    etiqueta_contraseña.pack()
    entrada_contraseña.pack()

    boton_login = tk.Button(ventana_login, text="Iniciar Sesión", command=lambda: verificar_credenciales(entrada_correo.get(), entrada_contraseña.get(), ventana_login))
    boton_login.pack()
    
    def abrir_ventana_registro():
        ventana_login.withdraw()  # Esconde la ventana de login
        ventana_registro(ventana_login)
        
    boton_registro = tk.Button(ventana_login, text="Registrarse", command=abrir_ventana_registro)
    boton_registro.pack()
    
    ventana_login.mainloop()
    
#Funcion que hashea contraseña    
def hash_contraseña(contraseña):
    return hashlib.sha256(contraseña.encode()).hexdigest()   
#Verificar credenciales para abrir ventana principal
def verificar_credenciales(correo, contraseña, ventana_login):
    usuarios = leer_datos_usuarios(ruta_archivo_usuarios)
    contraseña_hash = hash_contraseña(contraseña)  # Calcula el hash de la contraseña

    for usuario in usuarios:
        if usuario['correo'] == correo and usuario['contraseña'] == contraseña_hash:
            crear_ventana_principal()  # Abre la ventana principal
            ventana_login.withdraw()  # Oculta la ventana de login
            return

    tk.messagebox.showerror("Error", "Credenciales incorrectas")

    
       
# Función para leer los datos desde un archivo CSV
def leer_datos_csv(ruta_archivo):
    with open(ruta_archivo, mode='r', encoding='utf-8') as archivo:
        lector_csv = csv.DictReader(archivo)
        return list(lector_csv)
    
def mostrar_datos_csv_en_lienzo(ruta_csv):
    # Limpiar cualquier información anterior en el lienzo
    lienzo_jugadores_mercado.delete("all")
    
    # Leer los datos del archivo CSV correspondiente
    datos_csv = leer_datos_csv(ruta_csv)
    
    # Mostrar los datos de los jugadores en el lienzo
    for i, jugador in enumerate(datos_csv):
        texto_jugador = "{} {}, Equipo: {}, Valor: {}, Valor predicción: {}, Puntos Totales: {}, Puntos Predicción: {}".format(
            jugador['nombre'], jugador['apellido'], jugador['nombre_equipo'], 
            jugador['valor'], jugador['pred_valor'], jugador['puntos_totales'], jugador['pred_puntos_siguiente_jornada']
        )
        lienzo_jugadores_mercado.create_text(10, 10 + i * 30, anchor='nw', text=texto_jugador)

# Función para mostrar los datos de los jugadores en la caja de Mercado
def mostrar_datos_mercado(opcion):
    # Limpiar la caja de Jugadores en Mercado de datos anteriores
    for widget in caja_jugadores_mercado.winfo_children():
        widget.destroy()
    
    # Determinar qué archivo CSV cargar según la opción seleccionada
    if opcion == "Random Forest":
        ruta_csv = './Data/mercado_predicciones_forest.csv'
    elif opcion == "KNN":
        ruta_csv = './Data/mercado_predicciones_knn.csv'
    elif opcion == "Decision Tree":
        ruta_csv = './Data/mercado_predicciones_arbol.csv'
    else:
        return  # Salir si no se seleccionó una opción válida
    
    # Leer los datos del archivo CSV correspondiente
    datos_csv = leer_datos_csv(ruta_csv)
    
    # Mostrar los datos de los jugadores en la caja de Jugadores en Mercado
    for i, fila in enumerate(datos_csv):
        texto_fila = ""
        for clave, valor in fila.items():
            texto_fila += f"{clave}: {valor}, "
        label_fila = tk.Label(caja_jugadores_mercado, text=texto_fila, bg="white")
        label_fila.pack(anchor='w')  # Alineación a la izquierda
    
    # Actualizar la región de desplazamiento en función de los datos
    caja_jugadores_mercado.update_idletasks()
    caja_jugadores_mercado.config(scrollregion=caja_jugadores_mercado.bbox("all"))  

def mostrar_random_forest():
    mostrar_datos_csv_en_lienzo('./Data/mercado_predicciones_forest.csv')
    lienzo_jugadores_mercado.update_idletasks()
    lienzo_jugadores_mercado.config(scrollregion=lienzo_jugadores_mercado.bbox("all"))

def mostrar_knn():
    mostrar_datos_csv_en_lienzo('./Data/mercado_predicciones_knn.csv')
    lienzo_jugadores_mercado.update_idletasks()
    lienzo_jugadores_mercado.config(scrollregion=lienzo_jugadores_mercado.bbox("all"))

def mostrar_decision_tree():
    mostrar_datos_csv_en_lienzo('./Data/mercado_predicciones_arbol.csv')
    lienzo_jugadores_mercado.update_idletasks()
    lienzo_jugadores_mercado.config(scrollregion=lienzo_jugadores_mercado.bbox("all"))    

def crear_ventana_principal():
    global lienzo_jugadores_mercado
    global tabla_jugadores
    # Crear la ventana principal
    ventana = tk.Tk()
    ventana.title("PREDITECH INSIGHTS")
    # Configurar el tamaño de la ventana
    ventana.geometry("800x600")

    # Crear el header con el nombre "PREDITECH INSIGHTS"
    header = tk.Label(ventana, text="PREDITECH INSIGHTS", bg="green2", fg="black", font=("Georgia", 16))
    header.grid(row=0, column=0, columnspan=3, sticky="ew")

    # Crear un Canvas para la línea de separación debajo del header
    canvas = tk.Canvas(ventana, height=2, bg='black')
    canvas.grid(row=1, column=0, columnspan=3, sticky="ew")

    # Crear la caja izquierda y añadir scrollbar horizontal
    frame_izquierda = tk.Frame(ventana, bg="lightgrey")
    frame_izquierda.grid(row=2, column=0, sticky="nsew", padx=5, pady=5)

    # Header para la caja izquierda
    header_izquierda = tk.Label(frame_izquierda, text="EQUIPO", bg="lightgrey", fg="black", font=("Georgia", 14))
    header_izquierda.pack(side="top", fill="x")

    # Línea de separación debajo del header izquierdo
    linea_separacion_izquierda = tk.Canvas(frame_izquierda, height=2, bg='black')
    linea_separacion_izquierda.pack(fill="x")

    # Crear un Treeview para mostrar los datos de los jugadores
    tabla_jugadores = ttk.Treeview(frame_izquierda, columns=("Nombre", "Apellido", "Equipo", "Valor", "Predicción Valor", "Puntos Totales", "Predicción Puntos"),
                                   show="headings")
    tabla_jugadores.heading("Nombre", text="Nombre")
    tabla_jugadores.heading("Apellido", text="Apellido")
    tabla_jugadores.heading("Equipo", text="Equipo")
    tabla_jugadores.heading("Valor", text="Valor")
    tabla_jugadores.heading("Predicción Valor", text="Predicción Valor")
    tabla_jugadores.heading("Puntos Totales", text="Puntos Totales")
    tabla_jugadores.heading("Predicción Puntos", text="Predicción Puntos")
    tabla_jugadores.pack(fill="both", expand=True)
    
    # Definir tags con colores para el Treeview
    tabla_jugadores.tag_configure('mayor', background='lightgreen')
    tabla_jugadores.tag_configure('menor', background='red')
    
    ruta_archivo = './Data/Equipo_Predicciones.csv'
    datos_jugadores = leer_datos_csv(ruta_archivo)

    # Insertar los datos de los jugadores en la tabla
    for jugador in datos_jugadores:
        valor = float(jugador['valor'])
        pred_valor_rf = float(jugador['pred_valor_rf'])

        # Decidir qué tag usar en función de la condición
        if pred_valor_rf > valor:
            tag = 'mayor'
        else:
            tag = 'menor'
            
        tabla_jugadores.insert("", "end", values=(jugador['nombre'], jugador['apellido'], jugador['nombre_equipo'],
                                                  jugador['valor'], jugador['pred_valor_rf'],
                                                  jugador['puntos_totales'], jugador['pred_puntos_siguiente_jornada_rf']),tags=(tag,))

    # Configurar scroll vertical para la tabla
    scroll_y = ttk.Scrollbar(frame_izquierda, orient="vertical", command=tabla_jugadores.yview)
    tabla_jugadores.configure(yscrollcommand=scroll_y.set)
    scroll_y.pack(side="right", fill="y")

    # Configurar scroll horizontal para la tabla
    scroll_x = ttk.Scrollbar(frame_izquierda, orient="horizontal", command=tabla_jugadores.xview)
    tabla_jugadores.configure(xscrollcommand=scroll_x.set)
    scroll_x.pack(side="bottom", fill="x")

    # Configurar el tamaño de las columnas en la tabla
    tabla_jugadores.column("Nombre", width=100)
    tabla_jugadores.column("Apellido", width=100)
    tabla_jugadores.column("Equipo", width=100)
    tabla_jugadores.column("Valor", width=100)
    tabla_jugadores.column("Predicción Valor", width=100)
    tabla_jugadores.column("Puntos Totales", width=100)
    tabla_jugadores.column("Predicción Puntos", width=100)
    
    
    #PARTE DERECHA

    # Crear la caja DERECHA
    caja_derecha = tk.Frame(ventana, bg="lightgrey")
    caja_derecha.grid(row=2, column=2, sticky="nsew")
    header_derecha = tk.Label(caja_derecha, text="MERCADO", bg="lightgrey",fg="black", font=("Georgia", 14))
    header_derecha.pack(side="top", fill="x")
    
    # Línea de separación debajo del header derecho
    linea_separacion_derecha = tk.Canvas(caja_derecha, height=2, bg='black')
    linea_separacion_derecha.pack(fill="x")
    
    # Crear la caja debajo del navbox en Mercado
    caja_jugadores_mercado = tk.Frame(caja_derecha, bg="white")
    caja_jugadores_mercado.pack(fill="both", expand=True)
    
    # Configurar las barras de desplazamiento vertical y horizontal
    scroll_y = tk.Scrollbar(caja_jugadores_mercado, orient="vertical")
    scroll_y.pack(side="right", fill="y")
    scroll_x = tk.Scrollbar(caja_jugadores_mercado, orient="horizontal")
    scroll_x.pack(side="bottom", fill="x")
    
    # Crear un lienzo (Canvas) dentro de la caja de jugadores en Mercado
    lienzo_jugadores_mercado = tk.Canvas(caja_jugadores_mercado, bg="white", bd=0, xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
    lienzo_jugadores_mercado.pack(fill="both", expand=True)
    scroll_x.config(command=lienzo_jugadores_mercado.xview)
    scroll_y.config(command=lienzo_jugadores_mercado.yview)
    # Configurar scrollregion
    lienzo_jugadores_mercado.update_idletasks()
    lienzo_jugadores_mercado.config(scrollregion=lienzo_jugadores_mercado.bbox("all"))

    # Configurar los pesos de las columnas y filas
    ventana.grid_columnconfigure(0, weight=1)
    ventana.grid_columnconfigure(1, weight=0)  # Peso mínimo para la línea divisoria
    ventana.grid_columnconfigure(2, weight=1)
    ventana.grid_rowconfigure(2, weight=1)

    # Crear navbox en la caja derecha
    navbox = tk.Frame(caja_derecha, bg="lightgrey", bd=2, relief="groove")
    navbox.pack(side="top", fill="x", padx=10, pady=20)

    # Opciones para el navbox
    opciones = ["Random Forest", "KNN", "Decision Tree"]
    for opcion in opciones:
        if opcion == "Random Forest":
            boton = tk.Button(navbox, text=opcion, bg="lightgrey", relief="flat", command=mostrar_random_forest)
        elif opcion == "KNN":
            boton = tk.Button(navbox, text=opcion, bg="lightgrey", relief="flat", command=mostrar_knn)
        elif opcion == "Decision Tree":
            boton = tk.Button(navbox, text=opcion, bg="lightgrey", relief="flat", command=mostrar_decision_tree)

        boton.pack(side="left", fill="both", expand=True)
        
    def on_closing():
        ventana.withdraw()

    ventana.protocol("WM_DELETE_WINDOW", on_closing)  # Configura la acción al cerrar la ventana

    ventana.mainloop() 
    
    
# Ejecutar programa

if __name__ == "__main__":
    ventana_login()  # Iniciar con la ventana de login
