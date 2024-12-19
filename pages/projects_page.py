import allure
import time
from pages.home_page import HomePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException


class ProjectsPage(HomePage):

    PAGE_URL = Links.PROJECTS_PAGE

    MY_PROJECTS_MENU_BUTTON = (
        "xpath", "//div[@class='imKBXQv fb8d74bb _4e9ab24b']//button[@aria-label='My projects menu']")
    ADD_PROJECT_BUTTON = ("xpath", "//div[@role='menuitem']")
    PROJECT_NAME_FIELD = ("xpath", "//input[@name='name']")
    CHOOSE_LIST_BUTTON = ("xpath", "//label[@for='LIST']")
    ADD_BUTTON = ("xpath", "//button[@type='submit']")
    CHOOSE_BOARD_BUTTON = ("xpath", "//label[@for='BOARD']")
    NAME_THIS_SECTION_FIELD = ("xpath", "//input[@aria-label='Name this section']")
    ADD_SECTION_BUTTON = ("xpath", "//span[@class='board_add_section_button__label']")
    CONFIRM_ADD_SECTION_BUTTON = ("xpath", "//button[@type='submit']")
    MORE_ACTIONS_BUTTON = ("xpath", "//button[@aria-label='Project options menu']")
    EDIT_BUTTON = ("xpath", "(//div[@role='menuitem'])[1]")
    SAVE_BUTTON = ("xpath", "//button[@type='submit']")
    BOARD_SECTION = ("xpath", "//div[@class='board_view__sections']")
    DELETE_BUTTON = ("xpath", "//div[text()='Delete']")
    CONFIRM_DELETION_BUTTON = ("xpath", "//button[@data-autofocus='true']")
    DUPLICATE_BUTTON = ("xpath", "//div[text()='Duplicate']")
    ARCHIVE_BUTTON = ("xpath", "//div[text()='Archive']")
    CONFIRM_ARCHIVAL_BUTTON = ("xpath", "//button[@data-autofocus='true']")
    ACTIVE_PROJECTS_BUTTON = ("xpath", "//button[text()='Active projects']")
    ARCHIVED_PROJECTS_BUTTON = ("xpath", "//a[@href='/app/projects/archived']")
    PROJECT_ARCHIVED_MESSAGE = ("xpath", "//div[@class='fb8d74bb c4803194 b0e6eab4']/div")
    UNARCHIVE_BUTTON = ("xpath", "//button[@class='fb8d74bb _56a651f6 _3930afa0 _7ea1378e _7246d092']")
    MOVE_TO_BUTTON = ("xpath", "//div[@data-action-hint='task-overflow-menu-move-to-project']")

    def is_opened(self):
        with allure.step(f"Verify that the page with a URL starting with {self.PAGE_URL} is opened."):
            self.wait.until(EC.url_contains(self.PAGE_URL))

    @allure.step("Click on the \"My projects menu\" button.")
    def click_my_projects_menu_button(self):
        self.click_element(self.MY_PROJECTS_MENU_BUTTON)

    @allure.step("Click on the \"Add project\" button.")
    def click_add_project_button(self):
        self.click_element(self.ADD_PROJECT_BUTTON)

    @allure.step("Enter project name into the \"Name\" field.")
    def enter_project_name(self, project_name):
        self.enter_text(self.PROJECT_NAME_FIELD, project_name)

    @allure.step("Choose List as the project type.")
    def choose_list(self):
        self.click_element(self.CHOOSE_LIST_BUTTON)

    @allure.step("Click on the \"Add\" button.")
    def click_add_button(self):
        self.click_element(self.ADD_BUTTON)
        time.sleep(1)

    @allure.step("Verify that a project appears in the My Projects section.")
    def is_my_projects_section_contains_project(self, project_name):
        project_locator = ("xpath", f"//div[@class='WwLx9J2']//span[text()='{project_name}']")
        try:
            self.wait_for_visibility(project_locator)
        except:
            raise TimeoutException(f"Project \"{project_name}\" not found in the My projects section.")

    @allure.step("Choose Board as the project type.")
    def choose_board(self):
        self.click_element(self.CHOOSE_BOARD_BUTTON)

    @allure.step("Enter Board section name.")
    def enter_section_name(self, section_name):
        self.enter_text(self.NAME_THIS_SECTION_FIELD, section_name)

    @allure.step("Click on the confirm \"Add section\" button.")
    def click_confirm_add_section_button(self):
        self.click_element(self.CONFIRM_ADD_SECTION_BUTTON)

    @allure.step("Click on the \"Add section\" button.")
    def click_add_section_button(self):
        self.click_element(self.ADD_SECTION_BUTTON)

    @allure.step("Verify that the section appears on the Board.")
    def is_board_contains_section(self, section_name):
        section_locator = (
            "xpath", f"//div[@data-testid='project-board-view']//span[text()='{section_name}']")
        try:
            self.wait_for_visibility(section_locator)
        except:
            raise TimeoutException(f"Section \"{section_name}\" not found.")

    @allure.step("Open the project.")
    def open_project(self, project_name):
        project_locator = ("xpath", f"//div[text()='{project_name}']")
        self.click_element(project_locator)

    @allure.step("Click on the \"More actions\" button.")
    def click_more_actions_button(self):
        time.sleep(1)
        self.click_element(self.MORE_ACTIONS_BUTTON)

    @allure.step("Click on the \"Edit\" button.")
    def click_edit_button(self):
        self.click_element(self.EDIT_BUTTON)

    @allure.step("Click on the \"Save\" button.")
    def click_save_button(self):
        self.click_element(self.SAVE_BUTTON)
        time.sleep(1)

    @allure.step("Verify that the board sections are visible.")
    def is_board_sections_visible(self):
        try:
            self.wait_for_visibility(self.BOARD_SECTION)
        except:
            raise TimeoutException("Board sections not found")

    @allure.step("Click on the \"Delete\" button and confirm the deletion.")
    def click_delete_button(self):
        self.click_element(self.DELETE_BUTTON)
        self.click_element(self.CONFIRM_DELETION_BUTTON)
        time.sleep(1)

    @allure.step("Verify that the project is no longer visible in the My Projects section.")
    def is_my_project_section_not_contains_project(self, project_name):
        project_locator = ("xpath", f"//div[@class='WwLx9J2']//span[text()='{project_name}']")
        projects = self.driver.find_elements(*project_locator)
        assert len(projects) == 0, f"Project \"{project_name}\" is still visible in the My Project section."

    @allure.step("Verify that the \"Add\" button is disabled.")
    def is_add_button_disabled(self):
        button_element = self.wait_for_visibility(self.ADD_BUTTON)
        aria_disabled = button_element.get_attribute("aria-disabled")
        assert aria_disabled == "true", "The \"Add\" button is not disabled."

    @allure.step("Click on the \"Duplicate\" button.")
    def click_duplicate_button(self):
        self.click_element(self.DUPLICATE_BUTTON)

    @allure.step("Click on the \"Archive\" button and confirm the archival.")
    def click_archive_button(self):
        self.click_element(self.ARCHIVE_BUTTON)
        self.click_element(self.CONFIRM_ARCHIVAL_BUTTON)
        time.sleep(1)

    @allure.step("Click on the \"Active projects\" button.")
    def click_active_projects_button(self):
        self.click_element(self.ACTIVE_PROJECTS_BUTTON)

    @allure.step("Click on the \"Archived projects\" button.")
    def click_archived_projects_button(self):
        self.click_element(self.ARCHIVED_PROJECTS_BUTTON)

    @allure.step("Verify that the archived section contains the project.")
    def is_archived_section_contains_project(self, project_name):
        project_locator = ("xpath", f"//div[@class='rtqfsfx fb8d74bb']//div[text()='{project_name}']")
        try:
            self.wait_for_visibility(project_locator)
        except:
            raise TimeoutException(f"Project \"{project_name}\" not found in the archived section.")

    @allure.step("Verify that the page displays the message: \"This project is archived\".")
    def is_archived_message_visible(self):
        try:
            self.wait_for_visibility(self.PROJECT_ARCHIVED_MESSAGE)
        except:
            raise TimeoutException("Message \"This project is archived\" not found.")

    @allure.step("Click on the \"Unarchive\" button.")
    def click_unarchive_button(self):
        self.click_element(self.UNARCHIVE_BUTTON)
        time.sleep(1)

    @allure.step("Create a task in the section.")
    def create_task_in_section(self, section, task_name):
        add_task_button_locator = ("xpath", f"//button[@aria-label='Add task to {section}']")
        task_name_field_locator = ("xpath", "//div[@aria-label='Task name']")
        submit_button_locator = ("xpath", "//button[@type='submit']")
        self.click_element(add_task_button_locator)
        self.enter_text(task_name_field_locator, task_name)
        self.click_element(submit_button_locator)

    @allure.step("Click on the \"More actions\" button on the task.")
    def click_more_actions_button_on_task(self, task_name):
        task_locator = ("xpath", f"//div[text()='{task_name}']")
        more_actions_locator = (
            "xpath", f"//div[text()='{task_name}']/ancestor::div[@class='board_task__details']//button[@aria-label='More actions']")
        task_element = self.wait_for_visibility(task_locator)
        ActionChains(self.driver).move_to_element(task_element).perform()
        self.wait_for_visibility(more_actions_locator)
        self.click_element(more_actions_locator)

    @allure.step("Move task to section.")
    def move_task_to_section(self, section_name, project_name):
        self.click_element(self.MOVE_TO_BUTTON)
        target_locator = (
            "xpath", f"//div[text()='{project_name}']/ancestor::li/following-sibling::li//div[text()='{section_name}']")
        self.click_element(target_locator)

    @allure.step("Verify that the task appears in the section.")
    def is_section_contains_task(self, task_name, section_name):
        task_locator = (
            "xpath", f"//span[text()='{section_name}']/ancestor::section//div[text()='{task_name}']")
        try:
            self.wait_for_visibility(task_locator)
        except:
            raise TimeoutException(f"Task \"{task_name}\" not found in the section \"{section_name}\".")
