import mysql.connector
from abc import ABC, abstractmethod
import bbdd
from sshtunnel import SSHTunnelForwarder

class BBDD(ABC):
    @abstractmethod
    def conexion_bbdd(self):
        pass

    @abstractmethod
    def conexion_ubuntu(self):
        pass

    @abstractmethod
    def consultar_usuario(self, conexion):
        pass

    @abstractmethod
    def insertar_jugador_bbdd(self, lista_datos_jugadores, conexion):
        pass

    @abstractmethod
    def insertar_equipo_bbdd(self, lista_datos_equipos, conexion):
        pass



    @abstractmethod
    def cerrar_conexion(self, conexion):
        pass

class MySQL(BBDD):
    def conexion_bbdd(self):
        try:
            conexion = mysql.connector.connect(
                host="bxlfjozyadylicrojiil-mysql.services.clever-cloud.com",
                user="uvbui3pydp3dtywa",
                password="RlFkyyTF3rhbD2AppQHU",
                database="bxlfjozyadylicrojiil"
            )
            print("Conexión establecida correctamente.")
            return conexion
        except mysql.connector.Error as error:
            print("Error al conectar a la base de datos:", error)


    def conexion_ubuntu(self):
        try:
            with SSHTunnelForwarder(
                ('195.235.211.197', 35025),  # Dirección IP y puerto SSH
                ssh_username='ubuntu',
                ssh_password='ubuntu',
                remote_bind_address=('localhost', 3306)  # Dirección IP y puerto MySQL
            ) as tunnel:
                conexion = mysql.connector.connect(
                    user='admin',
                    password='7NxM!Br@7TH4_FV',
                    host='127.0.0.1',
                    port=tunnel.local_bind_port,
                    database='proyecto_computacion_2'
                )
                print("Conexión establecida correctamente con Ubuntu.")
                return conexion
        except Exception as error:
            print("Error al conectar a la base de datos:", error)

    def consultar_usuario():
        try:
            with SSHTunnelForwarder(
                ('195.235.211.197', 35025),
                ssh_username='ubuntu',
                ssh_password='ubuntu',
                remote_bind_address=('localhost', 3306)
            ) as tunnel:
                # Establecer conexión a la base de datos dentro del contexto del túnel SSH
                conexion_bd = mysql.connector.connect(
                    user='admin',
                    password='7NxM!Br@7TH4_FV',
                    host='127.0.0.1',
                    port=tunnel.local_bind_port,
                    database='proyecto_computacion_2'
                )
                
                with conexion_bd.cursor() as cursor:
                    consulta = "SELECT Id_usuario FROM Usuarios WHERE Correo = %s"
                    correo = "ivangarciamoriones23@gmail.com"
                    cursor.execute(consulta, (correo,))
                    resultado = cursor.fetchone()
                    cursor.close()
                    if resultado:
                        Id_usuario = resultado[0]
                        print("El ID de usuario para el correo {} es: {}".format(correo, Id_usuario))
                        return Id_usuario
                    else:
                        print("No se encontró ningún usuario con el correo {}".format(correo))
                        return None
        except mysql.connector.Error as error:
            print("Error al ejecutar la consulta:", error)



    def insertar_jugador_bbdd(datos_jugadores):
        try:
            with SSHTunnelForwarder(
                ('195.235.211.197', 35025),
                ssh_username='ubuntu',
                ssh_password='ubuntu',
                remote_bind_address=('localhost', 3306)
            ) as tunnel:
                # Establecer conexión a la base de datos dentro del contexto del túnel SSH
                conexion_bd = mysql.connector.connect(
                    user='admin',
                    password='7NxM!Br@7TH4_FV',
                    host='127.0.0.1',
                    port=tunnel.local_bind_port,
                    database='proyecto_computacion_2'
                )
                
                with conexion_bd.cursor() as cursor:
                    
                    consulta_existencia = "SELECT * FROM Jugadores WHERE Nombre = %s AND Apellido = %s"
                    parametros = (
                        datos_jugadores["nombre"],
                        datos_jugadores["apellido"]
                    )
                    cursor.execute(consulta_existencia, parametros)
                    resultado = cursor.fetchone()
                    if resultado:
                        print("El jugador ya existe en la base de datos. No es necesario insertarlo.")
                    else:
                        placeholders_jornadas = ', '.join(['%s'] * 38)
                        consulta_insercion = f"INSERT INTO Jugadores (Nombre, Apellido, Equipo, Posicion, Valor, Puntos_totales, Media_total, Partidos, Goles, Tarjetas, Media_en_casa, Media_visitante, Valor_subido_bajado, Mercado, Puntos_predicción, Valor_predicción, Jornada_1, Jornada_2, Jornada_3, Jornada_4, Jornada_5, Jornada_6, Jornada_7, Jornada_8, Jornada_9, Jornada_10, Jornada_11, Jornada_12, Jornada_13, Jornada_14, Jornada_15, Jornada_16, Jornada_17, Jornada_18, Jornada_19, Jornada_20, Jornada_21, Jornada_22, Jornada_23, Jornada_24, Jornada_25, Jornada_26, Jornada_27, Jornada_28, Jornada_29, Jornada_30, Jornada_31, Jornada_32, Jornada_33, Jornada_34, Jornada_35, Jornada_36, Jornada_37, Jornada_38) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, {placeholders_jornadas})"
                        parametros_insercion = (
                            datos_jugadores["nombre"],
                            datos_jugadores["apellido"],
                            datos_jugadores["nombre_equipo"],
                            datos_jugadores["posicion"],
                            datos_jugadores["valor"],
                            datos_jugadores["puntos_totales"],
                            datos_jugadores["media"],
                            datos_jugadores["partidos"],
                            datos_jugadores["goles"],
                            datos_jugadores["tarjetas"],
                            datos_jugadores["media_en_casa"],
                            datos_jugadores["media_fuera"],
                            datos_jugadores["valor_subido_bajado"],
                            datos_jugadores["mercado"],
                            datos_jugadores["puntos_predicción"],
                            datos_jugadores["valor_predicción"],
                            datos_jugadores["jornada_1"],
                            datos_jugadores["jornada_2"],
                            datos_jugadores["jornada_3"],
                            datos_jugadores["jornada_4"],
                            datos_jugadores["jornada_5"],
                            datos_jugadores["jornada_6"],
                            datos_jugadores["jornada_7"],
                            datos_jugadores["jornada_8"],
                            datos_jugadores["jornada_9"],
                            datos_jugadores["jornada_10"],
                            datos_jugadores["jornada_11"],
                            datos_jugadores["jornada_12"],
                            datos_jugadores["jornada_13"],
                            datos_jugadores["jornada_14"],
                            datos_jugadores["jornada_15"],
                            datos_jugadores["jornada_16"],
                            datos_jugadores["jornada_17"],
                            datos_jugadores["jornada_18"],
                            datos_jugadores["jornada_19"],
                            datos_jugadores["jornada_20"],
                            datos_jugadores["jornada_21"],
                            datos_jugadores["jornada_22"],
                            datos_jugadores["jornada_23"],
                            datos_jugadores["jornada_24"],
                            datos_jugadores["jornada_25"],
                            datos_jugadores["jornada_26"],
                            datos_jugadores["jornada_27"],
                            datos_jugadores["jornada_28"],
                            datos_jugadores["jornada_29"],
                            datos_jugadores["jornada_30"],
                            datos_jugadores["jornada_31"],
                            datos_jugadores["jornada_32"],
                            datos_jugadores["jornada_33"],
                            datos_jugadores["jornada_34"],
                            datos_jugadores["jornada_35"],
                            datos_jugadores["jornada_36"],
                            datos_jugadores["jornada_37"],
                            datos_jugadores["jornada_38"]
                        )
                        cursor.execute(consulta_insercion, parametros_insercion)
                        conexion_bd.commit()
                        print("Datos del jugador insertados correctamente.")

        except mysql.connector.Error as error:
            print("Error al ejecutar la consulta:", error)


    def insertar_equipo_bbdd(datos_equipos):
        try:
            with SSHTunnelForwarder(
                ('195.235.211.197', 35025),
                ssh_username='ubuntu',
                ssh_password='ubuntu',
                remote_bind_address=('localhost', 3306)
            ) as tunnel:
                # Establecer conexión a la base de datos dentro del contexto del túnel SSH
                conexion_bd = mysql.connector.connect(
                    user='admin',
                    password='7NxM!Br@7TH4_FV',
                    host='127.0.0.1',
                    port=tunnel.local_bind_port,
                    database='proyecto_computacion_2'
                )
                
                with conexion_bd.cursor() as cursor:
                    
                    consulta_existencia = "SELECT * FROM Equipos WHERE Nombre = %s"
                    parametros = (datos_equipos["nombre"],)
                    cursor.execute(consulta_existencia, parametros)
                    resultado = cursor.fetchone()

                    if resultado:
                        print("El equipo ya existe en la base de datos. No es necesario insertarlo.")
                    else:
                        consulta_insercion = "INSERT INTO Equipos (Nombre, Partidos, Puntos, Partidos_ganados, Partidos_empatados, Partidos_perdidos, Goles_a_favor, Goles_en_contra, Diferencia_goles) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                        parametros_insercion = (
                            datos_equipos["nombre"],
                            datos_equipos["partidos"],
                            datos_equipos["puntos"],
                            datos_equipos["partidos_ganados"],
                            datos_equipos["partidos_empatados"],
                            datos_equipos["partidos_perdidos"],
                            datos_equipos["goles_a_favor"],
                            datos_equipos["goles_en_contra"],
                            datos_equipos["diferencia_goles"]
                        )
                        cursor.execute(consulta_insercion, parametros_insercion)
                        conexion_bd.commit()
                        print("Datos del equipo insertados correctamente.")

        except mysql.connector.Error as error:
            print("Error al ejecutar la consulta:", error)


    def insertar_equipo_usuario(datos_equipo_usuario):
        try:
            with SSHTunnelForwarder(
                ('195.235.211.197', 35025),
                ssh_username='ubuntu',
                ssh_password='ubuntu',
                remote_bind_address=('localhost', 3306)
            ) as tunnel:
                # Establecer conexión a la base de datos dentro del contexto del túnel SSH
                conexion_bd = mysql.connector.connect(
                    user='admin',
                    password='7NxM!Br@7TH4_FV',
                    host='127.0.0.1',
                    port=tunnel.local_bind_port,
                    database='proyecto_computacion_2'
                )
                
                with conexion_bd.cursor() as cursor:
                    id_usuario = bbdd.MySQL.consultar_usuario()
                    # Crear un cursor para ejecutar consultas SQL
                    cursor = conexion_bd.cursor()

                    # Definir la consulta SQL para verificar la existencia del jugador por nombre y apellido
                    consulta_existencia = "SELECT * FROM Jugadores WHERE Nombre = %s AND Apellido = %s"
                    # Parámetros de la consulta
                    parametros = (
                        datos_equipo_usuario["nombre"],
                        datos_equipo_usuario["apellido"]
                    )
                    #print(parametros)

                    # Ejecutar la consulta para verificar la existencia del jugador
                    cursor.execute(consulta_existencia, parametros)

                    # Obtener el resultado de la consulta
                    resultado = cursor.fetchone()
                    #print(resultado)

                    # Verificar si el jugador ya existe en la tabla
                    if resultado:
                        # Definir la consulta SQL para actualizar el Id_usuario
                        consulta = "UPDATE Jugadores SET Id_usuario = %s WHERE nombre = %s AND apellido = %s"

                        parametros = (
                        datos_equipo_usuario["nombre"],
                        datos_equipo_usuario["apellido"]
                        )


                        # Ejecutar la consulta para actualizar el Id_usuario
                        cursor.execute(consulta,(id_usuario,) + parametros)

                        # Confirmar la transacción
                        conexion_bd.commit()

                        # Cerrar el cursor y la conexión
                        cursor.close()
                        conexion_bd.close()

                        print("Se ha actualizado el Id_usuario para el usuario {} {} con el valor: {}".format(datos_equipo_usuario["nombre"], datos_equipo_usuario["apellido"], id_usuario))

                    else:
                        # Definir la consulta SQL para insertar datos
                        print("No se ha encontrado el jugador {} {}".format(datos_equipo_usuario["nombre"], datos_equipo_usuario["apellido"]))


        except mysql.connector.Error as error:
            print("Error al ejecutar la consulta:", error)


    def insertar_mercado_usuario(datos_mercado_usuario):
        try:
            with SSHTunnelForwarder(
                ('195.235.211.197', 35025),
                ssh_username='ubuntu',
                ssh_password='ubuntu',
                remote_bind_address=('localhost', 3306)
            ) as tunnel:
                # Establecer conexión a la base de datos dentro del contexto del túnel SSH
                conexion_bd = mysql.connector.connect(
                    user='admin',
                    password='7NxM!Br@7TH4_FV',
                    host='127.0.0.1',
                    port=tunnel.local_bind_port,
                    database='proyecto_computacion_2'
                )
                
                with conexion_bd.cursor() as cursor:
                    # Definir la consulta SQL para verificar la existencia del jugador por nombre y apellido
                    consulta_existencia = "SELECT * FROM Jugadores WHERE Nombre = %s AND Apellido = %s"
                    # Parámetros de la consulta
                    parametros = (
                        datos_mercado_usuario["nombre"],
                        datos_mercado_usuario["apellido"]
                    )

                    # Ejecutar la consulta para verificar la existencia del jugador
                    cursor.execute(consulta_existencia, parametros)

                    # Obtener el resultado de la consulta
                    resultado = cursor.fetchone()

                    # Verificar si el jugador ya existe en la tabla
                    if resultado:
                        mercado = 1  # Establecer el valor como 1 para indicar que el jugador está en el mercado
                        # Definir la consulta SQL para actualizar el valor del Mercado
                        consulta = "UPDATE Jugadores SET Mercado = %s WHERE nombre = %s AND apellido = %s"

                        # Combinar el valor de Mercado con los parámetros del jugador en una tupla única
                        parametros_actualizacion = (mercado,) + parametros

                        # Ejecutar la consulta para actualizar el valor del Mercado
                        cursor.execute(consulta, parametros_actualizacion)

                        # Confirmar la transacción
                        conexion_bd.commit()

                        print("Se ha actualizado el Mercado para el jugador {} {}".format(datos_mercado_usuario["nombre"], datos_mercado_usuario["apellido"]))

                    else:
                        print("No se ha encontrado el jugador {} {}".format(datos_mercado_usuario["nombre"], datos_mercado_usuario["apellido"]))

        except mysql.connector.Error as error:
            print("Error al ejecutar la consulta:", error)





    def cerrar_conexion(self, conexion):
        try:
            if conexion.is_connected():
                conexion.close()
                print("Conexión cerrada correctamente.")
            else:
                print("La conexión ya está cerrada.")
        except mysql.connector.Error as error:
            print("Error al cerrar la conexión:", error)
