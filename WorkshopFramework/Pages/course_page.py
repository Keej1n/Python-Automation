from selenium.webdriver.common.by import By
from Lib import BrowserManager


class CoursePage:
    url = "https://courses.letskodeit.com/courses"
    searchCourses = By.CSS_SELECTOR, ".find-input"
    searchCoursesButton = By.CSS_SELECTOR, ".search-course"
    search_elements = By.CSS_SELECTOR, ".zen-course-list"

    def __init__(self, browser):
        self.browser = browser

    def search_and_count(self, search_word):
        BrowserManager.load(self.browser, self.url)
        BrowserManager.found_input_and_fill(self.browser, self.searchCourses, search_word)
        BrowserManager.found_and_click(self.browser, self.searchCoursesButton)
        BrowserManager.count_elements(self.browser, self.search_elements)



