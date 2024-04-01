from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class scraper:
    def __init__(self, chromedriver_path, url):
        self.chromedriver_path = chromedriver_path
        self.url = url


    # FUNCIÓN DONDE ABRIMOS LA PÁGINA
    def conexion_url(self, chromedriver_path, url):
        option = Options()  # Aquí definiste la variable como 'option'
        option.add_argument('--disable-notifications')
        
        driver = webdriver.Chrome(chromedriver_path, options=option)  
        driver.get(url)
        driver.maximize_window()
        return driver

    # FUNCIÓN DONDE ACEPTAOS LAS COCKIES EN BESOCCER
    def aceptar_cookies_besoccer(self):
        try:
            accept_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="qc-cmp2-ui"]/div[2]/div/button[3]')))
            
            accept_button.click()
            print("Cookies aceptadas.")
        except Exception as e:
            print("No fue necesario aceptar cookies o no se encontró el botón.", e)


    def inicializar_pagina_besoccer(self):
        self.driver = self.conexion_url(self.chromedriver_path, self.url)
        self.wait = WebDriverWait(self.driver, 10)  # Inicializa WebDriverWait aquí
        self.aceptar_cookies_besoccer()
    
    def close(self):
        self.driver.quit()



