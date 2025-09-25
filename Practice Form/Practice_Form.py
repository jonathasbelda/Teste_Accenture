from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time

# =====================
# Browser
# 1. Launch browser and navigate to URL
# 2. Navigate to url 'https://demoqa.com'
# 3. Verify that home page is visible successfully
# =====================

class Browser:
    def __init__(self):
        #1. Launch browser and navigate to URL
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        # 2. Navigate to url 'https://demoqa.com'
        self.driver.get("https://demoqa.com")
        self.wait = WebDriverWait(self.driver, 20)
        # 3. Verify that home page is visible successfully
        self.home_page_logo = (By.XPATH, "//*[@id='app']/header/a/img")
        assert self.wait.until(EC.visibility_of_element_located(self.home_page_logo)).is_displayed()
    print("✅Home page is visible successfully")

    def quit(self):
        self.driver.quit()
 

# =====================
# FormsPage
# 4. Click on 'Forms' button
# 5. Verify 'Forms' is visible
# 6. Click on 'Practice Form' button
# 7. Verify 'Practice Form' is visible
# 8. Fill in the form fields
# 9. Submit the form
# 10. Verify form submission
# =====================

class FormsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        
        # Locators
        # 4. Click on 'Forms' button
        self.forms_card = (By.XPATH, "//*[@id='app']/div/div/div[2]/div/div[2]/div/div[3]")
        # Locator do menu lateral "Forms". Útil para clicar no menu depois de abrir o card.
        self.forms_menu = (By.XPATH, "//span[text()='Forms']")
        # Locator do container ou seção "Forms". Pode ser usado para validar se a seção carregou.
        self.forms = (By.ID, "Forms")
        # 5. Verify 'Forms' is visible
        self.forms_text = (By.XPATH, "//div[@class='header-text' and text()='Forms']")
        
        #Methods
    def open_forms(self):
        # 4. Click on 'Forms' button
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.wait.until(EC.element_to_be_clickable(self.forms_card)).click()
        time.sleep(2)
        # 5. Verify 'Forms' is visible
        assert self.wait.until(EC.visibility_of_element_located(self.forms_text)).is_displayed()
        print("✅'Forms' is visible")
        
  
# =====================       
# PracticeForm    
# 7. Click on 'Practice Form' button
# 8. Verify 'Practice Form' is visible
# 9. Fill in the form fields
# 10. Submit the form
# 11. Verify form submission
# =====================    

