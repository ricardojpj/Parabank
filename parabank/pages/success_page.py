from selenium.webdriver.common.by import By

class SuccessPage:
    def __init__(self, driver):
        self.driver = driver
        self.success_message = (By.CSS_SELECTOR, ".title")

    def is_success_message_displayed(self):
        return self.driver.find_element(*self.success_message).is_displayed()

    def get_success_message_text(self):
        return self.driver.find_element(*self.success_message).text
