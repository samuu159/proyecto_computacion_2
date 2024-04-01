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

class EquiposAbstractos(ABC):
    def __init__(self):
        self.driver = None

    @abstractmethod
    def refresh_page(self):
        pass

    @abstractmethod
    def chromedriver(self):
        pass

    @abstractmethod
    def aceptar_cookies(self):
        pass

    @abstractmethod
    def link_equipos(self):
        pass

    @abstractmethod
    def datos_equipos(self):
        pass


class Equipos(EquiposAbstractos):
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
    
    def aceptar_cookies(self):
        try:
            accept_button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/button[3]'))
            )

            accept_button.click()
            print("Cookies aceptadas.")
        except Exception as e:
            print("No fue necesario aceptar cookies o no se encontró el botón.", e)

    def link_equipos(self):
        try:
            lista_equipos = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_all_elements_located((By.XPATH, '/html/body/main/section[3]/div/div[6]/div[2]/div[2]/div/div[2]/div/div/table/tbody/tr'))
            )
            #print(lista_equipos)

            link_equipos = []
            for equipo in lista_equipos[1:]:  # Omitir el primer elemento
                try:
                    enlace_equipo = WebDriverWait(equipo, 5).until(
                        EC.visibility_of_element_located((By.TAG_NAME, 'a'))
                    )
                    href_attribute = enlace_equipo.get_attribute('href')
                    link_equipos.append(href_attribute)

                except Exception as e:
                    print(f"Error: {e}")
            #print(link_equipos)
            return link_equipos

        except Exception as e:
            print(f"Error al obtener la lista de equipos: {e}")
            return []


    def datos_equipos(self):
        try:
            links_equipos = self.link_equipos()
            #lista_datos_equipos = []  # Lista para almacenar los datos de todos los equipos

            num_equipos = len(links_equipos)

            for i, link in enumerate(links_equipos):
                self.driver.get(link)
                try:
                    # Verificar si estamos en el primer equipo
                    if i == 0:
                        tabla = WebDriverWait(self.driver, 5).until(
                            EC.presence_of_element_located((By.XPATH, '/html/body/main/section[2]/div[2]/div[14]/div/div[2]/table/tbody'))
                        )

                        nombre_element = WebDriverWait(self.driver, 5).until(
                            EC.presence_of_element_located((By.XPATH, '/html/body/main/section[1]/div/div[1]/div[1]/div/h2'))
                        )
                        nombre = unidecode(nombre_element.text)

                        puntos = int(WebDriverWait(self.driver, 5).until(
                            EC.presence_of_element_located((By.XPATH, '/html/body/main/section[2]/div[2]/div[14]/div/div[2]/table/tbody/tr[2]/td[4]/strong'))
                        ).text)

                        partidos = int(WebDriverWait(self.driver, 5).until(
                            EC.presence_of_element_located((By.XPATH, '/html/body/main/section[2]/div[2]/div[14]/div/div[2]/table/tbody/tr[2]/td[5]'))
                        ).text)

                        partidos_ganados = int(WebDriverWait(self.driver, 5).until(
                            EC.presence_of_element_located((By.XPATH, '/html/body/main/section[2]/div[2]/div[14]/div/div[2]/table/tbody/tr[2]/td[6]'))
                        ).text)

                        partidos_empatados = int(WebDriverWait(self.driver, 5).until(
                            EC.presence_of_element_located((By.XPATH, '/html/body/main/section[2]/div[2]/div[14]/div/div[2]/table/tbody/tr[2]/td[7]'))
                        ).text)

                        partidos_perdidos = int(WebDriverWait(self.driver, 5).until(
                            EC.presence_of_element_located((By.XPATH, '/html/body/main/section[2]/div[2]/div[14]/div/div[2]/table/tbody/tr[2]/td[8]'))
                        ).text)

                        goles_a_favor = int(WebDriverWait(self.driver, 5).until(
                            EC.presence_of_element_located((By.XPATH, '/html/body/main/section[2]/div[2]/div[14]/div/div[2]/table/tbody/tr[2]/td[9]'))
                        ).text)

                        goles_en_contra = int(WebDriverWait(self.driver, 5).until(
                            EC.presence_of_element_located((By.XPATH, '/html/body/main/section[2]/div[2]/div[14]/div/div[2]/table/tbody/tr[2]/td[10]'))
                        ).text)

                        # Obtener la diferencia de goles
                        diferencia_goles = WebDriverWait(self.driver, 5).until(
                            EC.presence_of_element_located((By.XPATH, '/html/body/main/section[2]/div[2]/div[14]/div/div[2]/table/tbody/tr[2]/td[11]'))
                        ).text

                        # Eliminar el signo "+" si está presente
                        if '+' in diferencia_goles:
                            diferencia_goles = diferencia_goles.replace('+', '')

                        diferencia_goles = int(diferencia_goles)

                    # Verificar si estamos en el segundo equipo
                    elif i == 1:
                        tabla = WebDriverWait(self.driver, 5).until(
                            EC.presence_of_element_located((By.XPATH, '/html/body/main/section[2]/div[2]/div[14]/div/div[2]/table/tbody'))
                        )

                        nombre_element = WebDriverWait(self.driver, 5).until(
                            EC.presence_of_element_located((By.XPATH, '/html/body/main/section[1]/div/div[1]/div[1]/div/h2'))
                        )
                        nombre = unidecode(nombre_element.text)

                        puntos = int(WebDriverWait(self.driver, 5).until(
                            EC.presence_of_element_located((By.XPATH, '/html/body/main/section[2]/div[2]/div[14]/div/div[2]/table/tbody/tr[3]/td[4]/strong'))
                        ).text)

                        partidos = int(WebDriverWait(self.driver, 5).until(
                            EC.presence_of_element_located((By.XPATH, '/html/body/main/section[2]/div[2]/div[14]/div/div[2]/table/tbody/tr[3]/td[5]'))
                        ).text)

                        partidos_ganados = int(WebDriverWait(self.driver, 5).until(
                            EC.presence_of_element_located((By.XPATH, '/html/body/main/section[2]/div[2]/div[14]/div/div[2]/table/tbody/tr[3]/td[6]'))
                        ).text)

                        partidos_empatados = int(WebDriverWait(self.driver, 5).until(
                            EC.presence_of_element_located((By.XPATH, '/html/body/main/section[2]/div[2]/div[14]/div/div[2]/table/tbody/tr[3]/td[7]'))
                        ).text)

                        partidos_perdidos = int(WebDriverWait(self.driver, 5).until(
                            EC.presence_of_element_located((By.XPATH, '/html/body/main/section[2]/div[2]/div[14]/div/div[2]/table/tbody/tr[3]/td[8]'))
                        ).text)

                        goles_a_favor = int(WebDriverWait(self.driver, 5).until(
                            EC.presence_of_element_located((By.XPATH, '/html/body/main/section[2]/div[2]/div[14]/div/div[2]/table/tbody/tr[3]/td[9]'))
                        ).text)

                        goles_en_contra = int(WebDriverWait(self.driver, 5).until(
                            EC.presence_of_element_located((By.XPATH, '/html/body/main/section[2]/div[2]/div[14]/div/div[2]/table/tbody/tr[3]/td[10]'))
                        ).text)

                        # Obtener la diferencia de goles
                        diferencia_goles_text = WebDriverWait(self.driver, 5).until(
                            EC.presence_of_element_located((By.XPATH, '/html/body/main/section[2]/div[2]/div[14]/div/div[2]/table/tbody/tr[3]/td[11]'))
                        ).text

                        # Remover el signo '+' si está presente
                        if diferencia_goles_text.startswith('+'):
                            diferencia_goles_text = diferencia_goles_text[1:]

                        diferencia_goles = int(diferencia_goles_text)
                    # Verificar si estamos en el penúltimo equipo
                    elif i == num_equipos - 2:
                        tabla = WebDriverWait(self.driver, 5).until(
                            EC.presence_of_element_located((By.XPATH, '/html/body/main/section[2]/div[2]/div[14]/div/div[2]/table/tbody'))
                        )

                        nombre_element = WebDriverWait(self.driver, 5).until(
                            EC.presence_of_element_located((By.XPATH, '/html/body/main/section[1]/div/div[1]/div[1]/div/h2'))
                        )
                        nombre = unidecode(nombre_element.text)

                        puntos = int(WebDriverWait(self.driver, 5).until(
                            EC.presence_of_element_located((By.XPATH, '/html/body/main/section[2]/div[2]/div[14]/div/div[2]/table/tbody/tr[5]/td[4]/strong'))
                        ).text)

                        partidos = int(WebDriverWait(self.driver, 5).until(
                            EC.presence_of_element_located((By.XPATH, '/html/body/main/section[2]/div[2]/div[14]/div/div[2]/table/tbody/tr[5]/td[5]'))
                        ).text)

                        partidos_ganados = int(WebDriverWait(self.driver, 5).until(
                            EC.presence_of_element_located((By.XPATH, '/html/body/main/section[2]/div[2]/div[14]/div/div[2]/table/tbody/tr[5]/td[6]'))
                        ).text)

                        partidos_empatados = int(WebDriverWait(self.driver, 5).until(
                            EC.presence_of_element_located((By.XPATH, '/html/body/main/section[2]/div[2]/div[14]/div/div[2]/table/tbody/tr[5]/td[7]'))
                        ).text)

                        partidos_perdidos = int(WebDriverWait(self.driver, 5).until(
                            EC.presence_of_element_located((By.XPATH, '/html/body/main/section[2]/div[2]/div[14]/div/div[2]/table/tbody/tr[5]/td[8]'))
                        ).text)

                        goles_a_favor = int(WebDriverWait(self.driver, 5).until(
                            EC.presence_of_element_located((By.XPATH, '/html/body/main/section[2]/div[2]/div[14]/div/div[2]/table/tbody/tr[5]/td[9]'))
                        ).text)

                        goles_en_contra = int(WebDriverWait(self.driver, 5).until(
                            EC.presence_of_element_located((By.XPATH, '/html/body/main/section[2]/div[2]/div[14]/div/div[2]/table/tbody/tr[5]/td[10]'))
                        ).text)

                        # Obtener la diferencia de goles
                        diferencia_goles_text = WebDriverWait(self.driver, 5).until(
                            EC.presence_of_element_located((By.XPATH, '/html/body/main/section[2]/div[2]/div[14]/div/div[2]/table/tbody/tr[5]/td[11]'))
                        ).text

                        # Remover el signo '+' si está presente
                        if diferencia_goles_text.startswith('+'):
                            diferencia_goles_text = diferencia_goles_text[1:]

                        diferencia_goles = int(diferencia_goles_text)
                    # Verificar si estamos en el último equipo
                    elif i == num_equipos - 1:
                        tabla = WebDriverWait(self.driver, 5).until(
                            EC.presence_of_element_located((By.XPATH, '/html/body/main/section[2]/div[2]/div[14]/div/div[2]/table/tbody'))
                        )

                        nombre_element = WebDriverWait(self.driver, 5).until(
                            EC.presence_of_element_located((By.XPATH, '/html/body/main/section[1]/div/div[1]/div[1]/div/h2'))
                        )
                        nombre = unidecode(nombre_element.text)

                        puntos = int(WebDriverWait(self.driver, 5).until(
                            EC.presence_of_element_located((By.XPATH, '/html/body/main/section[2]/div[2]/div[14]/div/div[2]/table/tbody/tr[6]/td[4]/strong'))
                        ).text)

                        partidos = int(WebDriverWait(self.driver, 5).until(
                            EC.presence_of_element_located((By.XPATH, '/html/body/main/section[2]/div[2]/div[14]/div/div[2]/table/tbody/tr[6]/td[5]'))
                        ).text)

                        partidos_ganados = int(WebDriverWait(self.driver, 5).until(
                            EC.presence_of_element_located((By.XPATH, '/html/body/main/section[2]/div[2]/div[14]/div/div[2]/table/tbody/tr[6]/td[6]'))
                        ).text)

                        partidos_empatados = int(WebDriverWait(self.driver, 5).until(
                            EC.presence_of_element_located((By.XPATH, '/html/body/main/section[2]/div[2]/div[14]/div/div[2]/table/tbody/tr[6]/td[7]'))
                        ).text)

                        partidos_perdidos = int(WebDriverWait(self.driver, 5).until(
                            EC.presence_of_element_located((By.XPATH, '/html/body/main/section[2]/div[2]/div[14]/div/div[2]/table/tbody/tr[6]/td[8]'))
                        ).text)

                        goles_a_favor = int(WebDriverWait(self.driver, 5).until(
                            EC.presence_of_element_located((By.XPATH, '/html/body/main/section[2]/div[2]/div[14]/div/div[2]/table/tbody/tr[6]/td[9]'))
                        ).text)

                        goles_en_contra = int(WebDriverWait(self.driver, 5).until(
                            EC.presence_of_element_located((By.XPATH, '/html/body/main/section[2]/div[2]/div[14]/div/div[2]/table/tbody/tr[6]/td[10]'))
                        ).text)

                        # Obtener la diferencia de goles
                        diferencia_goles_text = WebDriverWait(self.driver, 5).until(
                            EC.presence_of_element_located((By.XPATH, '/html/body/main/section[2]/div[2]/div[14]/div/div[2]/table/tbody/tr[6]/td[11]'))
                        ).text

                        # Remover el signo '+' si está presente
                        if diferencia_goles_text.startswith('+'):
                            diferencia_goles_text = diferencia_goles_text[1:]

                        diferencia_goles = int(diferencia_goles_text)

                    else:
                        tabla = WebDriverWait(self.driver, 5).until(
                            EC.presence_of_element_located((By.XPATH, '/html/body/main/section[2]/div[2]/div[14]/div/div[2]/table/tbody'))
                        )

                        nombre_element = WebDriverWait(self.driver, 5).until(
                            EC.presence_of_element_located((By.XPATH, '/html/body/main/section[1]/div/div[1]/div[1]/div/h2'))
                        )
                        nombre = unidecode(nombre_element.text)

                        puntos = int(WebDriverWait(self.driver, 5).until(
                            EC.presence_of_element_located((By.XPATH, '/html/body/main/section[2]/div[2]/div[14]/div/div[2]/table/tbody/tr[4]/td[4]/strong'))
                        ).text)

                        partidos = int(WebDriverWait(self.driver, 5).until(
                            EC.presence_of_element_located((By.XPATH, '/html/body/main/section[2]/div[2]/div[14]/div/div[2]/table/tbody/tr[4]/td[5]'))
                        ).text)

                        partidos_ganados = int(WebDriverWait(self.driver, 5).until(
                            EC.presence_of_element_located((By.XPATH, '/html/body/main/section[2]/div[2]/div[14]/div/div[2]/table/tbody/tr[4]/td[6]'))
                        ).text)

                        partidos_empatados = int(WebDriverWait(self.driver, 5).until(
                            EC.presence_of_element_located((By.XPATH, '/html/body/main/section[2]/div[2]/div[14]/div/div[2]/table/tbody/tr[4]/td[7]'))
                        ).text)

                        partidos_perdidos = int(WebDriverWait(self.driver, 5).until(
                            EC.presence_of_element_located((By.XPATH, '/html/body/main/section[2]/div[2]/div[14]/div/div[2]/table/tbody/tr[4]/td[8]'))
                        ).text)

                        goles_a_favor = int(WebDriverWait(self.driver, 5).until(
                            EC.presence_of_element_located((By.XPATH, '/html/body/main/section[2]/div[2]/div[14]/div/div[2]/table/tbody/tr[4]/td[9]'))
                        ).text)

                        goles_en_contra = int(WebDriverWait(self.driver, 5).until(
                            EC.presence_of_element_located((By.XPATH, '/html/body/main/section[2]/div[2]/div[14]/div/div[2]/table/tbody/tr[4]/td[10]'))
                        ).text)

                        # Obtener la diferencia de goles
                        diferencia_goles_text = WebDriverWait(self.driver, 5).until(
                            EC.presence_of_element_located((By.XPATH, '/html/body/main/section[2]/div[2]/div[14]/div/div[2]/table/tbody/tr[4]/td[11]'))
                        ).text

                        # Remover el signo '+' si está presente
                        if diferencia_goles_text.startswith('+'):
                            diferencia_goles_text = diferencia_goles_text[1:]

                        diferencia_goles = int(diferencia_goles_text)               

                    # Almacenar los datos del equipo en un diccionario
                    datos_equipo = {
                        'nombre': nombre,
                        'partidos': partidos,
                        'puntos': puntos,
                        'partidos_ganados': partidos_ganados,
                        'partidos_empatados': partidos_empatados,
                        'partidos_perdidos': partidos_perdidos,
                        'goles_a_favor': goles_a_favor,
                        'goles_en_contra': goles_en_contra,
                        'diferencia_goles': diferencia_goles
                    }
                    #print(datos_equipo)
                    bbdd.MySQL.insertar_equipo_bbdd(datos_equipo) 

                except Exception as e:
                    pass
                    print(f"No se pudieron obtener los datos del equipo: {link}, Error: {e}")
            #print(lista_datos_equipos)
            return True  # Todos los equipos se han insertado correctamente

        except Exception as e:
            print(f"Error en el método datos_equipos: {str(e)}")
            return []
