from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
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
# Interactions_Page
# 4. Click on 'Interactions' button
# 5. Verify 'Interactions' is visible
# =====================

class interaction_page:
    def __init__(self, driver):
        self.driver = driver # Armazena o driver do Selenium dentro da classe
        self.wait = WebDriverWait(driver, 20) # Cria um objeto de espera explícita (20 segundos)
        
        # Locators
        # 4. Click on 'Interactions' button
        self.interaction_card = (By.XPATH, "//*[@id='app']/div/div/div[2]/div/div[5]/div/div[3]")
        #Locator do menu lateral "Interactions". Útil para clicar no menu depois de abrir o card.
        self.interaction_menu = (By.XPATH, "//span[text()='Interactions']")
        # Locator do container ou seção "Interactions". Pode ser usado para validar se a seção carregou.
        self.interaction = (By.ID, "Interactions")
        # 5. Verify 'Interactions' is visible
        self.interactions_text = (By.XPATH, "//div[@class='header-text' and text()='Interactions']")

        
        # Methods
    def interactions(self):
        # 4. Click on 'Interactions' button
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.wait.until(EC.element_to_be_clickable(self.interaction_card)).click()
        # 5. Verify 'Elements' is visible
        element = self.wait.until(EC.visibility_of_element_located(self.interactions_text))
        assert element.is_displayed(), "❌ O texto 'Interactions' não está visível"
        print("✅ 'Interactions' está visível")

        
     
# =====================
# sortable_page
# 6. Click on 'Sortable' button
# 7. Verify 'Sortable' is visible
# 8. Perform drag and drop to sort the items in descending order
# =====================   
    
class sortable_page:
    def __init__(self, driver):
        self.driver = driver #
        self.wait = WebDriverWait(driver, 20) 
        
        # Locators
        # 6. Click on 'Sortable' button
        self.sortable_menu = (By.XPATH, "//span[text()='Sortable']")
        # 7. Verify 'Sortable' is visible
        self.web_tables_text = (By.XPATH, "//span[@class='text' and text()='Sortable']")
        # 8. Perform drag and drop to sort the items in descending order
        self.item_list = (By.ID, "demo-tabpane-list")
        self.item_grid = (By.ID, "demo-tabpane-grid")
        self.item = (By.CLASS_NAME, "list-group-item")
        self.item1 = (By.CLASS_NAME, "list-group-item")
        self.item2 = (By.CLASS_NAME, "list-group-item")
        self.item3 = (By.CLASS_NAME, "list-group-item")
        self.item4 = (By.CLASS_NAME, "list-group-item")
        self.item5 = (By.CLASS_NAME, "list-group-item")
        self.item6 = (By.CLASS_NAME, "list-group-item")
        
        
           
        # Methods       
    def abrir_Sortable(self):
        # 6. Click on 'Sortable' button
        self.wait.until(EC.element_to_be_clickable(self.sortable_menu)).click()
        
        
        # 7. Verify 'Sortable' is visible
        self.wait.until(EC.element_to_be_clickable(self.sortable_menu)).click()
        time.sleep(2)  # Espera para garantir que a ação de clique seja processada
        element = self.wait.until(EC.visibility_of_element_located(self.web_tables_text))
        assert element.is_displayed(), "❌ O texto 'Sortable' não está visível"
        print("✅ 'Sortable' está visível")
   
       
    def ordenar_decrescente(self):
        # 8. Perform drag and drop to sort the items in descending order
        driver = self.driver
        # Localiza o elemento maior (posição 6) e o menor (posição 1)
        six = driver.find_element(By.XPATH, "//*[@id='demo-tabpane-list']/div/div[1]")  
        six1 = driver.find_element(By.XPATH, "//*[@id='demo-tabpane-list']/div/div[6]")
        
        # Arrasta o maior elemento para a posição do menor (decrescente)
        actions = ActionChains(driver)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        ActionChains(driver).drag_and_drop(six1, six).perform()
        
        # Rola até o final da página para garantir que os elementos estejam visíveis
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)

        # Localiza o elemento maior (posição 6) e o menor (posição 2)
        five = self.driver.find_element(By.XPATH, "//*[@id='demo-tabpane-list']/div/div[2]") 
        five1 = self.driver.find_element(By.XPATH, "//*[@id='demo-tabpane-list']/div/div[6]")
        
        # Rola até o final da página para garantir que os elementos estejam visíveis
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        # Arrasta o maior elemento para a posição do menor (decrescente)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(five1, five).perform()
        time.sleep(3)
        
        # Localiza o elemento maior (posição 6) e o menor (posição 3)
        four = self.driver.find_element(By.XPATH, "//*[@id='demo-tabpane-list']/div/div[3]")  
        four1 = self.driver.find_element(By.XPATH, "//*[@id='demo-tabpane-list']/div/div[6]")
        
        # Rola até o final da página para garantir que os elementos estejam visíveis
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        # Arrasta o maior elemento para a posição do menor (decrescente)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(four1, four).perform()
        time.sleep(3)
        
        # Localiza o elemento maior (posição 6) e o menor (posição 4)
        three = self.driver.find_element(By.XPATH, "//*[@id='demo-tabpane-list']/div/div[4]")  
        three1 = self.driver.find_element(By.XPATH, "//*[@id='demo-tabpane-list']/div/div[6]")
        
        # Rola até o final da página para garantir que os elementos estejam visíveis
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        # Arrasta o maior elemento para a posição do menor (decrescente)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(three1, three).perform()
        time.sleep(3)
        
        # Localiza o elemento maior (posição 6) e o menor (posição 5)
        Two = self.driver.find_element(By.XPATH, "//*[@id='demo-tabpane-list']/div/div[5]")  
        Two1  = self.driver.find_element(By.XPATH, "//*[@id='demo-tabpane-list']/div/div[6]")
        
        # Rola até o final da página para garantir que os elementos estejam visíveis
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        # Arrasta o maior elemento para a posição do menor (decrescente)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(Two1, Two).perform()
        time.sleep(3)
    
    
         
# Chamada da função

if __name__ == "__main__":
    # Abre o navegador (reutilizando o Browser)
    browser = Browser()
    driver = browser.driver
    
    # interactions
    interaction_page = interaction_page(driver)
    interaction_page.interactions()
    
    # sortable_page
    sortable_page = sortable_page(driver)
    sortable_page.abrir_Sortable()
    sortable_page.ordenar_decrescente()
    
    # Fecha o navegador
    browser.quit()
    
