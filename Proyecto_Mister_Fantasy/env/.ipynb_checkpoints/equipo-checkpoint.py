from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException
from unidecode import unidecode
import csv
import re
import time

# Configuración del navegador
options = Options()
options.add_argument('--disable-notifications')

# Ruta al controlador de Chrome (reemplaza con la ubicación de tu controlador)
chrome_driver_path = '../chromedriver-win64/chromedriver.exe'

# Crear una instancia de ChromeDriver
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)

# Navegar a la URL
driver.get('https://mister.mundodeportivo.com')
time.sleep(2)
# Aceptar cookies
try:
    boton = driver.find_element_by_id('didomi-notice-disagree-button')
    boton.click()
    time.sleep(2)
    botones = driver.find_elements_by_css_selector('.didomi-components-button.didomi-button.didomi-button-standard.standard-button')

    if botones:
        botones[0].location_once_scrolled_into_view
        botones[0].click()
except Exception as e:
    print(f"Error al aceptar las cookies: {str(e)}")

# Inicio de sesión o registro, si es necesario
try:
    time.sleep(4)
    boton = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/button')
    boton.click()

    boton = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/button')
    boton.click()

    boton = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/button')
    boton.click()

    boton = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/button')
    boton.click()

    boton = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/button[3]')
    boton.click()

    time.sleep(2)
    campo_input = driver.find_element_by_xpath('//*[@id="email"]')

    # Escribir texto en el campo de entrada
    campo_input.send_keys("ivangarciamoriones23@gmail.com")

    campo_input = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/form/div[2]/input')

    # Escribir texto en el campo de entrada
    campo_input.send_keys("Cloe2016!")
    time.sleep(2)
    boton = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/form/div[3]/button')
    boton.click()
except Exception as e:
    print(f"Error en el inicio de sesión o registro: {str(e)}")



time.sleep(2)
# Localiza el elemento <a> por su atributo href
enlace = driver.find_element_by_xpath('//*[@id="content"]/header/div[2]/ul/li[3]')  # Reemplaza con la URL del enlace
enlace.click()

lista_jugadores = driver.find_elements_by_xpath('/html/body/div[3]/div[2]/div[4]/ul/li')
link_jugadores = []
datos_jugadores = []
for jugador in lista_jugadores:
    try:
        # Dentro de cada iteración, encuentra el enlace con la clase 'btn-sw-link'
        enlace_jugador = jugador.find_element_by_class_name('btn-sw-link')

        # Obtiene el atributo 'href' del enlace y lo agrega al array
        href_attribute = enlace_jugador.get_attribute('href')
        link_jugadores.append(href_attribute)

    except Exception as e:
        print(f"Error: {e}")

