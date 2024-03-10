from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from Project1.Test_Data import sampledropdowndata
import pytest
import time
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
    def  test_login(self, booting_function):
        self.driver.get(self.url)
        # Use WebDriverWait to wait for the username input field to be visible and enabled
        username_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, sampledropdowndata.TestSelectors.input_box_username))
        )
        username_input.send_keys(sampledropdowndata.TestData.username)

        # Similarly, wait for the password input field to be visible and enabled
        password_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, sampledropdowndata.TestSelectors.input_box_password))
        )
        password_input.send_keys(sampledropdowndata.TestData.password)

        # Wait for the login button to be clickable
        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, sampledropdowndata.TestSelectors.login_xpath)))
        login_button.click()
        pim_module=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,sampledropdowndata.TestSelectors.pim_xpath)))
        pim_module.click()
        employee_list=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,sampledropdowndata.TestSelectors.existing_xpath)))
        employee_list.click()
        hint_list=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,sampledropdowndata.TestSelectors.hintsearch_xpath)))
        hint_list.send_keys(sampledropdowndata.TestData.hintname)
        search_click=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,sampledropdowndata.TestSelectors.search_xpath)))
        search_click.click()
        self.driver.maximize_window()
        self.driver.execute_script("window.scrollTo(0, 500)")
        edit_click=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,sampledropdowndata.TestSelectors.edit_xpath)))
        edit_click.click()
        #self.driver.execute_script("window.scrollTo(0,500)")
        nation_value=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,sampledropdowndata.TestSelectors.nation_xpath)))
        nation_value.click()
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0,500)")
        nation_select=WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,sampledropdowndata.TestSelectors.nation_select_xpath)))
        nation_select.click()
        time.sleep(10)
