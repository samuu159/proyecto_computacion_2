from abc import ABC, abstractmethod
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException
import time
from unidecode import unidecode
import bbdd

class PartidosAbstractos(ABC):
    def __init__(self):
        self.driver = None

    @abstractmethod
    def refresh_page(self):
        pass

    @abstractmethod
    def chromedriver(self):
        pass

    @abstractmethod
    def obtener_links_jornadas(self):
        pass

    @abstractmethod
    def obtener_partidos(self):
        pass



class Partidos(PartidosAbstractos):
    def __init__(self):
        super().__init__()

    def refresh_page(self):
        self.driver.refresh()

    def chromedriver(self):
        # Configuración del navegador
        options = Options()
        options.add_argument('--disable-notifications')

        # Ruta al controlador de Chrome
        s = Service('chromedriver-win64/chromedriver.exe')

        # Crear una instancia de ChromeDriver
        self.driver = webdriver.Chrome(service=s, options=options)

        # Devolver el controlador de Chrome
        return self.driver
    
    def obtener_links_jornadas(self):
        seguir = True
        while seguir:
            try:
                lista_partidos = WebDriverWait(self.driver, 5).until(
                    EC.visibility_of_all_elements_located((By.CLASS_NAME, 'player-row'))
                )

                link_partidos = []
                for partido in lista_partidos:
                    try:
                        enlace_partido = WebDriverWait(partido, 5).until(
                            EC.visibility_of_element_located((By.CLASS_NAME, 'btn-sw-link'))
                        )
                        href_attribute = enlace_partido.get_attribute('href')
                        link_partidos.append(href_attribute)

                    except Exception as e:
                        print(f"Error: {e}")

            except Exception as e:
                print(f"Error: {e}")

                time.sleep(2)
                boton = WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, '/html/body/div[6]/div[3]/div[3]/div[1]/button'))
                )
                boton.click()
                print("Botón 'Siguiente' clicado.")
            except TimeoutException as e:
                print("TimeoutException: ", e)
                seguir = False
            except Exception as e:
                print("Otra excepción:", e)
                seguir = False

        

        

        #print(link_jugadores)
        return link_jugadores

        