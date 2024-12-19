import allure
import random
from base.base_test import BaseTest
from utils.fake_data_generator import FakeDataGenerator


class TestRegistration(BaseTest):

    @allure.feature("Registration")
    @allure.description("""
    This test verifies that a new account can be successfully registered using valid email, password, and username information.
    """)
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("TC01: Successful registration of a new account with valid information.")
    def test_registration(self, delete_account):
        fake = FakeDataGenerator()
        email = fake.email
        password = fake.password
        username = fake.username
        # Steps:
        self.signup_page.open()
        self.signup_page.is_page_heading_signup()
        self.signup_page.enter_email(email)
        self.signup_page.enter_password(password)
        self.signup_page.click_signup_with_email_button()
        self.signup_page.enter_username(username)
        self.signup_page.click_continue_button()
        self.signup_page.select_personal_checkbox()
        self.signup_page.select_education_checkbox()
        self.signup_page.click_launch_todoist_button()
        self.home_page.is_opened()
        self.home_page.is_sidebar_contains_username(username)
        # Postconditions:
        with allure.step("Postconditions: Delete the created account."):
            delete_account(email, password)

    @allure.feature("Registration")
    @allure.description("""
    This test verifies that a new user cannot register an account when providing invalid information, such as incorrect email format, missing password, or other invalid inputs.
    """)
    @allure.severity(allure.severity_level.MINOR)
    @allure.title("TC08: Unsuccessful registration of a new account with invalid information.")
    def test_unsuccessful_registration(self):
        fake = FakeDataGenerator()
        email = fake.email
        password = fake.password
        invalid_email = self.data.EMAIL
        invalid_password = str(random.randint(1000000, 9999999))
        # Steps:
        self.signup_page.open()
        self.signup_page.is_page_heading_signup()
        self.signup_page.enter_email(invalid_email)
        self.signup_page.enter_password(password)
        self.signup_page.click_signup_with_email_button()
        self.signup_page.is_error_message_visible()
        self.signup_page.is_page_heading_signup()
        self.signup_page.enter_email(email)
        self.signup_page.enter_password(invalid_password)
        self.signup_page.click_signup_with_email_button()
        self.signup_page.is_page_heading_signup()
