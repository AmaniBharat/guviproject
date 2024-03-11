from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from Project1.Test_Data import project1test_data
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
    ##########CREATING THE NEW TEST CASE BY EDITING  THE DETAILS OF THE EMPLOYEEE#########
    def  test_login_004(self, booting_function):
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
            EC.element_to_be_clickable((By.XPATH, project1test_data.TestSelectors.login_xpath)))
        login_button.click()
        #############3CLICKING OF THE PIM MODULE BUTON#########
        pim_module=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,project1test_data.TestSelectors.pim_xpath)))
        pim_module.click()
        ############CLICKING ON HE ADDD EMPLOYEE BUTTON###########3
        add_module = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, project1test_data.TestSelectors.add_xpath)))
        add_module.click()
        ###############3FILLNG THE EMPLOYEEDETAILS############
        firstname_details = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, project1test_data.TestSelectors.firstname_xpath)))
        firstname_details.send_keys(project1test_data.TestData.editfirstname)
        middlename_details = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, project1test_data.TestSelectors.middlename_xpath)))
        middlename_details.send_keys(project1test_data.TestData.editmiddlename)
        lastname_details = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, project1test_data.TestSelectors.lastname_xpath)))
        lastname_details.send_keys(project1test_data.TestData.editlastname)
        add_click = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, project1test_data.TestSelectors.save_xpath)))
        add_click.click()
     #############SEARCHING THE EMPLOYEE NAME IN THE EMPLOYEE LIST BY GIVING THE HINTNAME#############
        employee_list=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,project1test_data.TestSelectors.existing_xpath)))
        employee_list.click()
        hint_list=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,project1test_data.TestSelectors.hintsearch_xpath)))
        hint_list.send_keys(project1test_data.TestData.edithintname)
        ############CICKING ON THE SERACH OPTION TO VIEW THE RECOR OF THE EMPLOYEE#########
        search_click=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,project1test_data.TestSelectors.search_xpath)))
        search_click.click()
        self.driver.maximize_window()
        ############SCROLLING DOWN THE WEBPAGE####
        self.driver.execute_script("window.scrollTo(0, 500)")
        #########CLICKING ON THE EDIT OPTION OF THE EMPLOYEE RECORD#############
        edit_click=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,project1test_data.TestSelectors.edit_xpath)))
        edit_click.click()
        self.driver.execute_script("window.scrollTo(0,400)")
        #nation_value=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,project1test_data.TestSelectors.nation_xpath)))
        #nation_value.click()

        ###########EDITING THE DETAILS OF THE EMPLOYEE DATE OF BIRTH###########
        dob_details=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,project1test_data.TestSelectors.dob_xpath)))
        dob_details.send_keys("1993-22-08")
        gender_details=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,project1test_data.TestSelectors.gender_xpath)))
        gender_details.click()
        ###########SAVING THE UPDATED DETAILS OF THE EMPLOYEEE######
        edit_save_click=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,project1test_data.TestSelectors.edit_save_xpath)))
        edit_save_click.click()
        #blood_details=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,data4.TestSelectors.blood_xpath)))
        #drop=Select(blood_details)
        #drop.select_by_visible_text("B+")
        #time.sleep(10)
        self.driver.execute_script("window.scrollTo(0,100)")
        ################### CONTACT DETAILS ####################
        contact_cick=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,project1test_data.TestSelectors.contact_xpath)))
        contact_cick.click()
        #################ADDRESS DETAILS###########
        stree1_details=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,project1test_data.TestSelectors.street1_xpath)))
        stree1_details.send_keys("4-253")
        street2_details=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,project1test_data.TestSelectors.street2_xpath)))
        street2_details.send_keys("k.g.road")
        city_details=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,project1test_data.TestSelectors.city_xpath)))
        city_details.send_keys("Pedda Dornala")
        state_details=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,project1test_data.TestSelectors.state_xpath)))
        state_details.send_keys("Andhra Pradesh")
        pincode_details=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,project1test_data.TestSelectors.pin_xpath)))
        pincode_details.send_keys("523331")
        #country_details=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,data4.TestSelectors.country_xpath)))
        #country=Select(country_details)
        #country.select_by_visible_text("India")
        self.driver.execute_script("window.scrollTo(0,300)")
        ##############################TELEPHONE DETAILS ##############
        mobile_details=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,project1test_data.TestSelectors.mobile_xpath)))
        mobile_details.send_keys("123456789")
        #######################EMAIL DETAILS###############
        email_details=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,project1test_data.TestSelectors.email_xpath)))
        email_details.send_keys("amanibharat@gmail.com")
        contact_save_click=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,project1test_data.TestSelectors.contact_save_xpath)))
        contact_save_click.click()
        self.driver.execute_script("window.scrollTo(0,200)")
        emergency_click=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,project1test_data.TestSelectors.emergency_click_xpath)))
        emergency_click.click()
        ########################### ADDING EMERGENCY CONTACT###################
        add_details=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,project1test_data.TestSelectors.emergency_add_xpath)))
        add_details.click()
        #########################EMERGENCY CONTACT DETAILS#################
        ename_details=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,project1test_data.TestSelectors.ename_xpath)))
        ename_details.send_keys("Bharat")
        erelation_details=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,project1test_data.TestSelectors.erelation_xpath)))
        erelation_details.send_keys("Spouse")
        emobile_details=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,project1test_data.TestSelectors.emobile_xpath)))
        emobile_details.send_keys("123456789")
        esave_click=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,project1test_data.TestSelectors.esave_xpath)))
        esave_click.click()
        self.driver.execute_script("window.scrollTo(0,200)")
        ########################DEPENDENT DETAILS###############
        dependent_click=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,project1test_data.TestSelectors.dependent_xpath)))
        dependent_click.click()
        dependent_add=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,project1test_data.TestSelectors.dependent_add_xpath)))
        dependent_add.click()
        dname_details=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,project1test_data.TestSelectors.dname_xpath)))
        dname_details.send_keys("Gnanvika")
        #drelation=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,data4.TestSelectors.drelation_xpath)))
        #drelation_select=Select(drelation)
        #drelation_select.select_by_visible_text("Child")
        ddob_details=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,project1test_data.TestSelectors.dob_xpath)))
        ddob_details.send_keys("2021-29-09")
        dsave_click=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,project1test_data.TestSelectors.dsave_xpath)))
        dsave_click.click()
        self.driver.execute_script("window.scrollTo(0,200)")
        assert self.driver.find_element(By.XPATH,
                                        '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[1]/div[1]/h6').text == "Amani Desu"
        print("Succeessfully updated the details of the employee")