class PracticeForm:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        
        # Locators
        # 7. Click on 'Practice Form' button
        self.practice_form_item = (By.XPATH, "//span[text()='Practice Form']")
        # 8. Verify 'Practice Form' is visible
        self.practice_form_text = (By.XPATH, "//span[@class='text' and text()='Practice Form']")
        # 9. Fill in the form fields
        self.first_name = (By.ID, "firstName")
        self.last_name = (By.ID, "lastName")
        self.email = (By.ID, "userEmail")
        self.gender_male = (By.XPATH, "//*[@id='genterWrapper']/div[2]/div[1]/label")
        self.phone = (By.ID, "userNumber")
        self.dob_input = (By.ID, "dateOfBirthInput")
        self.month_select = (By.CLASS_NAME, "react-datepicker__month-select")
        self.year_select = (By.CLASS_NAME, "react-datepicker__year-select")
        self.day_25 = (By.XPATH, "//*[@aria-label='Choose Friday, May 25th, 1990']")
        self.subjects_input = (By.ID, "subjectsInput")
        self.hobby_sports_label = (By.XPATH, "//label[text()='Sports']")
        self.upload_picture = (By.ID, "uploadPicture")
        self.address = (By.ID, "currentAddress")
        self.state_input = (By.ID, "react-select-3-input")
        self.city_input = (By.ID, "react-select-4-input")
        self.submit_button = (By.ID, "submit")
        self.close_modal = (By.ID, "closeLargeModal")
    
        # Methods
    def registration_Form(self):
        # 7. Click on 'Practice Form' button
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.wait.until(EC.element_to_be_clickable(self.practice_form_item)).click()
        time.sleep(2)
        # 8. Verify 'Practice Form' is visible
        assert self.wait.until(EC.visibility_of_element_located(self.practice_form_text)).is_displayed()
        print("✅'Practice Form' is visible")
        
    # 9. Fill in the form fields
    def preencher_nome(self, first, last):
        # Preenche o primeiro e último nome
        self.wait.until(EC.visibility_of_element_located(self.first_name)).send_keys(first)
        self.driver.find_element(*self.last_name).send_keys(last)

    def preencher_email(self, email):
        # Preenche o email
        self.driver.find_element(*self.email).send_keys(email)

    def selecionar_genero(self):
        # Seleciona o gênero "Male"
        self.driver.find_element(*self.gender_male).click()

    def preencher_telefone(self, phone):
        # Preenche o número de telefone
        self.driver.find_element(*self.phone).send_keys(phone)

    def selecionar_data_nascimento(self, mes="May", ano="1990", dia_aria_label=None):
        # Abre o calendário
        self.driver.find_element(*self.dob_input).click()
        # Seleciona mês e ano
        Select(self.driver.find_element(*self.month_select)).select_by_visible_text(mes)
        Select(self.driver.find_element(*self.year_select)).select_by_visible_text(ano)
        # Seleciona o dia (padrão = 25 de maio de 1990)
        if not dia_aria_label:
            dia_aria_label = "//*[@aria-label='Choose Friday, May 25th, 1990']"
        self.driver.find_element(By.XPATH, dia_aria_label).click()

    def adicionar_materia(self, materia):
        # Digita a matéria e confirma com Enter
        campo = self.driver.find_element(*self.subjects_input)
        campo.send_keys(materia)
        campo.send_keys("\n")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def selecionar_hobby(self):
        # Seleciona o hobby "Sports"
        element = self.wait.until(EC.element_to_be_clickable(self.hobby_sports_label))
        element.click()

    def fazer_upload(self, caminho_arquivo):
        # Faz upload de um arquivo local
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element(*self.upload_picture).send_keys(caminho_arquivo)
        time.sleep(5)

    def preencher_endereco(self, endereco):
        # Preenche o endereço
        self.driver.find_element(*self.address).send_keys(endereco)

    def selecionar_estado_cidade(self, estado, cidade):
        # Seleciona estado
        estado_input = self.driver.find_element(*self.state_input)
        estado_input.send_keys(estado)
        estado_input.send_keys("\n")
        # Seleciona cidade
        cidade_input = self.driver.find_element(*self.city_input)
        cidade_input.send_keys(cidade)
        cidade_input.send_keys("\n")

    # 10. Submit the form
    def submeter_formulario(self):
        # Rola até o final da página e clica em "Submit"
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element(*self.submit_button).click()
        time.sleep(5) # espera fixa para visualização

    # 11. Verify form submission
    def fechar_modal(self):
        # Fecha o modal de confirmação após o submit
        self.wait.until(EC.element_to_be_clickable(self.close_modal)).click()
    

# =====================
# Execução do teste
# =====================
if __name__ == "__main__":
    # Inicializa o navegador
    browser = Browser()
    driver = browser.driver

    # FormsPage
    forms_page = FormsPage(driver)
    forms_page.open_forms()
    
    
    # PracticeForm
    PracticeFormPage = PracticeForm(driver)
    PracticeFormPage.registration_Form()
    PracticeFormPage.preencher_nome("João", "Silva")
    PracticeFormPage.preencher_email("teste@hotmail.com")
    PracticeFormPage.selecionar_genero()
    PracticeFormPage.preencher_telefone("11999999999")
    PracticeFormPage.selecionar_data_nascimento()
    PracticeFormPage.adicionar_materia("Maths")
    PracticeFormPage.selecionar_hobby()
    PracticeFormPage.fazer_upload("C:/Users/User/OneDrive/Documentos/Accenture/Practice Form/files/Teste_Accenture.txt")
    PracticeFormPage.preencher_endereco("Rua teste, 123, São Paulo, SP")
    PracticeFormPage.selecionar_estado_cidade("NCR", "Delhi")
    PracticeFormPage.submeter_formulario()
    PracticeFormPage.fechar_modal()
    
    # Fecha o navegador
    browser.quit()
