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

#clicar em forms
def forms(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='app']/div/div/div[2]/div/div[2]/div/div[3]/h5").click()
    time.sleep(2)

#clicar em practice form
def practice_form(driver):
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/div/div[2]/div/ul/li").click()
    time.sleep(2)

    #preencher o formulário
    driver.find_element(By.ID, "firstName").send_keys("João")
    driver.find_element(By.ID, "lastName").send_keys("Silva")  
    driver.find_element(By.ID, "userEmail").send_keys("teste@hotmail.com")

    #Selecionar o gênero
    driver.find_element(By.XPATH, "//*[@id='genterWrapper']/div[2]/div[1]/label").click() 
    #Inserir o telefone
    driver.find_element(By.ID, "userNumber").send_keys("11999999999") 
    
    #Clicar no campo data de nascimento
    driver.find_element(By.ID, "dateOfBirthInput").click()
    time.sleep(1)
    #Clicar no campo mês
    driver.find_element(By.CLASS_NAME, "react-datepicker__month-select").click() 
    #Selecionar o mês
    select = Select(driver.find_element(By.CLASS_NAME, "react-datepicker__month-select"))
    #Selecionar o mês maio
    select.select_by_visible_text("May")
    time.sleep(1)
    #Clicar no campo ano
    driver.find_element(By.CLASS_NAME, "react-datepicker__year-select").click() 
    #Selecionar o ano 
    select = Select(driver.find_element(By.CLASS_NAME, "react-datepicker__year-select"))
    #Selecionar o ano 1990
    select.select_by_visible_text("1990")
    time.sleep(1)

    #Selecionar o dia 25
    driver.find_element(By.XPATH, "//*[@aria-label='Choose Friday, May 25th, 1990']").click()
    #Scroll até o final da página
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2) 

    #Scroll até o final da página
    driver.find_element(By.ID, "subjectsInput").send_keys("Maths")
    #Enter
    driver.find_element(By.ID, "subjectsInput").send_keys("\n")
    time.sleep(1)

    #Selecionar o hobby
    driver.find_element(By.XPATH, "//*[@id='hobbiesWrapper']/div[2]/div[1]/label").click() 
    time.sleep(1)

    #Fazer upload da arquivo 
    driver.find_element(By.ID, "uploadPicture").send_keys("C:/Users/User/OneDrive/Documentos/Accenture/Practice Form/files/Teste_Accenture.txt")      
    time.sleep(3)

    #Preencher o campo endereço
    driver.find_element(By.ID, "currentAddress").send_keys("Rua teste, 123, São Paulo, SP")
    time.sleep(1)

    #Selecionar o estado
    estado_input = driver.find_element(By.ID, "react-select-3-input")
    estado_input.send_keys("NCR")
    time.sleep(1) 
    estado_input.send_keys("\n")
    time.sleep(2)

    #Selecionar a cidade   
    cidade_input = driver.find_element(By.ID, "react-select-4-input")
    cidade_input.send_keys("Delhi")
    time.sleep(1) 
    cidade_input.send_keys("\n")
    time.sleep(2)

    #submit
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1) 
    driver.find_element(By.XPATH, "//*[@id='submit']").click()
    time.sleep(10) 

    #Fechar o modal
    driver.find_element(By.ID, "closeLargeModal").click()
    time.sleep(4)
   

# Chamada da função
driver = instanciar_chrome()
forms(driver)
practice_form(driver)

driver.quit()