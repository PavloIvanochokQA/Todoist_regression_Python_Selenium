import pytest
from config.data import Data
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from pages.home_page import HomePage
from pages.google_account_page import GoogleAccountPage
from pages.profile_management_pages import AccountManagementPage
from pages.profile_management_pages import PasswordManagementPage
from pages.profile_management_pages import EmailManagementPage
from pages.profile_management_pages import DeleteManagementPage
from pages.account_deleted_page import AccountDeletedPage
from pages.task_page import TaskPage
from pages.projects_page import ProjectsPage
from pages.search_page import SearchPage


class BaseTest:

    data: Data
    login_page: LoginPage
    signup_page: SignupPage
    home_page: HomePage
    google_account_page: GoogleAccountPage
    account_management_page: AccountManagementPage
    password_management_page: PasswordManagementPage
    email_management_page: EmailManagementPage
    delete_management_page: DeleteManagementPage
    account_deleted_page: AccountDeletedPage
    task_page: TaskPage
    projects_page: ProjectsPage
    search_page: SearchPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.data = Data
        request.cls.login_page = LoginPage(driver)
        request.cls.signup_page = SignupPage(driver)
        request.cls.home_page = HomePage(driver)
        request.cls.google_account_page = GoogleAccountPage(driver)
        request.cls.account_management_page = AccountManagementPage(driver)
        request.cls.password_management_page = PasswordManagementPage(driver)
        request.cls.email_management_page = EmailManagementPage(driver)
        request.cls.delete_management_page = DeleteManagementPage(driver)
        request.cls.account_deleted_page = AccountDeletedPage(driver)
        request.cls.task_page = TaskPage(driver)
        request.cls.projects_page = ProjectsPage(driver)
        request.cls.search_page = SearchPage(driver)
