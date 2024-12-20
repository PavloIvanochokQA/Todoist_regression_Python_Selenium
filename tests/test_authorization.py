import allure
import pytest
from base.base_test import BaseTest
from utils.fake_data_generator import FakeDataGenerator


class TestAuthorization(BaseTest):

    @allure.feature("Authorization")
    @allure.description("""
    This test verifies that a user can successfully login to an existing account using valid email and password credentials.
    """)
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("TC02: Successful login to an existing account with valid information.")
    def test_authorization(self):
        # Steps:
        self.login_page.open()
        self.login_page.is_page_heading_login()
        self.login_page.enter_email(self.data.EMAIL)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_login_button()
        self.home_page.is_opened()
        self.home_page.is_sidebar_contains_username(self.data.USERNAME)

    @allure.feature("Authorization")
    @allure.description("""
    This test verifies that a user can successfully logout from an account and is redirected to the login page.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("TC03: Successful logout from an account.")
    def test_logout(self, login):
        # Steps:
        self.home_page.click_username_button()
        self.home_page.click_logout_button()
        self.login_page.is_opened()
        self.login_page.is_page_heading_login()

    @allure.feature("Authorization")
    @allure.description("""
    This test verifies that a user can successfully login using a Google account, including the authorization process via Google's login page.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("TC04: Ability to login using a Google account.")
    @pytest.mark.skip(reason="The test is skipped because a CAPTCHA pass is sometimes required")
    def test_authorization_using_google(self):
        # Steps:
        self.login_page.open()
        self.login_page.is_page_heading_login()
        self.login_page.click_continue_with_google_button()
        self.google_account_page.is_opened()
        self.google_account_page.enter_gmail(self.data.GMAIL)
        self.google_account_page.click_confirm_gmail_button()
        self.google_account_page.enter_gmail_password(self.data.GMAIL_PASSWORD)
        self.google_account_page.click_confirm_password_button()
        self.home_page.is_opened()
        self.home_page.is_sidebar_contains_username(self.data.GMAIL_USERNAME)

    @allure.feature("Authorization")
    @allure.description("""
    This test verifies that a user cannot login to an existing account using invalid credentials, such as incorrect email or password.
    """)
    @allure.severity(allure.severity_level.MINOR)
    @allure.title("TC09: Unsuccessful login to an existing account with invalid information.")
    def test_unsuccessful_authorization(self):
        fake = FakeDataGenerator()
        email = self.data.EMAIL
        password = self.data.PASSWORD
        invalid_email = fake.email
        invalid_password = fake.password
        # Steps:
        self.login_page.open()
        self.login_page.is_page_heading_login()
        self.login_page.enter_email(invalid_email)
        self.login_page.enter_password(password)
        self.login_page.click_login_button()
        self.login_page.is_error_message_visible()
        self.login_page.is_opened()
        self.login_page.enter_email(email)
        self.login_page.enter_password(invalid_password)
        self.login_page.click_login_button()
        self.login_page.is_error_message_visible()
        self.login_page.is_opened()
