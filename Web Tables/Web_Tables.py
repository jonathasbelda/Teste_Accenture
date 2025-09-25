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
# ElementsPage
# 4. Click on 'Elements' button
# 5. Verify 'Elements' is visible
# 6. Click on 'Web Tables' button
# 7. Verify 'Web Tables' is visible
# 8. Click on 'Add' button
# 9. Fill in the form with valid data
# 10. Click 'Submit' button
# 11. Verify that the new user is added to the table
# 12. Click on 'Edit' button of the added user
# 13. Update the user's information
# 14. Click 'Submit' button
# 15. Verify that the user's information is updated in the table
# 16. Click on 'Delete' button of the added user
# 17. Verify that the user is removed from the table
# =====================

class ElementsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        
    # Locators
        # 4. Click on 'Elements' button
        card = self.driver.find_element(By.XPATH, "//h5[contains(text(),'Elements')]") # Centraliza o card na tela
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", card)
        self.elements_button = (By.XPATH, "//h5[contains(text(),'Elements')]")
        # 5. Verify 'Elements' is visible
        self.elements_text = (By.XPATH, "//div[@class='header-text' and text()='Elements']")
        # 6. Click on 'Web Tables' button
        self.web_tables_button = (By.XPATH, "//span[contains(text(),'Web Tables')]")
        #7. Verify 'Web Tables' is visible
        self.web_tables_text = (By.XPATH, "//span[@class='text' and text()='Web Tables']")
        # 8. Click on 'Add' button
        self.add_button = (By.ID, "addNewRecordButton")
        # 9. Fill in the form with valid data
        self.first_name_input = (By.ID, "firstName")
        self.last_name_input = (By.ID, "lastName")
        self.email_input = (By.ID, "userEmail")
        self.age_input = (By.ID, "age")
        self.salary_input = (By.ID, "salary")
        self.department_input = (By.ID, "department")
        # 10. Click 'Submit' button
        self.submit_button = (By.ID, "submit")
        # 11. Verify that the new user is added to the table
        self.added_user = (By.XPATH, "//div[@class='rt-tbody']//div[contains(text(),'João')]")
        # 12. Click on 'Edit' button of the added user
        self.edit_button = (By.ID, "edit-record-4")
        # 13. Update the user's information
        self.first_name_input = (By.ID, "firstName")
        # 14. Click 'Submit' button
        self.submit_button = (By.ID, "submit")
        # 15. Verify that the user's information is updated in the table
        self.updated_user = (By.XPATH, "//div[@class='rt-tbody']//div[contains(text(),'Carlos')]")
        # 16. Click on 'Delete' button of the added user
        self.delete_button = (By.ID, "delete-record-4")
        # 17. Verify that the user is removed from the table
        self.deleted_user = (By.XPATH, "//div[@class='rt-tbody']//div[contains(text(),'Carlos')]")
        
        
    # Methods
    def elements(self):
        # 4. Click on 'Elements' button
        self.wait.until(EC.element_to_be_clickable(self.elements_button)).click()
            
        # 5. Verify 'Elements' is visible
        assert self.wait.until(EC.visibility_of_element_located(self.elements_text)).is_displayed()
        print("✅Elements is visible successfully")
        
        
    def web_tables(self):
        # Scroll down to make the 'Web Tables' button visible
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # 6. Click on 'Web Tables' button
        self.wait.until(EC.element_to_be_clickable(self.web_tables_button)).click()
        #7. Verify 'Web Tables' is visible  
        assert self.wait.until(EC.visibility_of_element_located(self.web_tables_text)).is_displayed()
        print("✅Web Tables is visible successfully")


    def click_add_button(self):
        # 8. Click on 'Add' button
        self.wait.until(EC.element_to_be_clickable(self.add_button)).click()
        
    def fill_form(self, first_name, last_name, email, age, salary, department):
        # 9. Fill in the form with valid data
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.email_input).send_keys(email)
        self.driver.find_element(*self.age_input).send_keys(age)
        self.driver.find_element(*self.salary_input).send_keys(salary)
        self.driver.find_element(*self.department_input).send_keys(department)
        time.sleep(2)
        
        
    def submit_form(self):
        # 10. Click 'Submit' button
        self.wait.until(EC.element_to_be_clickable(self.submit_button)).click()
        
        # 11. Verify that the new user is added to the table
        assert self.wait.until(EC.visibility_of_element_located(self.added_user)).is_displayed()
        time.sleep(3)
        print("✅New user is added to the table successfully")
    
    def edit_user(self):
        # 12. Click on 'Edit' button of the added user
        self.wait.until(EC.element_to_be_clickable(self.edit_button)).click()
        time.sleep(3)
        
        # 13. Update the user's information
        first_name_field = self.wait.until(EC.visibility_of_element_located(self.first_name_input))
        first_name_field.clear()
        first_name_field.send_keys("Carlos")
        time.sleep(1)
        # 14. Click 'Submit' button
        self.wait.until(EC.element_to_be_clickable(self.submit_button)).click()
        # 15. Verify that the user's information is updated in the table
        assert self.wait.until(EC.visibility_of_element_located(self.updated_user)).is_displayed
        time.sleep(3)
        print("✅User's information is updated in the table successfully")
    
    def delete_user(self):
        # 16. Click on 'Delete' button of the added user
        self.wait.until(EC.element_to_be_clickable(self.delete_button)).click()
        time.sleep(2)
        # 17. Verify that the user is removed from the table
        time.sleep(3)
        assert len(self.driver.find_elements(By.XPATH, "//div[@class='rt-tbody']//div[contains(text(),'Carlos')]")) == 0
        print("✅User is removed from the table successfully")
        
               
    
#Chamada da função

if __name__ == "__main__":
    # Abre o navegador (reutilizando o Browser)
    browser = Browser()
    driver = browser.driver
    
    #ElementsPage
    elements_page = ElementsPage(driver)
    elements_page.elements()
    elements_page.web_tables()
    elements_page.click_add_button()
    elements_page.fill_form("João", "Silva", "Teste@hotmail.com", "30", "5000", "TI")
    elements_page.submit_form()
    elements_page.edit_user()
    elements_page.delete_user()
    


    #Fecha o navegador
    browser.quit()
    
    