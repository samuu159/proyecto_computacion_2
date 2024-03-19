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
import mysql.connector
import bbdd
from unidecode import unidecode

class JugadoresAbstractos(ABC):
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
    def link_jugadores(self):
        pass

    @abstractmethod
    def datos_jugadores(self):
        pass

class Jugadores(JugadoresAbstractos):
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

    def link_jugadores(self):
        try:
            self.hide_ads()

            boton = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="content"]/header/div[2]/ul/li[5]'))
            )
            boton.click()
            self.hide_ads()

            boton = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div[4]/div[1]/button[2]'))
            )
            boton.click()
            #self.refresh_page()
            self.hide_ads()

            # Esperar a que los botones en el bucle sean visibles y hacer clic en ellos
            seguir = True
            while seguir:
                try:
                    time.sleep(2)
                    boton = WebDriverWait(self.driver, 5).until(
                        EC.visibility_of_element_located((By.XPATH, '/html/body/div[7]/div[3]/div[3]/div[1]/button'))
                    )
                    boton.click()
                    print("Botón 'Siguiente' clicado.")
                except TimeoutException as e:
                    print("TimeoutException: ", e)
                    seguir = False
                except Exception as e:
                    print("Otra excepción:", e)
                    seguir = False

            lista_jugadores = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_all_elements_located((By.CLASS_NAME, 'player-row'))
            )

            link_jugadores = []
            for jugador in lista_jugadores:
                try:
                    enlace_jugador = WebDriverWait(jugador, 5).until(
                        EC.visibility_of_element_located((By.CLASS_NAME, 'btn-sw-link'))
                    )
                    href_attribute = enlace_jugador.get_attribute('href')
                    link_jugadores.append(href_attribute)

                except Exception as e:
                    print(f"Error: {e}")

            #print(link_jugadores)
            return link_jugadores
        except Exception as e:
            print(f"Error en el método some_method: {str(e)}")

    def datos_jugadores(self):
        try:
            links_jugadores = self.link_jugadores()
            lista_datos_jugadores = []  # Lista para almacenar los datos de todos los jugadores

            for link in links_jugadores:
                self.driver.get(link)
                try:
                        # Esperar a que aparezcan los elementos de nombre y apellido
                    try:

                        #Cambiar a partir de aqui!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                        
                        # Intenta encontrar el elemento del nombre del jugador
                        nombre_element = WebDriverWait(self.driver, 5).until(
                            EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div[5]/div[1]/div/div[1]/div[2]'))
                        )
                        
                        # Si se encuentra el elemento, obtén el nombre del jugador
                        nombre = unidecode(nombre_element.text)
                        print(nombre)
                    except:
                        # Si no se encuentra el elemento, asigna None al nombre
                        nombre = None
                    
                    try:
                        apellido_element = WebDriverWait(self.driver, 5).until(
                        EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div[5]/div[1]/div/div[1]/div[3]'))
                        )

                        apellido = unidecode(apellido_element.text)
                        print(apellido)

                    except:

                        apellido = None
                        

                    

                    # Esperar a que el enlace de imagen sea visible
                    try:
                        enlace_imagen = WebDriverWait(self.driver, 5).until(
                            EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div[5]/div[1]/div/div[1]/div[1]/a'))
                        )
                        print(enlace_imagen)
                    except:
                        enlace_imagen = None
                        

                    # Obtener el atributo href del enlace de la imagen
                    href_attribute = enlace_imagen.get_attribute('href')

                    numero_equipo = "Equipo Desconocido"

                    # Verificar si el atributo href está presente y no es None
                    if href_attribute:
                        # Utilizar expresión regular para extraer el número del equipo de la URL
                        resultado = re.search(r'/teams/(\d+)/', href_attribute)
                        
                        # Verificar si se encontró el número del equipo
                        if resultado:
                            numero_equipo = resultado.group(1)

                    # Diccionario de mapeo entre números de equipo y nombres de equipo
                    mapeo_equipos = {
                        '48': 'Alavés',
                        '21': 'Almería',
                        '1': 'Athletic Club',
                        '2': 'Atlético',
                        '3': 'Barcelona',
                        '4': 'Betis',
                        '499': 'Cádiz',
                        '5': 'Celta',
                        '9': 'Getafe',
                        '222': 'Girona',
                        '10': 'Granada',
                        '11': 'Las Palmas',
                        '408': 'Mallorca',
                        '50': 'Osasuna',
                        '14': 'Rayo Vallecano',
                        '15': 'Real Madrid',
                        '16': 'Real Sociedad',
                        '17': 'Sevilla',
                        '19': 'Valencia',
                        '20': 'Villarreal',
                    }

                    # Obtener el nombre del equipo a partir del número usando el diccionario de mapeo
                    nombre_equipo = mapeo_equipos.get(numero_equipo, "Equipo Desconocido")

                    posicion = WebDriverWait(self.driver, 5).until(
                        EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div[5]/div[1]/div/div[1]/div[1]/i'))
                    )
                    clases_css = posicion.get_attribute('class')

                    if 'pos-1' in clases_css and 'pos-big' in clases_css:
                        posicion = 'Portero'
                    elif 'pos-2' in clases_css and 'pos-big' in clases_css:
                        posicion = 'Defensa'
                    elif 'pos-3' in clases_css and 'pos-big' in clases_css:
                        posicion = 'Mediocentro'
                    elif 'pos-4' in clases_css and 'pos-big' in clases_css:
                        posicion = 'Delantero'
                    print(posicion)


                    valor = WebDriverWait(self.driver, 5).until(
                        EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div[5]/div[2]/div/div/div[1]/div[2]'))
                    )
                    valor = valor.text
                    valor = valor.replace('.', '')
                    print(valor)

                    
                    puntos_totales = WebDriverWait(self.driver, 5).until(
                        EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div[5]/div[2]/div/div/div[2]/div[2]'))
                    )
                    puntos_totales = puntos_totales.text
                    print(puntos_totales)

                    media = WebDriverWait(self.driver, 5).until(
                        EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div[5]/div[2]/div/div/div[3]/div[2]'))
                    )
                    media = media.text
                    media = media.replace(',', '.')
                    print(media)

                    partidos = WebDriverWait(self.driver, 5).until(
                        EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div[5]/div[2]/div/div/div[4]/div[2]'))
                    )
                    partidos = partidos.text
                    print(partidos)

                    goles = WebDriverWait(self.driver, 5).until(
                        EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div[5]/div[2]/div/div/div[5]/div[2]'))
                    )
                    goles = goles.text
                    print(goles)

                    
                    tarjetas = WebDriverWait(self.driver, 5).until(
                        EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div[5]/div[2]/div/div/div[6]/div[2]'))
                    )
                    tarjetas = tarjetas.text
                    print(tarjetas)


                    try:
                        media_en_casa = WebDriverWait(self.driver, 5).until(
                            EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div[6]/div/div[3]/div/div[2]/div[2]'))
                        )

                        media_en_casa = media_en_casa.text
                        media_en_casa = media_en_casa.replace(',', '.')
                        print(media_en_casa)
                    except:
                        media_en_casa = None
                        print(media_en_casa)

                    try:
                        media_fuera = WebDriverWait(self.driver, 5).until(
                            EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div[6]/div/div[3]/div/div[3]/div[2]'))
                        )

                        media_fuera = media_fuera.text
                        media_fuera = media_fuera.replace(',', '.')
                        print(media_fuera)

                    except:
                        media_fuera = None
                        print(media_fuera)


                    try:
                        valor_subido_bajado_element = WebDriverWait(self.driver, 5).until(
                            EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div[6]/div/div[6]/span'))
                        )
                        valor_subido_bajado_text = valor_subido_bajado_element.text.strip()  # Eliminar espacios en blanco al principio y al final
                        valor_subido_bajado_text = valor_subido_bajado_text.replace('.', '')
                        if valor_subido_bajado_text.startswith('↑'):
                            valor_subido_bajado = '' + valor_subido_bajado_text[1:]
                        elif valor_subido_bajado_text.startswith('↓'):
                            valor_subido_bajado = '-' + valor_subido_bajado_text[1:].lstrip()
                        else:
                            valor_subido_bajado = valor_subido_bajado_text

                    except:
                        try:
                            valor_subido_bajado_element = WebDriverWait(self.driver, 5).until(
                                EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div[6]/div/div[4]/span'))
                            )
                            valor_subido_bajado_text = valor_subido_bajado_element.text.strip()  # Eliminar espacios en blanco al principio y al final
                            valor_subido_bajado_text = valor_subido_bajado_text.replace('.', '')
                            if valor_subido_bajado_text.startswith('↑'):
                                valor_subido_bajado = '' + valor_subido_bajado_text[1:]
                            elif valor_subido_bajado_text.startswith('↓'):
                                valor_subido_bajado = '-' + valor_subido_bajado_text[1:].lstrip()
                            else:
                                valor_subido_bajado = valor_subido_bajado_text

                            

                        except:
                            try:
                                valor_subido_bajado_element = WebDriverWait(self.driver, 5).until(
                                    EC.visibility_of_element_located((By.XPATH, '/html/body/div[7]/div[3]/div[3]/div/div[5]/span'))
                                )
                                valor_subido_bajado_text = valor_subido_bajado_element.text.strip()  # Eliminar espacios en blanco al principio y al final
                                valor_subido_bajado_text = valor_subido_bajado_text.replace('.', '')
                                if valor_subido_bajado_text.startswith('↑'):
                                    valor_subido_bajado = '' + valor_subido_bajado_text[1:]
                                elif valor_subido_bajado_text.startswith('↓'):
                                    valor_subido_bajado = '-' + valor_subido_bajado_text[1:].lstrip()
                                else:
                                    valor_subido_bajado = valor_subido_bajado_text
                                
                                

                            except:
                                try:
                                    valor_subido_bajado_element = WebDriverWait(self.driver, 5).until(
                                        EC.visibility_of_element_located((By.XPATH, '/html/body/div[7]/div[3]/div[3]/div[1]/div[6]/span'))
                                    )
                                    valor_subido_bajado_text = valor_subido_bajado_element.text.strip()  # Eliminar espacios en blanco al principio y al final
                                    valor_subido_bajado_text = valor_subido_bajado_text.replace('.', '')
                                    if valor_subido_bajado_text.startswith('↑'):
                                        valor_subido_bajado = '' + valor_subido_bajado_text[1:]
                                    elif valor_subido_bajado_text.startswith('↓'):
                                        valor_subido_bajado = '-' + valor_subido_bajado_text[1:].lstrip()
                                    else:
                                        valor_subido_bajado = valor_subido_bajado_text

                                    

                                except:
                                    valor_subido_bajado_element = "0"
                    print(valor_subido_bajado)                

                    # Espera a que la lista de jornadas esté presente
                    #try:
                        #lista_jornadas = WebDriverWait(self.driver, 5).until(
                            #EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[6]/div/div[9]'))
                        #)
                    #except:
                        #try:
                            #lista_jornadas = WebDriverWait(self.driver, 5).until(
                                #EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[6]/div/div[7]'))
                            #)
                            
                        #except:
                            #lista_jornadas = WebDriverWait(self.driver, 5).until(
                                #EC.presence_of_element_located((By.XPATH, '/html/body/div[7]/div[3]/div[3]/div[1]/div[9]'))
                            #)
                            



                    # Localiza los elementos que contienen los valores de las jornadas
                    jornadas = WebDriverWait(self.driver, 5).until(
                        EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.line.btn.btn-player-gw'))
                    )

                    

                    # Inicializamos las variables de jornada
                    jornada_1 = jornada_2 = jornada_3 = jornada_4 = jornada_5 = jornada_6 = jornada_7 = jornada_8 = jornada_9 = jornada_10 = None
                    jornada_11 = jornada_12 = jornada_13 = jornada_14 = jornada_15 = jornada_16 = jornada_17 = jornada_18 = jornada_19 = jornada_20 = None
                    jornada_21 = jornada_22 = jornada_23 = jornada_24 = jornada_25 = jornada_26 = jornada_27 = jornada_28 = jornada_29 = jornada_30 = None
                    jornada_31 = jornada_32 = jornada_33 = jornada_34 = jornada_35 = jornada_36 = jornada_37 = jornada_38 = None

                    # Ahora asignamos valores a las jornadas que tengan datos disponibles
                    puntos = []
                    for jornada_index in range(28, 0, -1):  # Comenzamos desde la jornada 26 hasta la jornada 1 en orden descendente
                        jornada = jornadas[jornada_index - 1]  # Accedemos a la jornada correspondiente en la lista

                        # Esperamos a que el elemento del número de jornada sea visible
                        numero_jornada_elemento = WebDriverWait(jornada, 5).until(
                            EC.visibility_of_element_located((By.CLASS_NAME, 'gw'))
                        )

                        # Verificamos si el elemento 'score' existe
                        try:
                            # Esperamos a que el elemento sea visible
                            puntos_element = WebDriverWait(jornada, 5).until(
                                EC.visibility_of_element_located((By.CLASS_NAME, 'bar'))
                            )
                            puntos.append(puntos_element.text.strip())  # Agregamos los puntos a la lista

                        except:
                            # Si no hay puntos, verificamos si hay un elemento con la clase "status"
                            try:
                                # Esperamos a que el elemento sea visible
                                puntos_element = WebDriverWait(jornada, 5).until(
                                    EC.visibility_of_element_located((By.CLASS_NAME, 'bar.negative'))
                                )
                                puntos.append(puntos_element.text.strip())  # Agregamos los puntos a la lista

                            except:
                                puntos.append(None)  # Agregamos None si no hay puntos
                                print(f"No se encontraron puntos para la jornada {jornada_index}")

                    # Asignamos los datos de las jornadas a las variables correspondientes
                    jornada_1, jornada_2, jornada_3, jornada_4, jornada_5, jornada_6, jornada_7, jornada_8, jornada_9, jornada_10 = puntos[:10]
                    jornada_11, jornada_12, jornada_13, jornada_14, jornada_15, jornada_16, jornada_17, jornada_18, jornada_19, jornada_20 = puntos[10:20]
                    jornada_21, jornada_22, jornada_23, jornada_24, jornada_25, jornada_26, jornada_27, jornada_28 = puntos[20:28]  # Solo asignamos valores hasta la jornada 26

                    datos_jugador = {
                        "nombre": nombre,
                        "apellido": apellido,
                        "nombre_equipo": nombre_equipo,
                        "posicion": posicion,
                        "valor": valor,
                        "puntos_totales": puntos_totales,
                        "media": media,
                        "partidos": partidos,
                        "goles": goles,
                        "tarjetas": tarjetas,
                        "media_en_casa": media_en_casa,
                        "media_fuera": media_fuera,
                        "valor_subido_bajado": valor_subido_bajado,
                        "mercado": None,
                        "puntos_predicción": None, 
                        "valor_predicción": None,
                        "jornada_1": jornada_1,
                        "jornada_2": jornada_2,
                        "jornada_3": jornada_3,
                        "jornada_4": jornada_4,
                        "jornada_5": jornada_5,
                        "jornada_6": jornada_6,
                        "jornada_7": jornada_7,
                        "jornada_8": jornada_8,
                        "jornada_9": jornada_9,
                        "jornada_10": jornada_10,
                        "jornada_11": jornada_11,
                        "jornada_12": jornada_12,
                        "jornada_13": jornada_13,
                        "jornada_14": jornada_14,
                        "jornada_15": jornada_15,
                        "jornada_16": jornada_16,
                        "jornada_17": jornada_17,
                        "jornada_18": jornada_18,
                        "jornada_19": jornada_19,
                        "jornada_20": jornada_20,
                        "jornada_21": jornada_21,
                        "jornada_22": jornada_22,
                        "jornada_23": jornada_23,
                        "jornada_24": jornada_24,
                        "jornada_25": jornada_25,
                        "jornada_26": jornada_26,
                        "jornada_27": jornada_27,
                        "jornada_28": jornada_28,
                        "jornada_29": jornada_29,
                        "jornada_30": jornada_30,
                        "jornada_31": jornada_31,
                        "jornada_32": jornada_32,
                        "jornada_33": jornada_33,
                        "jornada_34": jornada_34,
                        "jornada_35": jornada_35,
                        "jornada_36": jornada_36,
                        "jornada_37": jornada_37,
                        "jornada_38": jornada_38,
                    }

                    lista_datos_jugadores.append(datos_jugador)  # Agrega el diccionario de datos del jugador a la lista


                except:
                    pass
                    print(f"No se pudo obtener los datos del jugador: {link}")

            return lista_datos_jugadores  # Retorna la lista de datos de todos los jugadores al final
        
        except Exception as e:
            print(f"Error en el método some_method: {str(e)}")

