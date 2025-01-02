import allure
from base.base_page import BasePage
from config.links import Links
from selenium.common.exceptions import TimeoutException


class SignupPage(BasePage):

    PAGE_URL = Links.SIGNUP_PAGE

    EMAIL_FIELD = ("xpath", "//input[@type='email']")
    PASSWORD_FIELD = ("xpath", "//input[@type='password']")
    YOUR_NAME_FIELD = ("xpath", "//input[@type='text']")
    SIGNUP_WITH_EMAIL_BUTTON = ("xpath", "//button[@type='submit']")
    CONTINUE_BUTTON = ("xpath", "//button[@type='submit']")
    LAUNCH_TODOIST_BUTTON = ("xpath", "//button[@aria-label='Launch Todoist']")
    PERSONAL_CHECKBOX = ("xpath", "//button[@data-gtm-id='personal']")
    WORK_CHECKBOX = ("xpath", "//button[@data-gtm-id='work']")
    EDUCATION_CHECKBOX = ("xpath", "//button[@data-gtm-id='education']")
    PAGE_HEADING = ("xpath", "//div[@class='fb8d74bb']//h1")
    ERROR_MESSAGE = ("xpath", "//form/div[@class='a83bd4e0 _266d6623 _8f5b5f2b fb8d74bb']")

    @allure.step("Enter email into the \"Email\" field.")
    def enter_email(self, email):
        self.enter_text(self.EMAIL_FIELD, email)

    @allure.step("Enter password into the \"Password\" field.")
    def enter_password(self, password):
        self.enter_text(self.PASSWORD_FIELD, password)

    @allure.step("Click on the \"Sign up with Email\" button.")
    def click_signup_with_email_button(self):
        self.click_element(self.SIGNUP_WITH_EMAIL_BUTTON)

    @allure.step("Enter username into the \"Your name\" field.")
    def enter_username(self, username):
        self.enter_text(self.YOUR_NAME_FIELD, username)

    @allure.step("Click on the \"Continue\" button.")
    def click_continue_button(self):
        self.click_element(self.CONTINUE_BUTTON)

    @allure.step("Select \"Personal\" checkbox.")
    def select_personal_checkbox(self):
        self.click_element(self.PERSONAL_CHECKBOX)

    @allure.step("Select \"Work\" checkbox.")
    def select_work_checkbox(self):
        self.click_element(self.WORK_CHECKBOX)

    @allure.step("Select \"Education\" checkbox.")
    def select_education_checkbox(self):
        self.click_element(self.EDUCATION_CHECKBOX)

    @allure.step("Click on the \"Launch Todoist\" button.")
    def click_launch_todoist_button(self):
        self.wait.until(lambda driver: driver.find_element(
            *self.LAUNCH_TODOIST_BUTTON).get_attribute("aria-disabled") == "false")
        self.driver.find_element(*self.LAUNCH_TODOIST_BUTTON).click()

    @allure.step("Verify that the page heading is \"Sign up\".")
    def is_page_heading_signup(self):
        heading_element = self.wait_for_visibility(self.PAGE_HEADING)
        assert heading_element.text == "Sign up", \
            f"Expected page heading \"Sign up\" but got: \"{heading_element.text}\"."

    @allure.step("Verify that the page displays an error message.")
    def is_error_message_visible(self):
        try:
            self.wait_for_visibility(self.ERROR_MESSAGE)
        except:
            raise TimeoutException("Error message not found.")
