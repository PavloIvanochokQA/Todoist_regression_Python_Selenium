import pytest
import random
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from pages.profile_management_pages import DeleteManagementPage
from pages.account_deleted_page import AccountDeletedPage
from pages.projects_page import ProjectsPage
from utils.fake_data_generator import FakeDataGenerator
from config.data import Data
from utils.screenshot import take_screenshot


@pytest.fixture(scope='function', autouse=True)
def driver(request):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def login(driver):
    login_page = LoginPage(driver)
    home_page = HomePage(driver)
    try:
        login_page.open()
        login_page.enter_email(Data.EMAIL)
        login_page.enter_password(Data.PASSWORD)
        login_page.click_login_button()
        home_page.is_opened()
    except Exception as e:
        take_screenshot(driver, "Login Failed")
        raise e


@pytest.fixture(scope="function")
def create_account(driver):
    signup_page = SignupPage(driver)
    home_page = HomePage(driver)
    fake = FakeDataGenerator()
    email = fake.email
    password = fake.password
    username = fake.username
    try:
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
    except Exception as e:
        take_screenshot(driver, "Account Creation Failed")
        raise e


@pytest.fixture(scope="function")
def delete_account(driver):
    delete_management_page = DeleteManagementPage(driver)
    account_deleted_page = AccountDeletedPage(driver)

    def delete(email, password):
        try:
            time.sleep(2)
            delete_management_page.open()
            time.sleep(2)
            delete_management_page.enter_email(email)
            delete_management_page.enter_password(password)
            delete_management_page.click_delete_account_button()
            account_deleted_page.is_opened()
        except Exception as e:
            take_screenshot(driver, "Account Deletion Failed")
            raise e
    return delete


@pytest.fixture(scope="function")
def create_task(driver):
    home_page = HomePage(driver)
    fake = FakeDataGenerator()
    task_name = fake.task_name
    task_description = fake.task_description
    task_priority = random.randint(1, 4)
    try:
        home_page.click_add_task_button()
        home_page.enter_task_name(task_name)
        home_page.enter_description(task_description)
        home_page.set_task_priority(task_priority)
        home_page.click_submit_add_task_button()
        return task_name, task_description, task_priority
    except Exception as e:
        take_screenshot(driver, "Task Creation Failed")
        raise e


@pytest.fixture(scope="function")
def delete_task(driver):
    home_page = HomePage(driver)

    def delete(task_name):
        try:
            time.sleep(2)
            home_page.open()
            time.sleep(2)
            home_page.click_more_actions_button(task_name)
            time.sleep(2)
            home_page.click_delete_button()
            home_page.confirm_deletion()
        except Exception as e:
            take_screenshot(driver, "Task Deletion Failed")
            raise e
    return delete


@pytest.fixture(scope="function")
def create_task_list(driver):
    home_page = HomePage(driver)
    projects_page = ProjectsPage(driver)
    fake = FakeDataGenerator()
    project_name = fake.project_name
    try:
        home_page.click_my_projects_button()
        projects_page.is_opened()
        projects_page.click_my_projects_menu_button()
        projects_page.click_add_project_button()
        projects_page.enter_project_name(project_name)
        projects_page.choose_list()
        projects_page.click_add_button()
        return project_name
    except Exception as e:
        take_screenshot(driver, "Task List Creation Failed")
        raise e


@pytest.fixture(scope="function")
def create_task_board(driver):
    projects_page = ProjectsPage(driver)
    fake = FakeDataGenerator()
    first_section = "To Do"
    second_section = "In Progress"
    third_section = "Done"
    project_name = fake.project_name
    try:
        projects_page.click_my_projects_button()
        projects_page.click_my_projects_menu_button()
        projects_page.click_add_project_button()
        projects_page.enter_project_name(project_name)
        projects_page.choose_board()
        projects_page.click_add_button()
        projects_page.enter_section_name(first_section)
        projects_page.click_confirm_add_section_button()
        projects_page.click_add_section_button()
        projects_page.enter_section_name(second_section)
        projects_page.click_confirm_add_section_button()
        projects_page.click_add_section_button()
        projects_page.enter_section_name(third_section)
        projects_page.click_confirm_add_section_button()
        return project_name, first_section, second_section, third_section
    except Exception as e:
        take_screenshot(driver, "Task Board Creation Failed")
        raise e
