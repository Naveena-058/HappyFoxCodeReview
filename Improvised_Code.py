from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import os
import time

class Testcase101:
    """
    Testcase101 class for automating the login, status creation, priority creation,
    and deletion operations on a web application.
    """

    def __init__(self):
        """
        Initialize the Testcase101 class with a Firefox WebDriver.
        """
        self.driver = webdriver.Firefox(executable_path=os.getenv('GECKODRIVER_PATH'))

    def login(self, username, password):
        """
        Log in to the web application with the provided username and password.
        
        :param username: Username for login
        :param password: Password for login
        """
        self.driver.get("https://interview.supporthive.com/staff/")
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.find_element(By.ID, "id_username").send_keys(username)
        self.driver.find_element(By.ID, "id_password").send_keys(password)
        self.driver.find_element(By.ID, "btn-submit").click()

    def create_status(self):
        """
        Create a new status in the web application.
        """
        action = ActionChains(self.driver)
        tickets = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "ember29")))
        action.move_to_element(tickets).perform()
        statuses = self.driver.find_element(By.LINK_TEXT, "Statuses")
        statuses.click()
        self.driver.find_element(By.XPATH, "/html/body/div[3]/div/section/section/div/header/button").click()
        self.driver.find_element(By.TAG_NAME, "input").send_keys("Issue Created")
        statusColourSelect = self.driver.find_element(By.XPATH, "//div[@class='sp-replacer sp-light']")
        statusColourSelect.click()
        statusColourEnter = self.driver.find_element(By.XPATH, "//input[@class='sp-input']")
        statusColourEnter.clear()
        statusColourEnter.send_keys("#47963f")
        ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
        firstElement = self.driver.find_element(By.XPATH, "//a[@id='first-link']")
        firstElement.click()
        secondElement = self.driver.find_element(By.XPATH, "//a[@id='second-link']")
        secondElement.click()
        self.driver.find_element(By.TAG_NAME, "textarea").send_keys("Status when a new ticket is created in HappyFox")
        addCreate = self.driver.find_element(By.XPATH, "//button[@class ='hf-entity-footer_primary hf-primary-action ember-view']")
        addCreate.click()
        time.sleep(3)
        moveTo = self.driver.find_element(By.XPATH, "//td[@class ='lt-cell align-center hf-mod-no-padding ember-view']")
        action.move_to_element(moveTo).perform()
        moveTo.click()
        time.sleep(9)
        issue = self.driver.find_element(By.XPATH, "//div[contains(text(),'Issue Created')]")
        action.move_to_element(issue).perform()
        make = self.driver.find_element(By.LINK_TEXT, "Make Default")
        make.click()

    def create_priority(self):
        """
        Create a new priority in the web application.
        """
        self.driver.find_element(By.LINK_TEXT, "Priorities").click()
        self.driver.find_element(By.XPATH, "//header/button[1]").click()
        self.driver.find_element(By.TAG_NAME, "input").send_keys("Assistance required")
        self.driver.find_element(By.TAG_NAME, "textarea").send_keys("Priority of the newly created tickets")
        button = self.driver.find_element(By.CSS_SELECTOR, "button[data-test-id='add-priority']")
        button.click()
        time.sleep(9)

    def delete_priority(self):
        """
        Delete a priority in the web application.
        """
        action = ActionChains(self.driver)
        tickets2 = self.driver.find_element(By.ID, "ember29")
        action.move_to_element(tickets2).perform()
        priorities2 = self.driver.find_element(By.LINK_TEXT, "Priorities")
        priorities2.click()
        self.driver.implicitly_wait(20)
        self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[3]/div[1]/section[1]/section[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[9]/td[2]").click()
        self.driver.find_element(By.LINK_TEXT, "Delete").click()
        delete = self.driver.find_element(By.CSS_SELECTOR, "button[data-test-id='delete-dependants-primary-action']")
        delete.click()
        time.sleep(9)

    def logout(self):
        """
        Log out from the web application.
        """
        self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[3]/div[1]/header[1]/div[2]/nav[1]/div[7]/div[1]/div[1]").click()
        self.driver.find_element(By.LINK_TEXT, "Logout").click()

    def run_test(self):
        """
        Run the entire test case: login, create status, create priority, delete priority, and logout.
        """
        self.login("Agent", "Agent@123")
        self.create_status()
        self.create_priority()
        self.delete_priority()
        self.logout()
        self.driver.quit()

if __name__ == "__main__":
    test = Testcase101()
    test.run_test()

class PagesforAutomationAssignment:
    """
    PagesforAutomationAssignment class for automating basic login and homepage verification
    on a web application.
    """

    def __init__(self):
        """
        Initialize the PagesforAutomationAssignment class with a Chrome WebDriver.
        """
        self.driver = webdriver.Chrome()

    def run_test(self):
        """
        Run the test case: open the website, perform login, verify the homepage, and quit the driver.
        """
        self.driver.get("https://www.happyfox.com")
        loginPage = LoginPage(self.driver)
        loginPage.login("username", "password")
        homePage = HomePage(self.driver)
        homePage.verifyHomePage()
        self.driver.quit()

if __name__ == "__main__":
    test = PagesforAutomationAssignment()
    test.run_test()

class BasePage:
    """
    BasePage class that serves as the base for all page classes, providing common methods and properties.
    """

    def __init__(self, driver):
        """
        Initialize the BasePage class with a WebDriver instance.

        :param driver: WebDriver instance
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

class LoginPage(BasePage):
    """
    LoginPage class for automating the login functionality.
    """

    def login(self, username, password):
        """
        Perform the login operation with the provided username and password.

        :param username: Username for login
        :param password: Password for login
        """
        self.driver.find_element(By.ID, "username").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "loginButton").click()

    def forgotPassword(self):
        """
        Click the 'Forgot password?' link.
        """
        self.driver.find_element(By.LINK_TEXT, "Forgot password?").click()

class HomePage(BasePage):
    """
    HomePage class for verifying and navigating the home page.
    """

    def verifyHomePage(self):
        """
        Verify that the current URL is the home page URL.
        """
        assert self.driver.current_url == "https://www.happyfox.com/home", "Not on the home page"

    def navigateToProfile(self):
        """
        Navigate to the profile page by clicking the profile link.
        """
        self.driver.find_element(By.ID, "profileLink").click()

class TablePage(BasePage):
    """
    TablePage class for retrieving text from rows of a table.
    """

    def __init__(self, driver):
        """
        Initialize the TablePage class with a WebDriver instance.

        :param driver: WebDriver instance
        """
        super().__init__(driver)
        self.rowLocator = By.XPATH("//table[@id='dataTable']/tbody/tr")

    def retrieveRowTexts(self):
        """
        Retrieve and print the text from each row in the table.

        :return: List of row texts
        """
        rows = self.driver.find_elements(self.rowLocator)
        row_texts = [row.text for row in rows]
        for i, row_text in enumerate(row_texts):
            print(f"Row {i} Text: {row_text}")
        return row_texts
