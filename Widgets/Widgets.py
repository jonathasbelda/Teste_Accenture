from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# =====================
# Browser
# 1. Launch browser and navigate to URL
# 2. Navigate to url 'https://demoqa.com'
# 3. Verify that home page is visible successfully
# =====================

# Configurações do Chrome
class Browser:
    def __init__(self):
        # 1. Launch browser and navigate to URL
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        # 2. Navigate to url 'https://demoqa.com'
        self.driver.get("https://demoqa.com")
        self.wait = WebDriverWait(self.driver, 20)
        # 3. Verify that home page is visible successfully
        self.home_page_logo = (By.XPATH, "//*[@id='app']/header/a/img")
        assert self.wait.until(EC.visibility_of_element_located(self.home_page_logo)).is_displayed()
    print("✅demoqa.com page is visible successfully")

    def quit(self):
        self.driver.quit()

# =====================
# MenuWidgets
# 4. click 'Widgets'
# 5. click 'Progress Bar'
# 6. Switch to Progress Bar section
# 7. Start the progress bar
# 8. Stop the progress bar at 25%
# 9. Restart the progress bar and wait until it reaches 100%
# 10. Reset the progress bar
# =====================

class WidgetsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        
        # Locators
        # 4. Click menu 'Widgets'
        self.widgets_card = (By.XPATH, "//*[@id='app']/div/div/div[2]/div/div[4]/div/div[3]/h5")


        #Methods
    def abrir_widgets(self):
        # 4. Click menu 'Widgets'
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.wait.until(EC.element_to_be_clickable(self.widgets_card)).click()

# =====================
# ProgressBarPage
# 5. click 'Progress Bar'
# 6. Switch to Progress Bar section
# 7. Start the progress bar
# 8. Stop the progress bar at 25%
# 9. Restart the progress bar and wait until it reaches 100%
# 10. Reset the progress bar
# =====================

class ProgressBarPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        
        # Locators
        # 5. click 'Progress Bar'
        self.progress_bar_menu = (By.XPATH, "//span[text()='Progress Bar']")
        # 6. Switch to Progress Bar section
        self.start_button = (By.ID, "startStopButton")
        # mostra o número (%)
        self.progress_text = (By.CSS_SELECTOR, "div.progress-bar")
        # 7. Start the progress bar
        self.start_button = (By.ID, "startStopButton")
        # 8. Stop the progress bar at 25%
        self.stop_button = (By.ID, "startStopButton")
        # 9. Restart the progress bar and wait until it reaches 100%
        self.restart_button = (By.ID, "startStopButton")
        # 10. Reset the progress bar
        self.reset_button = (By.ID, "resetButton")
        
        
        #Methods
    def abrir_progress_bar(self):
        # Rola até o item "Progress Bar"
        progress_element = self.driver.find_element(*self.progress_bar_menu)
        # 5. click 'Progress Bar'
        self.driver.execute_script("arguments[0].scrollIntoView();", progress_element)

        # 6. Switch to Progress Bar section
        self.wait.until(EC.element_to_be_clickable(self.progress_bar_menu)).click()
        print("✅ Menu 'Progress Bar' aberto com sucesso!")
        time.sleep(3)
   
    def start_progress_bar(self):
        # 7. Start the progress bar
        start_button = self.driver.find_element(By.ID, "startStopButton")
        start_button.click()
        time.sleep(2.5)  # espera 2,5s para a barra começar a rodar
        
    def stop_progress_bar(self):
        # 8. Stop the progress bar at 25%
        stop_start_button = self.driver.find_element(By.ID, "startStopButton") 
        stop_start_button.click()
        # Pegamos o elemento da barra
        progress_bar = self.driver.find_element(By.CSS_SELECTOR, "div.progress-bar")
        # Lemos o atributo
        progress_value = progress_bar.get_attribute("aria-valuenow")
        # Exibir na tela
        print(f"✅Progress bar parou em: {progress_value}%")
        time.sleep(5)
        
    def restart_progress_bar(self):
        # 9. Restart the progress bar and wait until it reaches 100%
        start_button = self.driver.find_element(By.ID, "startStopButton")
        start_button.click()

        # Espera até a barra chegar em 100%
        progress_bar = self.driver.find_element(By.CSS_SELECTOR, "div.progress-bar")
        self.wait.until(lambda driver: progress_bar.get_attribute("aria-valuenow") == "100")
        progress_value = progress_bar.get_attribute("aria-valuenow")
        print(f"✅Progress bar parou em: {progress_value}%")
        time.sleep(5)
        
    def reset_progress_bar(self):
        # 10. Reset the progress bar
        resetButton = self.driver.find_element(By.ID, "resetButton")
        resetButton.click()
        time.sleep(3)
    
    
#Chamada da função

if __name__ == "__main__":
    # Abre o navegador (reutilizando o Browser)
    browser = Browser()
    driver = browser.driver
    
    # Widgets
    WidgetsPage = WidgetsPage(driver)
    WidgetsPage.abrir_widgets()
    
    # ProgressBarPage
    ProgressBarPage = ProgressBarPage(driver)
    ProgressBarPage.abrir_progress_bar()
    ProgressBarPage.start_progress_bar()
    ProgressBarPage.stop_progress_bar()
    ProgressBarPage.restart_progress_bar()
    ProgressBarPage.reset_progress_bar()
    
    # Fecha o navegador
    browser.quit()