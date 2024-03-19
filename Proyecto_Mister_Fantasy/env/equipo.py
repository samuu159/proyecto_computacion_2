from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from unidecode import unidecode
import re
import time
import mysql.connector

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
        boton = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "didomi-notice-agree-button"))
        )
        # Hacer clic en el botón
        boton.click()
    except Exception as e:
        print(f"Error al aceptar las cookies: {str(e)}")

    # Inicio de sesión o registro, si es necesario
    try:
        boton = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/button'))
        )
        boton.click()

        boton = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/button'))
        )
        boton.click()

        boton = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/button'))
        )
        boton.click()

        boton = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/button'))
        )
        boton.click()

        boton = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/button[3]'))
        )
        boton.click()

        campo_email = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="email"]'))
        )
        # Escribir en el campo de entrada de correo electrónico
        campo_email.send_keys("ivangarciamoriones23@gmail.com")

        # Esperar hasta que el campo de entrada de contraseña esté presente y sea visible
        campo_contraseña = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div[2]/div/form/div[2]/input'))
        )
        # Escribir en el campo de entrada de contraseña
        campo_contraseña.send_keys("Cloe2016!")

        boton = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div[2]/div/form/div[3]/button'))
        )
        boton.click()


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
    boton = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/header/div[2]/ul/li[3]/a'))
        )
    boton.click()
    hide_ads()
    lista_jugadores = WebDriverWait(driver, 10).until(
        EC.visibility_of_all_elements_located((By.XPATH, '/html/body/div[3]/div[2]/div[4]/ul/li'))
    )

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

    # Recorre el array de enlaces e imprime cada enlace
    for link in link_jugadores:
        driver.get(link)
        
        conexion = mysql.connector.connect(
        host="bxlfjozyadylicrojiil-mysql.services.clever-cloud.com",
        user="uvbui3pydp3dtywa",
        password="RlFkyyTF3rhbD2AppQHU",
        database="bxlfjozyadylicrojiil"
        )
        print(conexion)

        
        try:
            time.sleep(1)
            # Esperar a que aparezcan los elementos de nombre y apellido
            nombre_element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div[5]/div[1]/div/div[1]/div[2]'))
            )
            apellido_element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div[5]/div[1]/div/div[1]/div[3]'))
            )

            # Obtener el texto de los elementos de nombre y apellido
            nombre = unidecode(nombre_element.text)
            apellido = unidecode(apellido_element.text)
            
                
            datos_jugador = {

                "nombre": nombre,
                "apellido": apellido,
  
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
                    # Definir la consulta SQL para actualizar el Id_usuario
                    consulta = "UPDATE Usuarios SET Id_usuario = %s WHERE nombre = %s AND apellido = %s"

                    parametros = (
                    datos_jugador["nombre"],
                    datos_jugador["apellido"]
                    )


                    # Ejecutar la consulta para actualizar el Id_usuario
                    cursor.execute(consulta, (Id_usuario,) + parametros)

                    # Confirmar la transacción
                    conexion.commit()

                    # Cerrar el cursor y la conexión
                    cursor.close()
                    conexion.close()

                    print("Se ha actualizado el Id_usuario para el usuario {} {} con el valor: {}".format(nombre, apellido, Id_usuario))

                else:
                    # Definir la consulta SQL para insertar datos
                    print("No se ha encontrado el jugador {} {}".format(nombre, apellido))
            finally:
                # Cerrar el cursor y la conexión
                if cursor:
                    cursor.close()
                if conexion:
                    conexion.close()

        except Exception as e:
            print(f"Error: {e}")




    # Cerrar el navegador al finalizar
    driver.quit()


if __name__ == '__main__':
    ejecutar_scrapeo()