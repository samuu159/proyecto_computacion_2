from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException
from unidecode import unidecode
import re
import time
import mysql.connector


def refresh_page(driver):
    driver.refresh()

def ejecutar_scrapeo():
    # Configuración del navegador
    options = Options()
    options.add_argument('--disable-notifications')

    # Ruta al controlador de Chrome
    s=Service('chromedriver-win64/chromedriver.exe')

    # Crear una instancia de ChromeDriver
    driver = webdriver.Chrome(service=s, options=options)

    def hide_ads():
    # Puedes agregar aquí cualquier lógica para identificar los elementos de anuncios, por ejemplo, mediante clases CSS
    # Aquí hay un ejemplo de cómo ocultar elementos que contienen la palabra "anuncio" en su clase
        driver.execute_script('''
            var elements = document.querySelectorAll('[class*="anuncio"]');
            elements.forEach(function(element) {
                element.style.display = 'none';
            });
    ''')
        
    
    # Navegar a la URL
    driver.get('https://mister.mundodeportivo.com')
    time.sleep(2)
    # Aceptar cookies
    try:
        boton = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "didomi-notice-agree-button"))
        )
        # Hacer clic en el botón
        boton.click()
    except Exception as e:
        print(f"Error al aceptar las cookies: {str(e)}")
    hide_ads()
    # Inicio de sesión o registro, si es necesario
    try:
        boton = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/button'))
        )
        boton.click()

        boton = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/button'))
        )
        boton.click()

        boton = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/button'))
        )
        boton.click()

        boton = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/button'))
        )
        boton.click()

        boton = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/button[3]'))
        )
        boton.click()

        campo_email = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="email"]'))
        )
        # Escribir en el campo de entrada de correo electrónico
        campo_email.send_keys("ivangarciamoriones23@gmail.com")

        # Esperar hasta que el campo de entrada de contraseña esté presente y sea visible
        campo_contraseña = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div[2]/div/form/div[2]/input'))
        )
        # Escribir en el campo de entrada de contraseña
        campo_contraseña.send_keys("Cloe2016!")

        boton = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div[2]/div/form/div[3]/button'))
        )
        boton.click()
        hide_ads()

    except Exception as e:
        print(f"Error en el inicio de sesión o registro: {str(e)}")

    conexion = mysql.connector.connect(
        host="bxlfjozyadylicrojiil-mysql.services.clever-cloud.com",
        user="uvbui3pydp3dtywa",
        password="RlFkyyTF3rhbD2AppQHU",
        database="bxlfjozyadylicrojiil"
    )
    print(conexion)

    # Crear un cursor para ejecutar consultas
    cursor = conexion.cursor()

    # Definir la consulta SQL
    consulta = "SELECT Id_usuario FROM Usuarios WHERE Correo = %s"

    # Supongamos que el correo electrónico está almacenado en la variable correo
    correo = "ivangarciamoriones23@gmail.com"

    # Ejecutar la consulta con el correo como parámetro
    cursor.execute(consulta, (correo,))

    # Obtener el resultado de la consulta
    resultado = cursor.fetchone()

    # Cerrar el cursor y la conexión
    cursor.close()
    conexion.close()

    # Si se encontró un resultado, imprimir el ID de usuario
    if resultado:
        Id_usuario = resultado[0]
        print("El ID de usuario para el correo {} es: {}".format(correo, Id_usuario))
    else:
        print("No se encontró ningún usuario con el correo {}".format(correo))


    hide_ads()
    boton = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="content"]/header/div[2]/ul/li[5]'))
        )
    boton.click()
    hide_ads()
    
    boton = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div[4]/div[1]/button[2]'))
        )
    boton.click()
    refresh_page(driver)
    hide_ads()
 
    # Esperar a que los botones en el bucle sean visibles y hacer clic en ellos
    seguir = True
    while seguir:
        try:
            time.sleep(2)
            boton = WebDriverWait(driver, 5).until(
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


    lista_jugadores = WebDriverWait(driver, 5).until(
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

    

    for link in link_jugadores:
        driver.get(link)
        try:
            try:
                conexion = mysql.connector.connect(
                host="bxlfjozyadylicrojiil-mysql.services.clever-cloud.com",
                user="uvbui3pydp3dtywa",
                password="RlFkyyTF3rhbD2AppQHU",
                database="bxlfjozyadylicrojiil"
                )
                print("conexion establecida")
            
            except mysql.connector.Error as error:
                print("Error al conectar a la base de datos:", error)
            
                # Esperar a que aparezcan los elementos de nombre y apellido
            try:
                # Intenta encontrar el elemento del nombre del jugador
                nombre_element = WebDriverWait(driver, 5).until(
                    EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div[5]/div[1]/div/div[1]/div[2]'))
                )
                
                # Si se encuentra el elemento, obtén el nombre del jugador
                nombre = unidecode(nombre_element.text)
            except:
                # Si no se encuentra el elemento, asigna None al nombre
                nombre = None
                #print("No se pudo encontrar el nombre del jugador.")
            
            try:
                apellido_element = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div[5]/div[1]/div/div[1]/div[3]'))
                )

                apellido = unidecode(apellido_element.text)

            except:
                apellido_element = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, '/html/body/div[4]/div[5]/div[1]/div/div[1]/div[3]'))
                )

                apellido = unidecode(apellido_element.text)
                

            

            # Esperar a que el enlace de imagen sea visible
            try:
                enlace_imagen = WebDriverWait(driver, 5).until(
                    EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div[5]/div[1]/div/div[1]/div[1]/a'))
                )
            except:
                enlace_imagen = WebDriverWait(driver, 5).until(
                    EC.visibility_of_element_located((By.XPATH, '/html/body/div[4]/div[5]/div[1]/div/div[1]/div[1]/a'))
                )
                

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

            posicion = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div[5]/div[1]/div/div[1]/div[1]/i'))
            )
            posicion = posicion.text

            valor = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div[5]/div[2]/div/div/div[1]/div[2]'))
            )
            valor = valor.text
            valor = valor.replace('.', '')

            puntos_totales = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div[5]/div[2]/div/div/div[2]/div[2]'))
            )
            puntos_totales = puntos_totales.text

            media = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div[5]/div[2]/div/div/div[3]/div[2]'))
            )
            media = media.text
            media = media.replace(',', '.')

            partidos = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div[5]/div[2]/div/div/div[4]/div[2]'))
            )
            partidos = partidos.text

            goles = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div[5]/div[2]/div/div/div[5]/div[2]'))
            )
            goles = goles.text

            tarjetas = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div[5]/div[2]/div/div/div[6]/div[2]'))
            )
            tarjetas = tarjetas.text

                    
            try: 
                media_en_casa = WebDriverWait(driver, 5).until(
                    EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div[6]/div/div[3]/div/div[2]/div[2]'))
                )
            except:
                media_en_casa = WebDriverWait(driver, 5).until(
                            EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div[6]/div/div[2]/div/div[2]/div[2]'))
                        )
                    

            media_en_casa = media_en_casa.text
            media_en_casa = media_en_casa.replace(',', '.')


            try: 
                media_fuera = WebDriverWait(driver, 5).until(
                    EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div[6]/div/div[3]/div/div[3]/div[2]'))
                )
            except:
                media_fuera = WebDriverWait(driver, 5).until(
                            EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div[6]/div/div[2]/div/div[3]/div[2]'))
                        )
                

            media_fuera = media_fuera.text
            media_fuera = media_fuera.replace(',', '.')




            try:
                valor_subido_bajado_element = WebDriverWait(driver, 5).until(
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
                    valor_subido_bajado_element = WebDriverWait(driver, 5).until(
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
                        valor_subido_bajado_element = WebDriverWait(driver, 5).until(
                            EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div[6]/div/div[3]/span'))
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
                            valor_subido_bajado_element = WebDriverWait(driver, 5).until(
                                EC.visibility_of_element_located((By.XPATH, '/html/body/div[6]/div[3]/div[3]/div[1]/div[4]/span'))
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
                            

            # Espera a que la lista de jornadas esté presente
            try:
                lista_jornadas = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[6]/div/div[9]'))
                )
            except:
                try:
                    lista_jornadas = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[6]/div/div[6]'))
                    )
                    
                except:
                    lista_jornadas = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, '/html/body/div[6]/div[3]/div[3]/div[1]/div[7]'))
                    )
                    



            # Localiza los elementos que contienen los valores de las jornadas
            jornadas = WebDriverWait(driver, 5).until(
                EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.line.btn.btn-player-gw'))
            )

            

            # Inicializamos las variables de jornada
            jornada_1 = jornada_2 = jornada_3 = jornada_4 = jornada_5 = jornada_6 = jornada_7 = jornada_8 = jornada_9 = jornada_10 = None
            jornada_11 = jornada_12 = jornada_13 = jornada_14 = jornada_15 = jornada_16 = jornada_17 = jornada_18 = jornada_19 = jornada_20 = None
            jornada_21 = jornada_22 = jornada_23 = jornada_24 = jornada_25 = jornada_26 = jornada_27 = jornada_28 = jornada_29 = jornada_30 = None
            jornada_31 = jornada_32 = jornada_33 = jornada_34 = jornada_35 = jornada_36 = jornada_37 = jornada_38 = None

            # Ahora asignamos valores a las jornadas que tengan datos disponibles
            puntos = []
            for jornada_index in range(27, 0, -1):  # Comenzamos desde la jornada 26 hasta la jornada 1 en orden descendente
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
            jornada_21, jornada_22, jornada_23, jornada_24, jornada_25, jornada_26, jornada_27 = puntos[20:27]  # Solo asignamos valores hasta la jornada 26

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




            try:
                # Crear un cursor para ejecutar consultas SQL
                cursor = conexion.cursor()

                # Definir la consulta SQL para verificar la existencia del jugador por nombre y apellido
                consulta_existencia = "SELECT * FROM Jugadores WHERE Nombre = %s AND Apellido = %s"

                # Parámetros de la consulta
                parametros = (
                    datos_jugador["nombre"],
                    datos_jugador["apellido"]
                )

                # Ejecutar la consulta para verificar la existencia del jugador
                cursor.execute(consulta_existencia, parametros)

                # Obtener el resultado de la consulta
                resultado = cursor.fetchone()

                # Verificar si el jugador ya existe en la tabla
                if resultado:
                    print("El jugador ya existe en la base de datos. No es necesario insertarlo.")
                else:
                    # Construir la consulta SQL
                    placeholders_jornadas = ', '.join(['%s'] * 38)  # Asumiendo que tienes hasta 38 jornadas
                    consulta_insercion = f"INSERT INTO Jugadores (Nombre, Apellido, Equipo, Posicion, Valor, Puntos_totales, Media_total, Partidos, Goles, Tarjetas, Media_en_casa, Media_visitante, Valor_subido_bajado, Mercado, Puntos_predicción, Valor_predicción, Jornada_1, Jornada_2, Jornada_3, Jornada_4, Jornada_5, Jornada_6, Jornada_7, Jornada_8, Jornada_9, Jornada_10, Jornada_11, Jornada_12, Jornada_13, Jornada_14, Jornada_15, Jornada_16, Jornada_17, Jornada_18, Jornada_19, Jornada_20, Jornada_21, Jornada_22, Jornada_23, Jornada_24, Jornada_25, Jornada_26, Jornada_27, Jornada_28, Jornada_29, Jornada_30, Jornada_31, Jornada_32, Jornada_33, Jornada_34, Jornada_35, Jornada_36, Jornada_37, Jornada_38) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, {placeholders_jornadas})"
                    # Parámetros de la consulta de inserción
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


                    # Ejecutar la consulta para insertar datos
                    cursor.execute(consulta_insercion, parametros_insercion)

                    # Confirmar la transacción
                    conexion.commit()
                    print("Datos del jugador insertados correctamente.")


            except mysql.connector.Error as error:
                print("Error al conectar a la base de datos:", error)

            finally:
                # Cerrar el cursor y la conexión
                if cursor:
                    cursor.close()
                if conexion:
                    conexion.close()

        except:
            pass
            print(f"No se pudo insertar los datos del jugador: {link}")
    # Cerrar el navegador al finalizar
    driver.quit()


if __name__ == '__main__':
    ejecutar_scrapeo()