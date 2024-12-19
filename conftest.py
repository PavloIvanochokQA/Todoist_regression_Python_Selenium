import pytest
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from pages.profile_management_pages import AccountManagementPage
from pages.profile_management_pages import DeleteManagementPage
from pages.account_deleted_page import AccountDeletedPage
from pages.projects_page import ProjectsPage
from utils.fake_data_generator import FakeDataGenerator
from config.data import Data


@pytest.fixture(scope='function', autouse=True)
def driver(request):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def login(driver):
    login_page = LoginPage(driver)
    home_page = HomePage(driver)
    login_page.open()
    login_page.enter_email(Data.EMAIL)
    login_page.enter_password(Data.PASSWORD)
    login_page.click_login_button()
    home_page.is_opened()
    return home_page


@pytest.fixture(scope="function")
def create_account(driver):
    signup_page = SignupPage(driver)
    home_page = HomePage(driver)
    fake = FakeDataGenerator()
    email = fake.email
    password = fake.password
    username = fake.username
    signup_page.open()
    signup_page.enter_email(email)
    signup_page.enter_password(password)
    signup_page.click_signup_with_email_button()
    signup_page.enter_username(username)
    signup_page.click_continue_button()
    signup_page.select_personal_checkbox()
    signup_page.click_launch_todoist_button()
    home_page.is_opened()
    return email, password, username


@pytest.fixture(scope="function")
def delete_account(driver):
    home_page = HomePage(driver)
    delete_management_page = DeleteManagementPage(driver)
    account_management_page = AccountManagementPage(driver)
    account_deleted_page = AccountDeletedPage(driver)

    def _delete_account(email, password):
        home_page.open()
        home_page.click_username_button()
        home_page.click_settings_button()
        account_management_page.click_delete_account_button()
        delete_management_page.enter_email(email)
        delete_management_page.enter_password(password)
        delete_management_page.click_delete_account_button()
        account_deleted_page.is_opened()
    return _delete_account


@pytest.fixture(scope="function")
def create_task(driver):
    home_page = HomePage(driver)
    fake = FakeDataGenerator()
    task_name = fake.task_name
    task_description = fake.task_description
    task_priority = random.randint(1, 4)
    home_page.click_add_task_button()
    home_page.enter_task_name(task_name)
    home_page.enter_description(task_description)
    home_page.set_task_priority(task_priority)
    home_page.click_submit_add_task_button()
    home_page.is_task_list_contains_task(task_name)
    return task_name, task_description, task_priority


@pytest.fixture(scope="function")
def delete_task(driver):
    def delete(task_name):
        home_page = HomePage(driver)
        home_page.open()
        home_page.click_more_actions_button(task_name)
        home_page.click_delete_button()
        home_page.confirm_deletion()
    return delete


@pytest.fixture(scope="function")
def create_task_list(driver):
    home_page = HomePage(driver)
    projects_page = ProjectsPage(driver)
    fake = FakeDataGenerator()
    project_name = fake.project_name
    home_page.click_my_projects_button()
    projects_page.is_opened()
    projects_page.click_my_projects_menu_button()
    projects_page.click_add_project_button()
    projects_page.enter_project_name(project_name)
    projects_page.choose_list()
    projects_page.click_add_button()
    projects_page.is_my_projects_section_contains_project(project_name)
    return project_name


@pytest.fixture(scope="function")
def delete_project(driver):
    def delete(project_name):
        home_page = HomePage(driver)
        projects_page = ProjectsPage(driver)
        home_page.click_my_projects_button()
        projects_page.open_project(project_name)
        projects_page.click_more_actions_button()
        projects_page.click_delete_button()
        projects_page.is_my_project_section_not_contains_project(project_name)
    return delete


@pytest.fixture(scope="function")
def create_task_board(driver):
    projects_page = ProjectsPage(driver)
    fake = FakeDataGenerator()
    first_section = "To Do"
    second_section = "In Progress"
    third_section = "Done"
    project_name = fake.project_name
    projects_page.click_my_projects_button()
    projects_page.click_my_projects_menu_button()
    projects_page.click_add_project_button()
    projects_page.enter_project_name(project_name)
    projects_page.choose_board()
    projects_page.click_add_button()
    projects_page.is_my_projects_section_contains_project(project_name)
    projects_page.enter_section_name(first_section)
    projects_page.click_confirm_add_section_button()
    projects_page.click_add_section_button()
    projects_page.enter_section_name(second_section)
    projects_page.click_confirm_add_section_button()
    projects_page.click_add_section_button()
    projects_page.enter_section_name(third_section)
    projects_page.click_confirm_add_section_button()
    return project_name, first_section, second_section, third_section
