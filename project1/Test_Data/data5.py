class TestData:
    username = "Admin"
    password = "admin123"
    firstname = "Amani"
    middlename = "Anna"
    lastname = "Desu"
    hintname="Amani Anna Desu"

# Python Class for Selenium Selectors
class TestSelectors:
    input_box_username = "username"
    input_box_password = "password"
    login_xpath = "//button[@type='submit']"
    pim_xpath = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span'
    add_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button'
    firstname_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input'
    middlename_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[2]/div[2]/input'
    lastname_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input'
    # image_xpath='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[1]/div/div[2]/div/button'
    save_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]'
    existing_xpath='//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a'
    hintsearch_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input'
    search_xpath='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]'
    ##########################3DELETING THE EXISTING EMPLOYEE########
    delete_xpath='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[9]/div/button[1]'
    sure_xpath='//*[@id="app"]/div[3]/div/div/div/div[3]/button[2]'