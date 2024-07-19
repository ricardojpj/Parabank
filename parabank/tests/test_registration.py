import unittest
from selenium import webdriver
import sys
from pages.home_page import HomePage
from pages.register_page import RegisterPage
from pages.success_page import SuccessPage
from utils.webdriver_setup import get_driver

class TestRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = get_driver()
        self.driver.get("https://parabank.parasoft.com/parabank/index.htm")
        self.home_page = HomePage(self.driver)
        self.register_page = RegisterPage(self.driver)
        self.success_page = SuccessPage(self.driver)

    def test_successful_registration(self):
        self.home_page.click_register()
        self.register_page.fill_form("Ricardo", "Parras", "avenida", "sucre", "pueblo libre", "12345", "123-456-7890", "123-45-6789", "ricardoparras", "password12", "password12")
        self.register_page.submit_form()
        self.assertTrue(self.success_page.is_success_message_displayed())
        self.assertEqual(self.success_page.get_success_message_text(), "Cuentra creada. Bienvenido!")

    def test_existing_account_registration(self):
        self.home_page.click_register()
        self.register_page.fill_form("Ricardo", "Parras", "avenida", "sucre", "pueblo libre", "12345", "123-456-7890", "123-45-6789", "ricardoparras", "password12", "password12")
        self.register_page.submit_form()
        self.assertTrue(self.register_page.is_error_message_displayed())
        self.assertIn("El usuario ya existe!", self.register_page.get_error_message())

    def test_password_mismatch(self):
        self.home_page.click_register()
        self.register_page.fill_form("Ricardo", "Parras", "avenida", "sucre", "pueblo libre", "12345", "123-456-7890", "123-45-6789", "ricardoparras2", "password1", "password2")
        self.register_page.submit_form()
        self.assertTrue(self.register_page.is_error_message_displayed())
        self.assertIn("Los passwords no coinciden!", self.register_page.get_error_message())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
