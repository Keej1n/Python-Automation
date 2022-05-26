from selenium.webdriver.common.by import By
from Lib import BrowserManager


class SignInPage:
    url = 'https://courses.letskodeit.com/login'
    register_loc = By.XPATH, "//a[@href='/register']"
    email_loc = By.ID, "email"
    password_loc = By.ID, "password"
    button_loc = By.XPATH, "//input[@type='submit']"

    def __init__(self, browser):
        self.browser = browser

    def go_to_sign_up(self):
        BrowserManager.check_url(self.browser, self.url)
        BrowserManager.found_and_click(self.browser, self.register_loc)

    def sign_in(self, email, password):
        BrowserManager.check_url(self.browser, self.url)
        BrowserManager.found_input_and_fill(self.browser, self.email_loc, email)
        BrowserManager.found_input_and_fill(self.browser, self.password_loc, password)
        BrowserManager.found_and_click(self.browser, self.button_loc)
