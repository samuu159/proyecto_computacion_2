import mysql.connector
from abc import ABC, abstractmethod
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
                    user='root',
                    password='7NxM!Br@7TH4_FV',
                    host='127.0.0.1',
                    port=tunnel.local_bind_port,
                    database='proyecto_computacion_2'
                )
                print("Conexión establecida correctamente con Ubuntu.")
                return conexion
        except Exception as error:
            print("Error al conectar a la base de datos:", error)

    def consultar_usuario(self, conexion):
        try:
            cursor = conexion.cursor()
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



    def insertar_jugador_bbdd(self, lista_datos_jugadores, conexion):
        try:
            cursor = conexion.cursor()
            for datos_jugador in lista_datos_jugadores:
                consulta_existencia = "SELECT * FROM Jugadores WHERE Nombre = %s AND Apellido = %s"
                parametros = (
                    datos_jugador["nombre"],
                    datos_jugador["apellido"]
                )
                cursor.execute(consulta_existencia, parametros)
                resultado = cursor.fetchone()
                if resultado:
                    print("El jugador ya existe en la base de datos. No es necesario insertarlo.")
                else:
                    placeholders_jornadas = ', '.join(['%s'] * 38)
                    consulta_insercion = f"INSERT INTO Jugadores (Nombre, Apellido, Equipo, Posicion, Valor, Puntos_totales, Media_total, Partidos, Goles, Tarjetas, Media_en_casa, Media_visitante, Valor_subido_bajado, Mercado, Puntos_predicción, Valor_predicción, Jornada_1, Jornada_2, Jornada_3, Jornada_4, Jornada_5, Jornada_6, Jornada_7, Jornada_8, Jornada_9, Jornada_10, Jornada_11, Jornada_12, Jornada_13, Jornada_14, Jornada_15, Jornada_16, Jornada_17, Jornada_18, Jornada_19, Jornada_20, Jornada_21, Jornada_22, Jornada_23, Jornada_24, Jornada_25, Jornada_26, Jornada_27, Jornada_28, Jornada_29, Jornada_30, Jornada_31, Jornada_32, Jornada_33, Jornada_34, Jornada_35, Jornada_36, Jornada_37, Jornada_38) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, {placeholders_jornadas})"
                    parametros_insercion = (
                        datos_jugador["nombre"],
                        datos_jugador["apellido"],
                        datos_jugador["nombre_equipo"],
                        datos_jugador["posicion"],
                        datos_jugador["valor"],
                        datos_jugador["puntos_totales"],
                        datos_jugador["media"],
                        datos_jugador["partidos"],
                        datos_jugador["goles"],
                        datos_jugador["tarjetas"],
                        datos_jugador["media_en_casa"],
                        datos_jugador["media_fuera"],
                        datos_jugador["valor_subido_bajado"],
                        datos_jugador["mercado"],
                        datos_jugador["puntos_predicción"],
                        datos_jugador["valor_predicción"],
                        datos_jugador["jornada_1"],
                        datos_jugador["jornada_2"],
                        datos_jugador["jornada_3"],
                        datos_jugador["jornada_4"],
                        datos_jugador["jornada_5"],
                        datos_jugador["jornada_6"],
                        datos_jugador["jornada_7"],
                        datos_jugador["jornada_8"],
                        datos_jugador["jornada_9"],
                        datos_jugador["jornada_10"],
                        datos_jugador["jornada_11"],
                        datos_jugador["jornada_12"],
                        datos_jugador["jornada_13"],
                        datos_jugador["jornada_14"],
                        datos_jugador["jornada_15"],
                        datos_jugador["jornada_16"],
                        datos_jugador["jornada_17"],
                        datos_jugador["jornada_18"],
                        datos_jugador["jornada_19"],
                        datos_jugador["jornada_20"],
                        datos_jugador["jornada_21"],
                        datos_jugador["jornada_22"],
                        datos_jugador["jornada_23"],
                        datos_jugador["jornada_24"],
                        datos_jugador["jornada_25"],
                        datos_jugador["jornada_26"],
                        datos_jugador["jornada_27"],
                        datos_jugador["jornada_28"],
                        datos_jugador["jornada_29"],
                        datos_jugador["jornada_30"],
                        datos_jugador["jornada_31"],
                        datos_jugador["jornada_32"],
                        datos_jugador["jornada_33"],
                        datos_jugador["jornada_34"],
                        datos_jugador["jornada_35"],
                        datos_jugador["jornada_36"],
                        datos_jugador["jornada_37"],
                        datos_jugador["jornada_38"]
                    )
                    cursor.execute(consulta_insercion, parametros_insercion)
                    conexion.commit()
                    print("Datos del jugador insertados correctamente.")
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
