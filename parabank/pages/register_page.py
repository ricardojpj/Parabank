from selenium.webdriver.common.by import By

class RegisterPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_field = (By.ID, "customer.firstName")
        self.last_name_field = (By.ID, "customer.lastName")
        self.address_field = (By.ID, "customer.address.street")
        self.city_field = (By.ID, "customer.address.city")
        self.state_field = (By.ID, "customer.address.state")
        self.zip_code_field = (By.ID, "customer.address.zipCode")
        self.phone_field = (By.ID, "customer.phoneNumber")
        self.ssn_field = (By.ID, "customer.ssn")
        self.username_field = (By.ID, "customer.username")
        self.password_field = (By.ID, "customer.password")
        self.confirm_password_field = (By.ID, "repeatedPassword")
        self.register_button = (By.CSS_SELECTOR, "input[value='Register']")
        self.error_message = (By.CLASS_NAME, "error")

    def fill_form(self, first_name, last_name, address, city, state, zip_code, phone, ssn, username, password, confirm_password):
        self.driver.find_element(*self.first_name_field).send_keys(first_name)
        self.driver.find_element(*self.last_name_field).send_keys(last_name)
        self.driver.find_element(*self.address_field).send_keys(address)
        self.driver.find_element(*self.city_field).send_keys(city)
        self.driver.find_element(*self.state_field).send_keys(state)
        self.driver.find_element(*self.zip_code_field).send_keys(zip_code)
        self.driver.find_element(*self.phone_field).send_keys(phone)
        self.driver.find_element(*self.ssn_field).send_keys(ssn)
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.confirm_password_field).send_keys(confirm_password)

    def submit_form(self):
        self.driver.find_element(*self.register_button).click()

    def get_error_message(self):
        return self.driver.find_element(*self.error_message).text

    def is_error_message_displayed(self):
        return self.driver.find_element(*self.error_message).is_displayed()
