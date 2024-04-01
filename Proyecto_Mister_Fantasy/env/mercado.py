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

class Mercado_usuario_abstracto(ABC):
    def __init__(self):
        self.driver = None

    @abstractmethod
    def refresh_page(self):
        pass

    @abstractmethod
    def chromedriver(self):
        pass

    @abstractmethod
    def hide_ads(self):
        pass

    @abstractmethod
    def aceptar_cookies(self):
        pass

    @abstractmethod
    def iniciar_sesion(self):
        pass

    @abstractmethod
    def link_mercado_usuario(self):
        pass

    @abstractmethod
    def datos_mercado_usuario(self):
        pass

class Mercado_usuario(Mercado_usuario_abstracto):
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

    def hide_ads(self):
        self.driver.execute_script('''
            var elements = document.querySelectorAll('[class*="anuncio"]');
            elements.forEach(function(element) {
                element.style.display = 'none';
            });
        ''')

    def aceptar_cookies(self):
        try:
            boton = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.ID, "didomi-notice-agree-button"))
            )
            # Hacer clic en el botón
            boton.click()
        except Exception as e:
            print(f"Error al aceptar las cookies: {str(e)}")

    def iniciar_sesion(self):
        try:
            boton = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/button'))
            )
            boton.click()

            boton = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/button'))
            )
            boton.click()

            boton = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/button'))
            )
            boton.click()

            boton = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/button'))
            )
            boton.click()

            boton = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/button[3]'))
            )
            boton.click()

            campo_email = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="email"]'))
            )
            # Escribir en el campo de entrada de correo electrónico
            campo_email.send_keys("ivangarciamoriones23@gmail.com")

            # Esperar hasta que el campo de entrada de contraseña esté presente y sea visible
            campo_contraseña = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div[2]/div/form/div[2]/input'))
            )
            # Escribir en el campo de entrada de contraseña
            campo_contraseña.send_keys("Cloe2016!")

            boton = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div[2]/div/form/div[3]/button'))
            )
            boton.click()
            self.hide_ads()
        except Exception as e:
            print(f"Error al intentar iniciar sesión: {str(e)}")

    def link_mercado_usuario(self):
        
        self.hide_ads()
        boton = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="content"]/header/div[2]/ul/li[2]'))
            )
        boton.click()

        self.hide_ads()
        time.sleep(5)
        lista_jugadores = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_all_elements_located((By.CLASS_NAME, 'player-row'))
            )
        #print(lista_jugadores)

        link_jugadores = []
        for jugador in lista_jugadores:
            try:
                enlace_jugador = WebDriverWait(jugador, 10).until(
                    EC.visibility_of_element_located((By.CLASS_NAME, 'btn-sw-link'))
                )
                href_attribute = enlace_jugador.get_attribute('href')
                link_jugadores.append(href_attribute)

            except Exception as e:
                print(f"Error: {e}")

        return link_jugadores
    
    def datos_mercado_usuario(self):
        link_jugadores = self.link_mercado_usuario()

        for link in link_jugadores:
            self.driver.get(link)
            try:

                try:
                    
                            
                    # Intenta encontrar el elemento del nombre del jugador
                    nombre_element = WebDriverWait(self.driver, 3).until(
                        EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/div[4]/div[1]/div/div[1]/div[2]'))
                    )
                    
                    # Si se encuentra el elemento, obtén el nombre del jugador
                    nombre = unidecode(nombre_element.text)
                    print(nombre)
                except:
                    # Si no se encuentra el elemento, asigna None al nombre
                    nombre = None
                
                try:
                    apellido_element = WebDriverWait(self.driver, 3).until(
                    EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/div[4]/div[1]/div/div[1]/div[3]'))
                    )

                    apellido = unidecode(apellido_element.text)
                    print(apellido)

                except:

                    apellido = None
                
                    
                datos_mercado_usuario = {
                    "nombre": nombre,
                    "apellido": apellido,

                }

                print(datos_mercado_usuario)
                try: 
                    bbdd.MySQL.insertar_mercado_usuario(datos_mercado_usuario)  

                except Exception as e:
                    print(f"Error al insertar los datos del jugador en la base de datos: {str(e)}")

            except Exception as e:
                pass
                print(f"Error al obtener los datos del jugador: {str(e)}")