import jugadores
import bbdd
from abc import ABC, abstractmethod

class Main(ABC):
    @abstractmethod
    def main_jugadores(self):
        pass

class Programa(Main):
    def main_jugadores(self):
        # Obtener una instancia de ChromeDriver
        jugador = jugadores.Jugadores()

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

        conexion = bbdd.MySQL().conexion_ubuntu()
        print(conexion)

        bbdd.MySQL().consultar_usuario(conexion)



        #Cambiar xpath para obtener los datos de los jugadores linea 200 jugadores.py !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


        bbdd.MySQL().insertar_jugador_bbdd(jugador.datos_jugadores(), conexion)

        bbdd.MySQL().cerrar_conexion(conexion)  # Cerrar la conexión

        # Cerrar el navegador al finalizar
        driver.quit()

if __name__ == "__main__":
    programa = Programa()
    programa.main_jugadores()

    #def main_arbitros():
        # Obtener una instancia de ChromeDriver
        #driver = arbitro.chromedriver()

        # Navegar a la URL
        #driver.get('https://es.besoccer.com/competicion/arbitros/primera')

        #arbitro.hide_ads(driver)

        #arbitro.aceptar_cookies_besoccer(driver)

        #arbitro.obtener_datos_arbitros(driver)

        #bbdd.conexion_bbdd()

        #bbdd.insertar_arbitro_bbdd(arbitro.obtener_datos_arbitros(driver), bbdd.conexion_bbdd())



