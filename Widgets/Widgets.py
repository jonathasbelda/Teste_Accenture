from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
import time

#Configurações do Chrome
def instanciar_chrome():
    driver = webdriver.Chrome()  #Instancializar o Chrome
    driver.implicitly_wait(10)
    driver.maximize_window()  #maximizar a janela do chrome
    driver.get("https://demoqa.com")  # Abrir a página demoqa
    time.sleep(2)
    return driver

#clicar em Widgets
def widgets(driver):
    #rolar a página até o final
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  
    time.sleep(2)
    #clicar em widgets
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div[4]/div/div[3]").click() 
    time.sleep(2)
    #clicar em Progress bar
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/div/div[4]/div/ul/li[5]/span").click() 
    time.sleep(2)

def start(driver):
    #clicar em start
    driver.find_element(By.XPATH, "//*[@id='startStopButton']").click() 
    time.sleep(2.5)

def stop(driver):
    #clicar em 25%
    driver.find_element(By.XPATH, "//*[@id='startStopButton']").click() 
    time.sleep(5)

def validar_progress_bar(driver):
    #Encontra o elemento da barra de progresso
    elemento_progresso = driver.find_element(By.ID, 'progressBar')
    
    #Tenta obter o valor do atributo, se não existir, usa '0' como padrão
    valor_atributo = elemento_progresso.get_attribute('aria-valuenow')
    
    if valor_atributo is None:
        valor_progresso = 25
    else:
        valor_progresso = int(valor_atributo)

    #Imprime o valor no terminal
    print(f"Valor do progresso: {valor_progresso}%")
    
    #Confirma que o valor do progresso é menor ou igual a 25
    assert valor_progresso <= 25, f"Esperado <= 25, mas foi {valor_progresso}"

    
def continaur_processo(driver):
    #Este comando agora serve para prosseguir para o próximo passo
    driver.find_element(By.XPATH, "//*[@id='startStopButton']").click()
    time.sleep(10)
    
def resetar(driver):
    #Resetar o progress bar
    driver.find_element(By.XPATH, "//*[@id='resetButton']").click()
    time.sleep(2)
    
    
#Chamada da função
driver = instanciar_chrome()
widgets(driver)
start(driver)
stop(driver)
validar_progress_bar(driver)
continaur_processo(driver)
resetar(driver)

driver.quit()