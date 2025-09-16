from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time

#Configurações do Chrome
def instanciar_chrome():
    driver = webdriver.Chrome()  #Instancializar o Chrome
    driver.implicitly_wait(10)
    driver.maximize_window()  #maximizar a janela do chrome
    driver.get("https://demoqa.com")  # Abrir a página demoqa
    time.sleep(2)
    return driver

#clicar em interactions
def interactions(driver):
    #rolar a página até o final
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    #clicar em interactions
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div[5]/div/div[3]").click() 
    time.sleep(2)
    #clicar em Sortable
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/div/div[5]/div/ul/li[1]").click()
    time.sleep(2)

def ordenar_decrescente(driver):
    #Valor 6 para 1
    six = driver.find_element(By.XPATH, "//*[@id='demo-tabpane-list']/div/div[1]")
    six1 = driver.find_element(By.XPATH, "//*[@id='demo-tabpane-list']/div/div[6]")  
    actions = ActionChains(driver)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    ActionChains(driver).drag_and_drop(six1, six).perform()
    time.sleep(3)

    #Valor 6 para 2
    five = driver.find_element(By.XPATH, "//*[@id='demo-tabpane-list']/div/div[2]")
    five1 = driver.find_element(By.XPATH, "//*[@id='demo-tabpane-list']/div/div[6]")  
    actions = ActionChains(driver)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    ActionChains(driver).drag_and_drop(five1, five).perform()
    time.sleep(2)
    
    #Valor 6 para 3
    Four = driver.find_element(By.XPATH, "//*[@id='demo-tabpane-list']/div/div[3]")
    Four1 = driver.find_element(By.XPATH, "//*[@id='demo-tabpane-list']/div/div[6]")  
    actions = ActionChains(driver)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    ActionChains(driver).drag_and_drop(Four1, Four).perform()
    time.sleep(2)

    #Valor 6 para 4
    Three= driver.find_element(By.XPATH, "//*[@id='demo-tabpane-list']/div/div[4]")
    Three1 = driver.find_element(By.XPATH, "//*[@id='demo-tabpane-list']/div/div[6]")  
    actions = ActionChains(driver)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    ActionChains(driver).drag_and_drop(Three1, Three).perform()
    time.sleep(2)

    #Valor 6 para 5
    Two= driver.find_element(By.XPATH, "//*[@id='demo-tabpane-list']/div/div[5]")
    Two1 = driver.find_element(By.XPATH, "//*[@id='demo-tabpane-list']/div/div[6]")  
    actions = ActionChains(driver)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    ActionChains(driver).drag_and_drop(Two1, Two).perform()
    time.sleep(2)
 
 

# Chamada da função
driver = instanciar_chrome()
interactions(driver)
ordenar_decrescente(driver)

driver.quit()