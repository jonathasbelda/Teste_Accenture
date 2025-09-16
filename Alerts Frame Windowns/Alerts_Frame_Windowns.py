from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import time


# Configurações do Chrome
def instanciar_chrome():
    driver = webdriver.Chrome()  # Instancializar o Chrome
    driver.implicitly_wait(10)
    driver.maximize_window()  # maximizar a janela do chrome
    driver.get("https://demoqa.com")  # Abrir a página demoqa
    time.sleep(2)
    return driver


# clicar em Alerts, Frame & Windows e abrir uma nova aba
def alerts(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    
    #abrir menu alerts, frame & windows
    driver.find_element(By.XPATH, "//*[@id='app']/div/div/div[2]/div/div[3]/div/div[3]").click()  
    time.sleep(2)
    
    #clicar em Browser Windows
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/div/div[3]/div/ul/li[1]").click()  
    time.sleep(1)
    
    #clicar em New windows
    driver.find_element(By.ID, "tabButton").click()    
    time.sleep(2)
    
    #mudar para a nova aba
    driver.switch_to.window(driver.window_handles[1]) 
    #imprimir o texto da nova aba
    print(driver.find_element(By.ID, "sampleHeading").text)  
    time.sleep(2)
    
    #fechar a nova aba
    driver.close()  
    #voltar para a aba original
    driver.switch_to.window(driver.window_handles[0]) 
    time.sleep(2)
    
 
# Chamada da função
driver = instanciar_chrome()
alerts(driver)

driver.quit()

