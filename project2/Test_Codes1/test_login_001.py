from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Test_Data1 import data01
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
    def  test_login_001(self, booting_function):
        self.driver.get(self.url)
        # Use WebDriverWait to wait for the username input field to be visible and enabled
        username_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, data01.TestSelectors.input_box_username))
        )
        username_input.send_keys(data01.TestData.username)
    ##########################3FORGOT PASSWORD CLICK################
        forgot_click=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,data01.TestSelectors.forgot_xpath)))
        forgot_click.click()
    ##################CHOOSING RESET PASSWORD LINK#############
        rusername_details=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,data01.TestSelectors.rusername_xpath)))
        rusername_details.send_keys("Admin")
        reset_click=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,data01.TestSelectors.reset_xpath)))
        reset_click.click()
        time.sleep(10)
        assert self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/div/h6').text=='Reset Password link sent successfully'
        print("the link has been sent successfully")


