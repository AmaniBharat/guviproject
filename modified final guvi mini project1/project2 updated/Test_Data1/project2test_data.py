
# Python Class for Username and Password
class TestData:
    username = "Admin"
    password = "admin123"


# Python Class for Selenium Selectors
class TestSelectors:

    input_box_username = "username"
    input_box_password = "password"
    forgot_xpath='//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[4]/p'

##################reset details##############

    rusername_xpath='//*[@id="app"]/div[1]/div[1]/div/form/div[1]/div/div[2]/input'
    reset_xpath='//*[@id="app"]/div[1]/div[1]/div/form/div[2]/button[2]'

##################admin elements fetching##########

    login_xpath = "//button[@type='submit']"
    admin_xpath='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a'
