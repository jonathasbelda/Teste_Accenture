from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import time

#Configurações do Chrome
def instanciar_chrome():
    driver = webdriver.Chrome()  #Instancializar o Chrome
    driver.implicitly_wait(10)
    driver.maximize_window()  #maximizar a janela do chrome
    driver.get("https://demoqa.com")  # Abrir a página demoqa
    time.sleep(2)
    return driver

#clicar em elemnts
def elements(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    #clicar em Elements
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div[1]/div/div[3]").click()
    time.sleep(2)
    #clicar em Web Tables
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/div/div[1]/div/ul/li[4]").click() 
    time.sleep(2)
 
#Registration Form
def adiconar_usuário(driver):
    #clicar em add new record   
    driver.find_element(By.ID, "addNewRecordButton").click()
    time.sleep(2) 

def registration_form(driver):
    #Preencher o campo first name
    driver.find_element(By.ID, "firstName").send_keys("João") 
    #Preencher o campo last name
    driver.find_element(By.ID, "lastName").send_keys("Silva")
    #Preencher o campo email
    driver.find_element(By.ID, "userEmail").send_keys("teste@teste.com")
    time.sleep(1) 
    
    #Preencher o campo age
    driver.find_element(By.ID, "age").send_keys("30")  
    time.sleep(1)
    #Preencher o campo salary
    driver.find_element(By.ID, "salary").send_keys("5000")  
    time.sleep(1)
    #Preencher o campo department
    driver.find_element(By.ID, "department").send_keys("TI")  
    time.sleep(1)
    
    #clicar em submit
    driver.find_element(By.ID, "submit").click()  
    time.sleep(2)

def editar_usuário(driver):
    #clicar em edit
    driver.find_element(By.XPATH, "//*[@id='edit-record-4']").click()  
    time.sleep(2)
    #limpar o campo first name
    driver.find_element(By.ID, "firstName").clear() 
    #Preencher o campo first name
    driver.find_element(By.ID, "firstName").send_keys("Carlos") 
    time.sleep(1)
    #clicar em submit
    driver.find_element(By.ID, "submit").click()
    time.sleep(2)

def deletar_usuário(driver):
    #clicar em delete
    driver.find_element(By.ID, "delete-record-4").click()
    time.sleep(2)



# Chamada da função
driver = instanciar_chrome()
elements(driver)
adiconar_usuário(driver)
registration_form(driver)
editar_usuário(driver)
deletar_usuário(driver)


driver.quit()