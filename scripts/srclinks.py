import time
from config import URL
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

def iniciar_driver():
    # Instala o ChromeDriver correspondente à versão atual do seu navegador Chrome
    servico = Service(ChromeDriverManager().install())

    # Inicia o WebDriver com o serviço configurado
    driver = webdriver.Chrome(service=servico)
    return driver

def encontrar_links(driver):
    # Faz a requisição da página web em que contém o anexo a ser baixado
    driver.get(URL)
    pdf_links = []
    
    # Espera até o pop-up de cookies aparecer e ser clicado
    try:
        cookies = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div/div/div/div/div[2]/button[3]'))
        )
        cookies.click()
        print("Pop-up de cookies fechado")
    except Exception as e:
        print(f"Erro ao fechar o pop-up de cookies: {e}")
    

    # Verifica as variáveis de tag 'a' para salvar os pdfs
    links = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.TAG_NAME, 'a'))
    )

    for link in links:
        href = link.get_attribute('href')
        if href and href.endswith('.pdf'):
            # Filtra os links para pegar apenas os dois PDFs específicos 
            if 'Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf' in href or "Anexo_II_DUT_2021_RN_465.2021_RN628.2025_RN629.2025.pdf" in href: 
                pdf_links.append(href)
    
    print(f"Links dos PDFs encontrados: '{pdf_links}'")
    return pdf_links