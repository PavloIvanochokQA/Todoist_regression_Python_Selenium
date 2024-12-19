# Todoist Regression Testing Checklist
## 1. Registration and Authorization: 
*   [TC01](/docs/test_cases/TC01.md): Successful registration of a new account with valid information.
*	[TC02](/docs/test_cases/TC02.md): Successful login to an existing account with valid information.
*	[TC03](/docs/test_cases/TC03.md): Successful logout from an account.
*   [TC04](/docs/test_cases/TC04.md): Ability to login using a Google account.
*	[TC05](/docs/test_cases/TC05.md): Successful password change.
*   [TC06](/docs/test_cases/TC06.md): Successful  email and username change.
*	[TC07](/docs/test_cases/TC07.md): Successful account deletion.
*	[TC08](/docs/test_cases/TC08.md): Unsuccessful registration of a new account with invalid information.
*	[TC09](/docs/test_cases/TC09.md): Unsuccessful login to an existing account with invalid information.
*	[TC10](/docs/test_cases/TC10.md): Inability to change the current password with an incorrect password.
*	[TC11](/docs/test_cases/TC11.md): Inability to delete the account with an incorrect email or password.

## 2. Task Creation and Editing:
* [TC12](/docs/test_cases/TC12.md): Successful task creation.
* [TC13](/docs/test_cases/TC13.md): Successful change of name, description, and priority for a task.
* [TC14](/docs/test_cases/TC14.md): Successful addition of a sub-task.
* [TC15](/docs/test_cases/TC15.md): Successful change of task due date and time.
* [TC16](/docs/test_cases/TC16.md): Successful task completion and marking as completed.
* [TC17](/docs/test_cases/TC17.md): Successful task deletion.
* [TC18](/docs/test_cases/TC18.md): Successful task creation with a link.
* [TC19](/docs/test_cases/TC19.md): Successful addition of a comment to a task.
* [TC20](/docs/test_cases/TC20.md): Successful addition of a label to a task.
* [TC21](/docs/test_cases/TC21.md): Successful task duplication.
* [TC22](/docs/test_cases/TC22.md): Unsuccessful task creation with invalid information.

## 3. Task Lists and Boards:
* [TC23](/docs/test_cases/TC23.md): Successful creation of a new Task List.
* [TC24](/docs/test_cases/TC24.md): Successful creation of a new Task Board with sections.
* [TC25](/docs/test_cases/TC25.md): Successful change of the Project name and type.
* [TC26](/docs/test_cases/TC26.md): Successful deletion of a Project.
* [TC27](/docs/test_cases/TC27.md): Unsuccessful creation of a new Project due to invalid information.
* [TC28](/docs/test_cases/TC28.md): Successful duplication of a Task List.
* [TC29](/docs/test_cases/TC29.md): Successful archiving of a Project.
* [TC30](/docs/test_cases/TC30.md): Successful task moving on Board.

## 4. Search and Filtering:
* [TC31](/docs/test_cases/TC31.md): Successful search for a task by its name.
* [TC32](/docs/test_cases/TC32.md): Successful search for a task by its description.
* [TC33](/docs/test_cases/TC33.md): Successful filtering for a task by its priority.
* [TC34](/docs/test_cases/TC34.md): Successful filtering for a task by its label.
* [TC35](/docs/test_cases/TC35.md): Successful filtering for a task by its due date.
* [TC36](/docs/test_cases/TC36.md): Successful search for a task that contains a link.
* [TC37](/docs/test_cases/TC37.md): Successful search for a task with a specific comment.
* [TC38](/docs/test_cases/TC38.md): Successful search for a sub-task by its name.
* [TC39](/docs/test_cases/TC39.md): Unsuccessful search for a task with non-existent information.