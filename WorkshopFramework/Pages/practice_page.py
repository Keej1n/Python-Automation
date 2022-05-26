from selenium.webdriver.common.by import By

from Lib import BrowserManager


class PracticePage:
    url = 'https://courses.letskodeit.com/practice'
    sign_in_button_loc = By.XPATH, "//a[@href='/login']"

    def __init__(self, browser):
        self.browser = browser

    def go_to_sign_in(self):
        BrowserManager.load(self.browser, self.url)
        BrowserManager.found_and_click(self.browser, self.sign_in_button_loc)
