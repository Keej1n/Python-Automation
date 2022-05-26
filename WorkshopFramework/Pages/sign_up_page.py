from selenium.webdriver.common.by import By
from Lib import BrowserManager


class SignUpPage:
    url = 'https://courses.letskodeit.com/register'
    first_name_field = By.XPATH, "//input[@id='name']"
    last_name_field = By.XPATH, "//input[@id='last_name']"
    email_field = By.XPATH, "//input[@id='email']"
    password_field = By.XPATH, "//input[@id='password']"
    password_confirmation = By.XPATH, "//input[@id='password_confirmation']"
    submit_btn = By.XPATH, "//input[@type='submit']"
    dropdown = By.ID, "dropdownMenu1"
    log_out = By.XPATH, '//a[contains(text(), "Logout")]'

    def __init__(self, browser):
        self.browser = browser

    def sign_up(self, first_name, last_name, email, password):
        BrowserManager.check_url(self.browser, self.url)
        BrowserManager.found_input_and_fill(self.browser, self.first_name_field, first_name)
        BrowserManager.found_input_and_fill(self.browser, self.last_name_field, last_name)
        BrowserManager.found_input_and_fill(self.browser, self.email_field, email)
        BrowserManager.found_input_and_fill(self.browser, self.password_field, password)
        BrowserManager.found_input_and_fill(self.browser, self.password_confirmation, password)
        BrowserManager.found_and_click(self.browser, self.submit_btn)
        BrowserManager.found_and_click(self.browser, self.dropdown)
        BrowserManager.found_and_click(self.browser, self.log_out)


