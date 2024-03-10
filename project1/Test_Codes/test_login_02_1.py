from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Project1.Test_Data import data2_1
import pytest
import time
class TestOrangeHRM:
    url = "https://opensource-demo.orangehrmlive.com"
    # Booting Method for running the Python Project1
    @pytest.fixture
    def booting_function(self):
        # service_obj = Service("c:/NewDriver/chromedriver.exe")
        self.driver = webdriver.Chrome()
        yield
        self.driver.close()
    #########################CREATING NEGATIVE TEST CASE 1 WITH CORRECT USERNAME AND INCORRECT PASSWORD##############
    def  test_login_2_1(self, booting_function):
        self.driver.get(self.url)
        # Use WebDriverWait to wait for the username input field to be visible and enabled
        username_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, data2_1.TestSelectors.input_box_username))
        )
        username_input.send_keys(data2_1.TestData.username)

        # Similarly, wait for the password input field to be visible and enabled
        password_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, data2_1.TestSelectors.input_box_password))
        )
        password_input.send_keys(data2_1.TestData.password)

        # Wait for the login button to be clickable
        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2_1.TestSelectors.login_xpath))
        )
        login_button.click()
        time.sleep(10)
        assert self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[1]/div[1]/span/h6').text == 'Dashboard'
        print("USER IS NOT LOGGED IN SUCCESSFULLY# WITH USERNAME {username} and PASSWORD {password}".format(
            username=data2_1.TestData.username, password=data2_1.TestData.password))

        invalid_data=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,data2_1.TestSelectors.invalid_xpath)))
        print(invalid_data.text)
