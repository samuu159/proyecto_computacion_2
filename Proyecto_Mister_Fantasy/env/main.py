import jugadores
import bbdd
import equipos
import equipo_usuario
import mercado
import partidos
from abc import ABC, abstractmethod

class Main(ABC):
    @abstractmethod
    def main_jugadores(self):
        pass

    @abstractmethod
    def main_equipos(self):
        pass

    @abstractmethod
    def main_equipo_usuario(self):
        pass

    @abstractmethod
    def main_mercado_usuario(self):
        pass

    @abstractmethod
    def main_partidos(self):
        pass

class Programa(Main):
    def main_jugadores(self):
        # Obtener una instancia de ChromeDriver
        jugador = jugadores.Jugadores()
        mysql_instance = bbdd.MySQL()

        jugador.chromedriver()
        driver = jugador.driver

        # Navegar a la URL
        driver.get('https://mister.mundodeportivo.com')

        # Ocultar anuncios
        jugador.hide_ads()

        # Aceptar cookies
        jugador.aceptar_cookies()

        # Iniciar sesión o registro, si es necesario
        jugador.iniciar_sesion()

        #conexion = bbdd.MySQL().conexion_bbdd()
        #print(conexion)

        conexion = mysql_instance.conexion_ubuntu()
        print(conexion)

        #mysql_instance.consultar_usuario()


        jugador.datos_jugadores()

        #mysql_instance().cerrar_conexion(conexion)  # Cerrar la conexión

        # Cerrar el navegador al finalizar
        driver.quit()




    def main_equipos(self):
        # Obtener una instancia de ChromeDriver
        equipo = equipos.Equipos()
        mysql_instance = bbdd.MySQL()


        equipo.chromedriver()
        driver = equipo.driver

        # Navegar a la URL
        driver.get('https://es.besoccer.com/competicion/clasificacion/primera')

        # Aceptar coockies
        equipo.aceptar_cookies()

        conexion = mysql_instance.conexion_ubuntu()
        print(conexion)

        equipo.datos_equipos()

        #bbdd.MySQL().cerrar_conexion(conexion)  # Cerrar la conexión

        # Cerrar el navegador al finalizar
        driver.quit()


    def main_equipo_usuario(self):
        # Obtener una instancia de ChromeDriver
        equipo_user = equipo_usuario.Equipo_usuario()
        mysql_instance = bbdd.MySQL()

        equipo_user.chromedriver()
        driver = equipo_user.driver

        # Navegar a la URL
        driver.get('https://mister.mundodeportivo.com')

        # Ocultar anuncios
        equipo_user.hide_ads()

        # Aceptar cookies
        equipo_user.aceptar_cookies()

        # Iniciar sesión o registro, si es necesario
        equipo_user.iniciar_sesion()

        #conexion = bbdd.MySQL().conexion_bbdd()
        #print(conexion)

        conexion = mysql_instance.conexion_ubuntu()
        print(conexion)

        #mysql_instance.consultar_usuario(conexion)


        equipo_user.datos_equipo_usuario()

        #mysql_instance().cerrar_conexion(conexion)  # Cerrar la conexión

        # Cerrar el navegador al finalizar
        driver.quit()

    def main_mercado_usuario(self):
        # Obtener una instancia de ChromeDriver
        mercado_user = mercado.Mercado_usuario()
        mysql_instance = bbdd.MySQL()

        mercado_user.chromedriver()
        driver = mercado_user.driver

        # Navegar a la URL
        driver.get('https://mister.mundodeportivo.com')

        # Ocultar anuncios
        mercado_user.hide_ads()

        # Aceptar cookies
        mercado_user.aceptar_cookies()

        # Iniciar sesión o registro, si es necesario
        mercado_user.iniciar_sesion()

        #conexion = bbdd.MySQL().conexion_bbdd()
        #print(conexion)

        conexion = mysql_instance.conexion_ubuntu()
        print(conexion)

        #mysql_instance.consultar_usuario(conexion)


        mercado_user.datos_mercado_usuario()

        #mysql_instance().cerrar_conexion(conexion)  # Cerrar la conexión

        # Cerrar el navegador al finalizar
        driver.quit()


    def main_partidos(self):

        partido = partidos.Partidos()
        mysql_instance = bbdd.MySQL()
        partido.chromedriver()
        driver = partido.driver
        driver.get('https://www.sofascore.com/es/torneo/futbol/spain/laliga/8#id:52376,tab:matches')


        pass


if __name__ == "__main__":
    programa = Programa()
    #programa.main_jugadores()
    #programa.main_equipos()
    #programa.main_equipo_usuario()
    programa.main_mercado_usuario()


