from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

class arbitro:
    def chromedriver():
        # Configuración del navegador
        options = Options()
        options.add_argument('--disable-notifications')

        # Ruta al controlador de Chrome
        s = Service('chromedriver-win64/chromedriver.exe')

        # Crear una instancia de ChromeDriver
        driver = webdriver.Chrome(service=s, options=options)
        return driver
    
    def hide_ads(driver):
        # Puedes agregar aquí cualquier lógica para identificar los elementos de anuncios,
        # por ejemplo, mediante clases CSS
        # Aquí hay un ejemplo de cómo ocultar elementos que contienen la palabra "anuncio" en su clase
        driver.execute_script('''
            var elements = document.querySelectorAll('[class*="anuncio"]');
            elements.forEach(function(element) {
                element.style.display = 'none';
            });
        ''')

    def aceptar_cookies_besoccer(driver):
        try:
            accept_button = driver.wait.until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="qc-cmp2-ui"]/div[2]/div/button[3]'))
            )

            accept_button.click()
            print("Cookies aceptadas.")
        except Exception as e:
            print("No fue necesario aceptar cookies o no se encontró el botón.", e)



    def obtener_datos_arbitros(driver):
        datos_arbitros = []
        for index in range(3, 23):
            try:
                xpath = f'//*[@id="mod_referees"]/div/table/tbody/tr[{index}]/td[2]/a'
                element = driver.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
                driver.execute_script("arguments[0].scrollIntoView(true);", element)
                driver.execute_script("arguments[0].click();", element)

                datos_arbitro = {
                    'arbitro': driver.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="mod_detail_head_referee"]/div[1]/div/div[1]/div/h2'))).text,
                    'partidos_jugados': driver.find_element_by_xpath('//*[@id="mod_referee_stats"]/div/div[2]/div[2]/div/div/div[1]/div[2]').text,
                    'penaltis_pitados': driver.find_element_by_xpath('//*[@id="mod_referee_stats"]/div/div[2]/div[2]/div/div/div[2]/div[2]').text,
                    'p_penalti': driver.find_element_by_xpath('//*[@id="mod_referee_stats"]/div/div[2]/div[2]/div/div/div[2]/div[3]').text,
                    'tarjetas_amarillas': driver.find_element_by_xpath('//*[@id="mod_referee_stats"]/div/div[2]/div[2]/div/div/div[3]/div[2]').text,
                    'p_amarilla': driver.find_element_by_xpath('//*[@id="mod_referee_stats"]/div/div[2]/div[2]/div/div/div[3]/div[3]').text,
                    'tarjetas_rojas': driver.find_element_by_xpath('//*[@id="mod_referee_stats"]/div/div[2]/div[2]/div/div/div[4]/div[2]').text,
                    'p_roja': driver.find_element_by_xpath('//*[@id="mod_referee_stats"]/div/div[2]/div[2]/div/div/div[4]/div[3]').text,
                    'doble_amarilla': driver.find_element_by_xpath('//*[@id="mod_referee_stats"]/div/div[2]/div[2]/div/div/div[5]/div[2]').text,
                    'p_doble_amarilla': driver.find_element_by_xpath('//*[@id="mod_referee_stats"]/div/div[2]/div[2]/div/div/div[5]/div[3]').text
                }
                datos_arbitros.append(datos_arbitro)
                print("Todo bien")

                driver.back()
            except Exception as e:
                print(f"Error al procesar el árbitro en el índice {index}: {e}")

        return datos_arbitros

