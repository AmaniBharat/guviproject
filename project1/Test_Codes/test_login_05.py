from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from Project1.Test_Data import data5
import pytest
import time
from selenium.webdriver.common.alert import Alert
class TestOrangeHRM:
    url = "https://opensource-demo.orangehrmlive.com"
    # Booting Method for running the Python Project1
    @pytest.fixture
    def booting_function(self):
        # service_obj = Service("c:/NewDriver/chromedriver.exe")
        self.driver = webdriver.Chrome()
        self.actions = ActionChains(self.driver)
        yield
        self.driver.close()
    def  test_login_005(self, booting_function):
        self.driver.get(self.url)
        # Use WebDriverWait to wait for the username input field to be visible and enabled
        username_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, data5.TestSelectors.input_box_username))
        )
        username_input.send_keys(data5.TestData.username)

        # Similarly, wait for the password input field to be visible and enabled
        password_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, data5.TestSelectors.input_box_password))
        )
        password_input.send_keys(data5.TestData.password)

        # Wait for the login button to be clickable
        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data5.TestSelectors.login_xpath)))
        login_button.click()
        pim_module=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,data5.TestSelectors.pim_xpath)))
        pim_module.click()
        add_module=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,data5.TestSelectors.add_xpath)))
        add_module.click()
        firstname_details=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,data5.TestSelectors.firstname_xpath)))
        firstname_details.send_keys(data5.TestData.firstname)
        middlename_details=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,data5.TestSelectors.middlename_xpath)))
        middlename_details.send_keys(data5.TestData.middlename)
        lastname_details=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,data5.TestSelectors.lastname_xpath)))
        lastname_details.send_keys(data5.TestData.lastname)
        add_click = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data5.TestSelectors.save_xpath)))
        add_click.click()

        employee_list=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,data5.TestSelectors.existing_xpath)))
        employee_list.click()
        hint_list=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,data5.TestSelectors.hintsearch_xpath)))
        hint_list.send_keys(data5.TestData.hintname)
        search_click=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,data5.TestSelectors.search_xpath)))
        search_click.click()
        self.driver.maximize_window()
        self.driver.execute_script("window.scrollTo(0, 500)")
        #######################DELETING THE EMPLOYEE###############
        delete_click=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,data5.TestSelectors.delete_xpath)))
        delete_click.click()
        sure_click=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,data5.TestSelectors.sure_xpath)))
        sure_click.click()
        time.sleep(5)
        assert self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/span').text=='No Records Found'
        print("The Employee Is Successfully Deleted")
