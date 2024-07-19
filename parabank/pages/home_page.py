from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.register_link = (By.LINK_TEXT, "Register")

    def click_register(self):
        self.driver.find_element(*self.register_link).click()
