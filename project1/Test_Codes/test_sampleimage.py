import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Project1.Test_Data import sampledata
import pytest
import pyautogui
from pynput.keyboard import Key,Controller
class TestOrangeHRM:
    url = "https://opensource-demo.orangehrmlive.com"
    # Booting Method for running the Python Project1
    @pytest.fixture
    def booting_function(self):
        # service_obj = Service("c:/NewDriver/chromedriver.exe")
        self.driver = webdriver.Chrome()
        yield
        self.driver.close()
    def  test_login(self, booting_function):
        self.driver.get(self.url)
        # Use WebDriverWait to wait for the username input field to be visible and enabled
        username_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, sampledata.TestSelectors.input_box_username))
        )
        username_input.send_keys(sampledata.TestData.username)

        # Similarly, wait for the password input field to be visible and enabled
        password_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, sampledata.TestSelectors.input_box_password))
        )
        password_input.send_keys(sampledata.TestData.password)

        # Wait for the login button to be clickable
        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, sampledata.TestSelectors.login_xpath))
        )
        login_button.click()
        #a=WebDriverWait(self.driver,10).until(self.driver.switch_to.alert)
        #a.accept()
        pim_module=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,sampledata.TestSelectors.pim_xpath)))
        pim_module.click()
        add_module=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,sampledata.TestSelectors.add_xpath)))
        add_module.click()
        image_details=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,sampledata.TestSelectors.image_xpath)))
        image_details.click()
        time.sleep(10)
        keyboard=Controller()
        keyboard.type("C:\\sampleimage\\download.jpg")
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(10)


