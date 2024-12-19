import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait


class AccountManagementPage(BasePage):

    PAGE_URL = Links.ACCOUNT_SETTINGS_PAGE

    NAME_FIELD = ("xpath", "//input[@name='name']")
    EMAIL_FIELD = ("xpath", "//div/div[@class='a83bd4e0 fb8d74bb']")
    CHANGE_PASSWORD_BUTTON = ("xpath", "//a[@href='/app/settings/account/password']")
    CHANGE_EMAIL_BUTTON = ("xpath", "//a[@href='/app/settings/account/email']")
    DELETE_ACCOUNT_BUTTON = ("xpath", "//a[@href='/app/settings/account/delete']")
    UPDATE_BUTTON = ("xpath", "//button[@type='submit']")
    CLOSE_SETTINGS_BUTTON = ("xpath", "//button[@aria-label='Close settings']")
    ERROR_MESSAGE = ("xpath", "(//div[@aria-live='assertive'])[2]/div")

    @allure.step("Click on the \"Change password\" button.")
    def click_change_password_button(self):
        self.click_element(self.CHANGE_PASSWORD_BUTTON)

    @allure.step("Click on the \"Change email\" button.")
    def click_change_email_button(self):
        self.click_element(self.CHANGE_EMAIL_BUTTON)

    @allure.step("Click on the \"Delete account\" button.")
    def click_delete_account_button(self):
        self.click_element(self.DELETE_ACCOUNT_BUTTON)

    @allure.step("Enter new username into the \"Name\" field.")
    def enter_new_username(self, new_username):
        self.enter_text(self.NAME_FIELD, new_username)

    @allure.step("Click on the \"Update\" button.")
    def click_update_button(self):
        self.click_element(self.UPDATE_BUTTON)

    @allure.step("Click on the \"Close settings\" button.")
    def click_close_settings_button(self):
        self.click_element(self.CLOSE_SETTINGS_BUTTON)

    @allure.step("Verify that the page displays an error message.")
    def is_error_message_visible(self):
        try:
            self.wait_for_visibility(self.ERROR_MESSAGE)
        except:
            raise TimeoutException("Error message not found.")

    @allure.step("Verify that the error message is not visible.")
    def is_error_message_not_visible(self):
        try:
            error_element = WebDriverWait(self.driver, 2).until(
                EC.visibility_of_element_located(self.ERROR_MESSAGE))
            assert False, f"Error message: {error_element.text}"
        except TimeoutException:
            assert True


class PasswordManagementPage(AccountManagementPage):

    PAGE_URL = Links.PASSWORD_SETTINGS_PAGE

    CURRENT_PASSWORD_FIELD = ("xpath", "(//input[@type='password'])[1]")
    NEW_PASSWORD_FIELD = ("xpath", "(//input[@type='password'])[2]")
    CONFIRM_NEW_PASSWORD_FIELD = ("xpath", "(//input[@type='password'])[3]")
    CHANGE_PASSWORD_BUTTON = ("xpath", "//button[@type='submit']")

    @allure.step("Enter current password into the \"Current password\" field.")
    def enter_password(self, current_password):
        self.enter_text(self.CURRENT_PASSWORD_FIELD, current_password)

    @allure.step("Enter new password into the \"New password\" and \"Confirm new password\" fields.")
    def enter_new_password(self, new_password):
        self.enter_text(self.NEW_PASSWORD_FIELD, new_password)
        self.enter_text(self.CONFIRM_NEW_PASSWORD_FIELD, new_password)

    @allure.step("Click on the \"Change password\" button.")
    def click_change_password_button(self):
        self.click_element(self.CHANGE_PASSWORD_BUTTON)


class EmailManagementPage(AccountManagementPage):

    PAGE_URL = Links.EMAIL_SETTINGS_PAGE

    NEW_EMAIL_FIELD = ("xpath", "(//input[@type='email'])[1]")
    CONFIRM_NEW_EMAIL_FIELD = ("xpath", "(//input[@type='email'])[2]")
    TODOIST_PASSWORD_FIELD = ("xpath", "//input[@type='password']")
    CHANGE_EMAIL_BUTTON = ("xpath", "//button[@type='submit']")

    @allure.step("Enter new email into the \"New email\" and \"Confirm new email\" fields.")
    def enter_new_email(self, new_email):
        self.enter_text(self.NEW_EMAIL_FIELD, new_email)
        self.enter_text(self.CONFIRM_NEW_EMAIL_FIELD, new_email)

    @allure.step("Enter password into the \"Todoist password\" field.")
    def enter_password(self, password):
        self.enter_text(self.TODOIST_PASSWORD_FIELD, password)

    @allure.step("Click on the \"Change email\" button.")
    def click_change_email_button(self):
        self.click_element(self.CHANGE_EMAIL_BUTTON)


class DeleteManagementPage(AccountManagementPage):

    PAGE_URL = Links.DELETE_SETTINGS_PAGE

    TODOIST_EMAIL_FIELD = ("xpath", "(//input[@type='text'])[2]")
    TODOIST_PASSWORD_FIELD = ("xpath", "//input[@type='password']")
    DELETE_ACCOUNT_BUTTON = ("xpath", "//button[@type='submit']")
    ERROR_MESSAGE = ("xpath", "//div[@aria-live='polite']")

    @allure.step("Enter email into the \"Todoist email\" field.")
    def enter_email(self, email):
        self.enter_text(self.TODOIST_EMAIL_FIELD, email)

    @allure.step("Enter password into the \"Todoist password\" field.")
    def enter_password(self, password):
        self.enter_text(self.TODOIST_PASSWORD_FIELD, password)

    @allure.step("Click on the \"Delete account\" button.")
    def click_delete_account_button(self):
        self.click_element(self.DELETE_ACCOUNT_BUTTON)
