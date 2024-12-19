import allure
from base.base_page import BasePage
from config.links import Links
from selenium.common.exceptions import TimeoutException


class LoginPage(BasePage):

    PAGE_URL = Links.LOGIN_PAGE

    EMAIL_FIELD = ("xpath", "//input[@type='email']")
    PASSWORD_FIELD = ("xpath", "//input[@type='password']")
    LOGIN_BUTTON = ("xpath", "//button[@type='submit']")
    USERNAME_BUTTON = ("xpath", "//button[@aria-label='Settings']")
    GOOGLE_BUTTON = ("xpath", "//a[@data-gtm-id='google-provider-link']")
    PAGE_HEADING = ("xpath", "//div[@class='fb8d74bb']//h1")
    ERROR_MESSAGE = ("xpath", "//form/div[@class='a83bd4e0 _266d6623 _8f5b5f2b fb8d74bb']")

    @allure.step("Enter email into the \"Email\" field.")
    def enter_email(self, email):
        self.enter_text(self.EMAIL_FIELD, email)

    @allure.step("Enter password into the \"Password\" field.")
    def enter_password(self, password):
        self.enter_text(self.PASSWORD_FIELD, password)

    @allure.step("Click on the \"Log in\" button.")
    def click_login_button(self):
        self.click_element(self.LOGIN_BUTTON)

    @allure.step("Click on the \"Continue with Google\" button.")
    def click_continue_with_google_button(self):
        self.click_element(self.GOOGLE_BUTTON)

    @allure.step("Verify that the page heading is \"Log in\".")
    def is_page_heading_login(self):
        heading_element = self.wait_for_visibility(self.PAGE_HEADING)
        assert heading_element.text == "Log in", f"Expected \"Log in\" but got \"{heading_element.text}\"."

    @allure.step("Verify that the page displays an error message.")
    def is_error_message_visible(self):
        try:
            self.wait_for_visibility(self.ERROR_MESSAGE)
        except:
            raise TimeoutException("Error message not found.")
