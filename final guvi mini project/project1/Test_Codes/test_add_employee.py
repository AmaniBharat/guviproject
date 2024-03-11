import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Project1.Test_Data import project1test_data
import pytest
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
    ############Test Case 3 Of addding new employee in the pim module######
    def  test_login_003(self, booting_function):
        self.driver.get(self.url)
        # Use WebDriverWait to wait for the username input field to be visible and enabled
        username_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, project1test_data.TestSelectors.input_box_username))
        )
        username_input.send_keys(project1test_data.TestData.username)

        # Similarly, wait for the password input field to be visible and enabled
        password_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, project1test_data.TestSelectors.input_box_password))
        )
        password_input.send_keys(project1test_data.TestData.password)

        # Wait for the login button to be clickable
        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, project1test_data.TestSelectors.login_xpath))
        )
        login_button.click()
        ###########Clicking the pim module#########
        pim_module=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,project1test_data.TestSelectors.pim_xpath)))
        pim_module.click()
        ############By clicking the add new employee button############
        add_module=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,project1test_data.TestSelectors.add_xpath)))
        add_module.click()
        ##############giving the employee details###########
        firstname_details=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,project1test_data.TestSelectors.firstname_xpath)))
        firstname_details.send_keys(project1test_data.TestData.addirstname)
        middlename_details=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,project1test_data.TestSelectors.middlename_xpath)))
        middlename_details.send_keys(project1test_data.TestData.addmiddlename)
        lastname_details=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,project1test_data.TestSelectors.lastname_xpath)))
        lastname_details.send_keys(project1test_data.TestData.addlastname)
        #######################3UPLOADING THE IMAGE TO THE WEBPAGE##############
        image_details = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, project1test_data.TestSelectors.image_xpath)))
        image_details.click()
        time.sleep(10)
        keyboard = Controller()
        keyboard.type("C:\\sampleimage\\download.jpg")
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(10)
        ################adding the employee details by clicking the save button###########
        add_click=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,project1test_data.TestSelectors.save_xpath)))
        add_click.click()
        time.sleep(10)
        ############asserting the test case whether new employyee added or nt in the portal###########
        assert self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/h6').text=="Personal Details"
        print("Succeessfully added and Saved the new employee")




