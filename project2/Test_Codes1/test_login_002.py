from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Test_Data1 import data02
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
    def  test_login_002(self, booting_function):
        self.driver.get(self.url)
        # Use WebDriverWait to wait for the username input field to be visible and enabled
        username_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, data02.TestSelectors.input_box_username))
        )
        username_input.send_keys(data02.TestData.username)

        # Similarly, wait for the password input field to be visible and enabled
        password_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, data02.TestSelectors.input_box_password))
        )
        password_input.send_keys(data02.TestData.password)

        # Wait for the login button to be clickable
        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data02.TestSelectors.login_xpath))
        )
        login_button.click()
        #############Validating the title of webpage#######
        assert self.driver.title=='OrangeHRM'
        print("Successsfull validation of title as OrangeHRM")
        ###########Validating the options of the webpage###########
        self.driver.maximize_window()
        admin_click=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,data02.TestSelectors.admin_xpath)))
        admin_click.click()
        time.sleep(10)
        ###################checking whetherthe following options are displayed on webpage or not#############
        #expected_items=['User Management','Job','Organization','Qualifications','Nationalities','Corporate Banking','Configuration']
        menu_items=self.driver.find_elements(By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li')
        for i in menu_items:
            if i.is_displayed() :
                print(i.text)

