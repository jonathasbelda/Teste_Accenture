from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait, Select
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
# MenuAlerts
# 4. Click menu 'Alerts, Frame & Windows'
# 5. click 'Browser Windows'
# 6. click 'New Window'
# 7. Switch to new tab
# 8. Print the text from new tab
# 9. Close the tab
# 10. Go back to original tab
# =====================

class alerts:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        
        # Locators
        # 4. Click menu 'Alerts, Frame & Windows'
        self.alerts_frame_windows_menu = (By.XPATH, "//*[@id='app']/div/div/div[2]/div/div[3]/div/div[3]")
        # 5. click 'Browser Windows'
        self.browser_windows_option = (By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/div/div[3]/div/ul/li[1]")
        # 6. click 'New Window'
        self.new_window_button = (By.ID, "tabButton")
        # 7. Switch to new tab
        self.logged_in_as_text = (By.XPATH, "//h2[contains(text(),'Logged in as username')]")
        # 8. Print the text from new tab
        self.new_tab_text = (By.ID, "sampleHeading")

    # Methods   
        # 4. Click menu 'Alerts, Frame & Windows'
    def open_alerts(self):
        self.wait.until(EC.element_to_be_clickable(self.alerts_frame_windows_menu)).click()
        
        
        # 5. click 'Browser Windows'
    def click_browser_windows(self):
        self.wait.until(EC.element_to_be_clickable(self.browser_windows_option)).click()
      
        
        # 6. click 'New Window'
    def click_new_window(self):
        self.wait.until(EC.element_to_be_clickable(self.new_window_button)).click()   
       
        
        
        # 7. Switch to new tab
    def switch_new_tab(self):
        driver.switch_to.window(driver.window_handles[1]) 
        time.sleep(2)
        
        
       # 8. Print the text from new tab
    def print_new_tab_text(self):   
        return self.wait.until(EC.visibility_of_element_located(self.new_tab_text)).is_displayed()
    print("✅'This is a sample page")
    
    
    def close_new_tab(self):
        # 9. Close the tab
        driver.close()  
        time.sleep(2)
        
        
    def go_back_original_tab(self):
        # 10. Go back to original tab
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(2)
    
 
#Chamada da função

if __name__ == "__main__":
    # Abre o navegador (reutilizando o Browser)
    browser = Browser()
    driver = browser.driver
    
    
    # Executa o teste de alerts
    alerts = alerts(driver)
    alerts.open_alerts()
    alerts.click_browser_windows()
    alerts.click_new_window()
    alerts.switch_new_tab()
    alerts.print_new_tab_text()
    alerts.close_new_tab()
    alerts.go_back_original_tab()
    
    
    # Fecha o navegador
    browser.quit()
    