# Recorre el array de enlaces e imprime cada enlace
for link in link_jugadores:
    driver.get(link)
    time.sleep(1)
    try:
        time.sleep(1)
        ## Utiliza Selenium para localizar los elementos por su clase
        posicion = driver.find_element_by_xpath('/html/body/div[3]/div[5]/div[1]/div/div[1]/div[1]/i')
        
        enlace_imagen = driver.find_element_by_xpath('/html/body/div[3]/div[5]/div[1]/div/div[1]/div[1]/a')
        img_tag = enlace_imagen.find_element_by_tag_name('img')
        src_attribute = img_tag.get_attribute('src')
        print(src_attribute)


        # Definir la expresión regular para extraer el número del equipo
        expresion_regular = r'(\d+)\.png'

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
        
        # Buscar el número del equipo en el enlace de la imagen
        resultado = re.search(expresion_regular, src_attribute)
        print(resultado)
        nombre_equipo = "Equipo Desconocido"
        # Verificar si se encontró el número del equipo
        if resultado:
            numero_equipo = resultado.group(1)
            # Obtener el nombre del equipo a partir del número usando el diccionario de mapeo
            nombre_equipo = mapeo_equipos.get(numero_equipo, nombre_equipo)

        clases_css = posicion.get_attribute('class')

        if 'pos-1' in clases_css and 'pos-big' in clases_css:
            posicion = 'Portero'
        elif 'pos-2' in clases_css and 'pos-big' in clases_css:
            posicion = 'Defensa'
        elif 'pos-3' in clases_css and 'pos-big' in clases_css:
            posicion = 'Mediocentro'
        elif 'pos-4' in clases_css and 'pos-big' in clases_css:
            posicion = 'Delantero'
        nombre = unidecode(driver.find_element_by_xpath('/html/body/div[3]/div[5]/div[1]/div/div[1]/div[2]').text)  # Reemplaza 'nombre-clase' con la clase real
        apellido = unidecode(driver.find_element_by_xpath('/html/body/div[3]/div[5]/div[1]/div/div[1]/div[3]').text)
        valor = driver.find_element_by_xpath('/html/body/div[3]/div[5]/div[2]/div/div/div[1]/div[2]').text
        puntos_totales = driver.find_element_by_xpath('/html/body/div[3]/div[5]/div[2]/div/div/div[2]/div[2]').text
        media = driver.find_element_by_xpath('/html/body/div[3]/div[5]/div[2]/div/div/div[3]/div[2]').text
        partidos = driver.find_element_by_xpath('/html/body/div[3]/div[5]/div[2]/div/div/div[4]/div[2]').text
        goles = driver.find_element_by_xpath('/html/body/div[3]/div[5]/div[2]/div/div/div[5]/div[2]').text
        tarjetas = driver.find_element_by_xpath('/html/body/div[3]/div[5]/div[2]/div/div/div[6]/div[2]').text
        media_en_casa = driver.find_element_by_xpath('/html/body/div[3]/div[6]/div/div[3]/div/div[2]/div[2]').text
        media_fuera = driver.find_element_by_xpath('/html/body/div[3]/div[6]/div/div[3]/div/div[3]/div[2]').text
        valor_subido_bajado_element = driver.find_element_by_xpath('/html/body/div[3]/div[6]/div/div[6]/span')
        
        valor_subido_bajado_text = valor_subido_bajado_element.text.strip()  # Eliminar espacios en blanco al principio y al final

        if valor_subido_bajado_text.startswith('↑'):
            valor_subido_bajado = '+' + valor_subido_bajado_text[1:]
        elif valor_subido_bajado_text.startswith('↓'):
            valor_subido_bajado = '-' + valor_subido_bajado_text[1:]
        else:
            valor_subido_bajado = valor_subido_bajado_text



        #Falla con ocampos porque no tiene video
        lista_jornadas = driver.find_element_by_xpath('/html/body/div[3]/div[6]/div/div[9]')
        
        # Localiza los elementos que contienen los valores de las jornadas
        jornadas = driver.find_elements_by_class_name('line.btn.btn-player-gw')

        # Crea una lista para almacenar la información relevante de las jornadas
        info_jornadas = []

        for jornada in jornadas:
            numero_jornada = jornada.find_element_by_class_name('gw').text
            # Verifica si el elemento 'score' existe
            puntos_element = jornada.find_elements_by_class_name('bar')
            if puntos_element:
                puntos = puntos_element[0].text
                if puntos.strip() == '':
                    puntos = 'No jugo'
            else:
                # Si no hay puntos, verifica si hay un elemento con la clase "status"
                puntos_element = jornada.find_elements_by_class_name('bar negative')
                if puntos_element:
                    puntos = puntos_element[0].text
            info_jornadas.append(f'{numero_jornada}: Puntos {puntos}')

            
        datos_jugador = {
            "nombre_equipo": nombre_equipo,
            "posicion": posicion,
            "nombre": nombre,
            "apellido": apellido,
            "valor": valor,
            "puntos_totales": puntos_totales,
            "media": media,
            "partidos": partidos,
            "goles": goles,
            "tarjetas": tarjetas,
            "media_en_casa": media_en_casa,
            "media_fuera": media_fuera,
            "valor_subido_bajado": valor_subido_bajado,
            "info_jornadas": info_jornadas,
        }
        datos_jugadores.append(datos_jugador)


        ruta_del_archivo = 'team_data/equipo.csv'

        with open(ruta_del_archivo, 'w', newline='', encoding='utf-8') as archivo_csv:
            campo_nombres = ["nombre_equipo", "posicion", "nombre", "apellido", "valor", "puntos_totales", "media", "partidos", "goles", "tarjetas", "media_en_casa", "media_fuera", "valor_subido_bajado", "info_jornadas"]
            writer = csv.DictWriter(archivo_csv, fieldnames=campo_nombres)
            writer.writeheader()

            for datos_jugador in datos_jugadores:
                writer.writerow(datos_jugador)
        print(f"Los datos se han escrito en {ruta_del_archivo}")


        
    except NoSuchElementException:
        valor_subido_bajado_element = "0"
        lista_jornadas = driver.find_element_by_xpath('/html/body/div[3]/div[6]/div/div[9]')
        
        # Localiza los elementos que contienen los valores de las jornadas
        jornadas = driver.find_elements_by_class_name('line.btn.btn-player-gw')

        # Crea una lista para almacenar la información relevante de las jornadas
        info_jornadas = []

        # Itera a través de los elementos y extrae la información número de jornada y puntos
        for jornada in jornadas:
            numero_jornada = jornada.find_element_by_class_name('gw').text
            # Verifica si el elemento 'score' existe
            puntos_element = jornada.find_elements_by_class_name('bar')
            if puntos_element:
                puntos = puntos_element[0].text
                if puntos.strip() == '':
                    puntos = 'No jugo'
            else:
                # Si no hay puntos, verifica si hay un elemento con la clase "status"
                puntos_element = jornada.find_elements_by_class_name('bar negative')
                if puntos_element:
                    puntos = puntos_element[0].text
            info_jornadas.append(f'{numero_jornada}: Puntos {puntos}')

        datos_jugador = {
            "nombre_equipo": nombre_equipo,
            "posicion": posicion,
            "nombre": nombre,
            "apellido": apellido,
            "valor": valor,
            "puntos_totales": puntos_totales,
            "media": media,
            "partidos": partidos,
            "goles": goles,
            "tarjetas": tarjetas,
            "media_en_casa": media_en_casa,
            "media_fuera": media_fuera,
            "valor_subido_bajado": valor_subido_bajado,
            "info_jornadas": info_jornadas,
        }
        datos_jugadores.append(datos_jugador)


        ruta_del_archivo = 'team_data/equipo.csv'

        with open(ruta_del_archivo, 'w', newline='', encoding='utf-8') as archivo_csv:
            campo_nombres = ["nombre_equipo", "posicion", "nombre", "apellido", "valor", "puntos_totales", "media", "partidos", "goles", "tarjetas", "media_en_casa", "media_fuera", "valor_subido_bajado", "info_jornadas"]
            writer = csv.DictWriter(archivo_csv, fieldnames=campo_nombres)
            writer.writeheader()

            for datos_jugador in datos_jugadores:
                writer.writerow(datos_jugador)
        print(f"Los datos se han escrito en {ruta_del_archivo}")
        
        
        
    except:
        valor_subido_bajado_element = driver.find_element_by_xpath('/html/body/div[6]/div[3]/div[3]/div[1]/div[4]/span')
        valor_subido_bajado_text = valor_subido_bajado_element.text.strip()  # Eliminar espacios en blanco al principio y al final

        if valor_subido_bajado_text.startswith('↑'):
            valor_subido_bajado = '+' + valor_subido_bajado_text[1:]
        elif valor_subido_bajado_text.startswith('↓'):
            valor_subido_bajado = '-' + valor_subido_bajado_text[1:]
        else:
            valor_subido_bajado = valor_subido_bajado_text

            valor_subido_bajado = valor_subido_bajado_text

        lista_jornadas = driver.find_element_by_xpath('/html/body/div[6]/div[3]/div[3]/div[1]/div[7]')
        
        # Localiza los elementos que contienen los valores de las jornadas
        jornadas = driver.find_elements_by_class_name('line.btn.btn-player-gw')

        # Crea una lista para almacenar la información relevante de las jornadas
        info_jornadas = []

        # Itera a través de los elementos y extrae la información de número de jornada y puntos
        for jornada in jornadas:
            numero_jornada = jornada.find_element_by_class_name('gw').text
            # Verifica si el elemento 'score' existe
            puntos_element = jornada.find_elements_by_class_name('bar')
            if puntos_element:
                puntos = puntos_element[0].text
                if puntos.strip() == '':
                    puntos = 'No jugo'
            else:
                # Si no hay puntos, verifica si hay un elemento con la clase "status"
                puntos_element = jornada.find_elements_by_class_name('bar negative')
                if puntos_element:
                    puntos = puntos_element[0].text
            info_jornadas.append(f'{numero_jornada}: Puntos {puntos}')

        datos_jugador = {
            "nombre_equipo": nombre_equipo,
            "posicion": posicion,
            "nombre": nombre,
            "apellido": apellido,
            "valor": valor,
            "puntos_totales": puntos_totales,
            "media": media,
            "partidos": partidos,
            "goles": goles,
            "tarjetas": tarjetas,
            "media_en_casa": media_en_casa,
            "media_fuera": media_fuera,
            "valor_subido_bajado": valor_subido_bajado,
            "info_jornadas": info_jornadas,
        }
        datos_jugadores.append(datos_jugador)


        ruta_del_archivo = 'team_data/equipo.csv'

        with open(ruta_del_archivo, 'w', newline='', encoding='utf-8') as archivo_csv:
            campo_nombres = ["nombre_equipo", "posicion", "nombre", "apellido", "valor", "puntos_totales", "media", "partidos", "goles", "tarjetas", "media_en_casa", "media_fuera", "valor_subido_bajado", "info_jornadas"]
            writer = csv.DictWriter(archivo_csv, fieldnames=campo_nombres)
            writer.writeheader()

            for datos_jugador in datos_jugadores:
                writer.writerow(datos_jugador)
        print(f"Los datos se han escrito en {ruta_del_archivo}")
    
print("FIN")
# Cerrar el navegador al finalizar
driver.quit()
