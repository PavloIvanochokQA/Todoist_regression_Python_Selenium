import allure
from base.base_test import BaseTest
from utils.fake_data_generator import FakeDataGenerator


class TestProjectsManagement(BaseTest):

    @allure.feature("Projects Management")
    @allure.description("""
    This test verifies that a new Task List can be successfully created with a valid name.
    """)
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("TC23: Successful creation of a new Task List.")
    def test_task_list_creation(self, login, delete_project):
        fake = FakeDataGenerator()
        project_name = fake.project_name
        # Steps:
        self.home_page.click_my_projects_button()
        self.projects_page.is_opened()
        self.projects_page.click_my_projects_menu_button()
        self.projects_page.click_add_project_button()
        self.projects_page.enter_project_name(project_name)
        self.projects_page.choose_list()
        self.projects_page.click_add_button()
        self.projects_page.is_my_projects_section_contains_project(project_name)
        # Postconditions:
        with allure.step("Postconditions: Delete the created project."):
            delete_project(project_name)

    @allure.feature("Projects Management")
    @allure.description("""
    This test verifies that a new Task Board can be successfully created with multiple sections.
    """)
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("TC24: Successful creation of a new Task Board with sections.")
    def test_task_board_creation(self, login, delete_project):
        fake = FakeDataGenerator()
        project_name = fake.project_name
        first_section_name = "To Do"
        second_section_name = "In Progress"
        third_section_name = "Done"
        # Steps:
        try:
            self.home_page.click_my_projects_button()
            self.projects_page.is_opened()
            self.projects_page.click_my_projects_menu_button()
            self.projects_page.click_add_project_button()
            self.projects_page.enter_project_name(project_name)
            self.projects_page.choose_board()
            self.projects_page.click_add_button()
            self.projects_page.is_my_projects_section_contains_project(project_name)
            self.projects_page.is_board_sections_visible()
            self.projects_page.enter_section_name(first_section_name)
            self.projects_page.click_confirm_add_section_button()
            self.projects_page.click_add_section_button()
            self.projects_page.enter_section_name(second_section_name)
            self.projects_page.click_confirm_add_section_button()
            self.projects_page.click_add_section_button()
            self.projects_page.enter_section_name(third_section_name)
            self.projects_page.click_confirm_add_section_button()
            self.projects_page.is_board_contains_section(first_section_name)
            self.projects_page.is_board_contains_section(second_section_name)
            self.projects_page.is_board_contains_section(third_section_name)
        # Postconditions:
        finally:
            with allure.step("Postconditions: Delete the created project."):
                delete_project(project_name)

    @allure.feature("Projects Management")
    @allure.description("""
    This test verifies that the project name and type can be successfully changed.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("TC25: Successful change of the Project name and type.")
    def test_project_name_type_change(self, login, create_task_list, delete_project):
        project_name = create_task_list
        fake = FakeDataGenerator()
        new_project_name = fake.project_name
        is_project_name_changed = False
        # Steps:
        try:
            self.projects_page.click_more_actions_button()
            self.projects_page.click_edit_button()
            self.projects_page.enter_project_name(new_project_name)
            self.projects_page.choose_board()
            self.projects_page.click_save_button()
            self.projects_page.is_my_projects_section_contains_project(new_project_name)
            is_project_name_changed = True
            self.projects_page.is_board_sections_visible()
        # Postconditions:
        finally:
            with allure.step("Postconditions: Delete the created project."):
                project_name_to_use = new_project_name if is_project_name_changed else project_name
                delete_project(project_name_to_use)

    @allure.feature("Projects Management")
    @allure.description("""
    This test verifies that a user can successfully delete an existing project.
    """)
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("TC26: Successful deletion of a Project.")
    def test_project_deletion(self, login, create_task_list):
        project_name = create_task_list
        # Steps:
        self.home_page.click_my_projects_button()
        self.projects_page.open_project(project_name)
        self.projects_page.click_more_actions_button()
        self.projects_page.click_delete_button()
        self.projects_page.is_my_project_section_not_contains_project(project_name)

    @allure.feature("Projects Management")
    @allure.description("""
    This test verifies that the system prevents the creation of a new project when invalid information is provided.
    """)
    @allure.severity(allure.severity_level.MINOR)
    @allure.title("TC27: Unsuccessful creation of a new Project due to invalid information.")
    def test_unsuccessful_project_creation(self, login):
        project_name = ""
        # Steps:
        self.home_page.click_my_projects_button()
        self.projects_page.click_my_projects_menu_button()
        self.projects_page.click_add_project_button()
        self.projects_page.enter_project_name(project_name)
        self.projects_page.choose_list()
        self.projects_page.is_add_button_disabled()

    @allure.feature("Projects Management")
    @allure.description("""
    This test verifies that a user can successfully duplicate an existing task list, creating an identical copy.
    """)
    @allure.severity(allure.severity_level.MINOR)
    @allure.title("TC28: Successful duplication of a Task List.")
    def test_task_list_duplication(self, login, create_task_list, create_task, delete_project):
        project_name = create_task_list
        task_name, task_description, task_priority = create_task
        # Steps:
        try:
            self.projects_page.click_more_actions_button()
            self.projects_page.click_duplicate_button()
            self.projects_page.is_my_projects_section_contains_project("Copy of " + project_name)
            self.projects_page.click_my_projects_button()
            self.projects_page.open_project("Copy of " + project_name)
            self.projects_page.is_task_list_contains_task(task_name)
        # Postconditions:
        finally:
            with allure.step("Postconditions: Delete the created project and its duplicate."):
                delete_project(project_name)
                delete_project("Copy of " + project_name)

    @allure.feature("Projects Management")
    @allure.description("""
    This test verifies that a user can successfully archive a project, confirm its archival in the archived projects section, and restore it back to the active projects section.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("TC29: Successful archiving of a Project.")
    def test_project_archiving(self, login, create_task_list, delete_project):
        project_name = create_task_list
        # Steps:
        try:
            self.projects_page.click_more_actions_button()
            self.projects_page.click_archive_button()
            self.projects_page.is_my_project_section_not_contains_project(project_name)
            self.projects_page.click_my_projects_button()
            self.projects_page.click_active_projects_button()
            self.projects_page.click_archived_projects_button()
            self.projects_page.is_archived_section_contains_project(project_name)
            self.projects_page.open_project(project_name)
            self.projects_page.is_archived_message_visible()
            self.projects_page.click_unarchive_button()
            self.projects_page.is_my_projects_section_contains_project(project_name)
        # Postconditions:
        finally:
            with allure.step("Postconditions: Delete the created project."):
                delete_project(project_name)

    @allure.feature("Projects Management")
    @allure.description("""
    This test verifies that a user can successfully move a task from one column to another on the Board, ensuring the task's position is updated correctly and persists after a page refresh.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("TC30: Successful task moving on Board.")
    def test_task_moving_on_board(self, login, create_task_board, delete_project):
        project_name, first_section, second_section, third_section = create_task_board
        fake = FakeDataGenerator()
        task_name = fake.task_name
        # Steps:
        try:
            self.projects_page.create_task_in_section(first_section, task_name)
            self.projects_page.click_more_actions_button_on_task(task_name)
            self.projects_page.move_task_to_section(second_section, project_name)
            self.projects_page.is_section_contains_task(task_name, second_section)
            self.projects_page.click_more_actions_button_on_task(task_name)
            self.projects_page.move_task_to_section(third_section, project_name)
            self.projects_page.is_section_contains_task(task_name, third_section)
        # Postconditions:
        finally:
            with allure.step("Postconditions: Delete the created project."):
                delete_project(project_name)
