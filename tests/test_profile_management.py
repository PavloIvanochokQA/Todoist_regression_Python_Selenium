import allure
import random
import pytest
from base.base_test import BaseTest
from utils.fake_data_generator import FakeDataGenerator
from utils.screenshot import take_screenshot


class TestProfileManagement(BaseTest):

    @pytest.mark.order(7)
    @pytest.mark.regression
    @allure.feature("Profile Management")
    @allure.description("""
    This test verifies that a user can successfully delete their account by accessing the account settings and following the deletion process.
    """)
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("TC07: Successful account deletion.")
    def test_accound_deletion(self, create_account):
        email, password, username = create_account
        try:
            # Steps:
            self.home_page.click_username_button()
            self.home_page.click_settings_button()
            self.account_management_page.click_delete_account_button()
            self.delete_management_page.is_opened()
            self.delete_management_page.enter_email(email)
            self.delete_management_page.enter_password(password)
            self.delete_management_page.click_delete_account_button()
            self.account_deleted_page.is_opened()
            self.account_deleted_page.is_page_heading_account_deleted()
        except Exception as e:
            take_screenshot(self.driver, "Account Deletion Test Failed")
            raise e

    @pytest.mark.order(5)
    @pytest.mark.regression
    @allure.feature("Profile Management")
    @allure.description("""
    This test verifies that a user can successfully change their password through the account settings by entering the current password and a new one.
    """)
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("TC05: Successful password change.")
    def test_password_change(self, create_account, delete_account):
        email, password, username = create_account
        fake = FakeDataGenerator()
        new_password = fake.password
        is_password_changed = False
        try:
            # Steps:
            self.home_page.click_username_button()
            self.home_page.click_settings_button()
            self.account_management_page.click_change_password_button()
            self.password_management_page.is_opened()
            self.password_management_page.enter_password(password)
            self.password_management_page.enter_new_password(new_password)
            self.password_management_page.click_change_password_button()
            self.password_management_page.is_error_message_not_visible()
            self.account_management_page.is_opened()
            is_password_changed = True
        except Exception as e:
            take_screenshot(self.driver, "Password Change Test Failed")
            raise e
        finally:
            # Postconditions:
            with allure.step("Postconditions: Delete the created account."):
                password_to_use = new_password if is_password_changed else password
                delete_account(email, password_to_use)

    @pytest.mark.order(6)
    @pytest.mark.regression
    @allure.feature("Profile Management")
    @allure.description("""
    This test verifies that a user can successfully change their email address and username through the account settings.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("TC06: Successful email and username change.")
    def test_email_and_username_change(self, create_account, delete_account):
        email, password, username = create_account
        fake = FakeDataGenerator()
        new_email = fake.email
        new_username = fake.username
        is_email_changed = False
        try:
            # Steps:
            self.home_page.click_username_button()
            self.home_page.click_settings_button()
            self.account_management_page.click_change_email_button()
            self.email_management_page.is_opened()
            self.email_management_page.enter_new_email(new_email)
            self.email_management_page.enter_password(password)
            self.email_management_page.click_change_email_button()
            self.email_management_page.is_error_message_not_visible()
            self.account_management_page.is_opened()
            is_email_changed = True
            self.account_management_page.enter_new_username(new_username)
            self.account_management_page.click_update_button()
            self.account_management_page.click_close_settings_button()
            self.home_page.is_sidebar_contains_username(new_username)
        except Exception as e:
            take_screenshot(self.driver, "Email and Username Change Test Failed")
            raise e
        finally:
            # Postconditions:
            with allure.step("Postconditions: Delete the created account."):
                email_to_use = new_email if is_email_changed else email
                delete_account(email_to_use, password)

    @pytest.mark.order(10)
    @pytest.mark.regression
    @allure.feature("Profile Management")
    @allure.description("""
    This test verifies that a user cannot change the current password when providing an incorrect current password.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("TC10: Inability to change the current password with an incorrect password.")
    def test_unsuccessful_password_change(self, create_account, delete_account):
        email, password, username = create_account
        fake = FakeDataGenerator()
        new_password = fake.password
        invalid_password = fake.password
        invalid_new_password = str(random.randint(1000000, 9999999))
        try:
            # Steps:
            self.home_page.click_username_button()
            self.home_page.click_settings_button()
            self.account_management_page.click_change_password_button()
            self.password_management_page.is_opened()
            self.password_management_page.enter_password(invalid_password)
            self.password_management_page.enter_new_password(new_password)
            self.password_management_page.click_change_password_button()
            self.password_management_page.is_error_message_visible()
            self.password_management_page.is_opened()
            self.password_management_page.enter_password(password)
            self.password_management_page.enter_new_password(invalid_new_password)
            self.password_management_page.click_change_password_button()
            self.password_management_page.is_error_message_visible()
            self.password_management_page.is_opened()
        except Exception as e:
            take_screenshot(self.driver, "Unsuccessful Password Change Test Failed")
            raise e
        finally:
            # Postconditions:
            with allure.step("Postconditions: Delete the created account."):
                delete_account(email, password)

    @pytest.mark.order(11)
    @pytest.mark.regression
    @allure.feature("Profile Management")
    @allure.description("""
    This test verifies that a user cannot delete their account when providing an incorrect email or password.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("TC11: Inability to delete the account with an incorrect email or password.")
    def test_unsuccessful_account_deletion(self, create_account, delete_account):
        email, password, username = create_account
        fake = FakeDataGenerator()
        invalid_email = fake.email
        invalid_password = fake.password
        try:
            # Steps:
            self.home_page.click_username_button()
            self.home_page.click_settings_button()
            self.account_management_page.click_delete_account_button()
            self.delete_management_page.is_opened()
            self.delete_management_page.enter_email(email)
            self.delete_management_page.enter_password(invalid_password)
            self.delete_management_page.click_delete_account_button()
            self.delete_management_page.is_error_message_visible()
            self.delete_management_page.is_opened()
            self.delete_management_page.enter_email(invalid_email)
            self.delete_management_page.enter_password(password)
            self.delete_management_page.click_delete_account_button()
            self.delete_management_page.is_error_message_visible()
            self.delete_management_page.is_opened()
        except Exception as e:
            take_screenshot(self.driver, "Unsuccessful Account Deletion Test Failed")
            raise e
        finally:
            # Postconditions:
            with allure.step("Postconditions: Delete the created account."):
                delete_account(email, password)
