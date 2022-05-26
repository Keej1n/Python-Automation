# import section
from Pages.practice_page import PracticePage
from Pages.sign_in_page import SignInPage
from Pages.sign_up_page import SignUpPage
from Pages.course_page import CoursePage
from Lib import BrowserManager

import test_data


# main section

if __name__ == '__main__':
    browser = BrowserManager.browser()

    # Step One
    practice_page = PracticePage(browser)
    practice_page.go_to_sign_in()

    # Step Two
    sign_in_page = SignInPage(browser)
    sign_in_page.go_to_sign_up()

    # Step Three
    sign_up_page = SignUpPage(browser)
    sign_up_page.sign_up(test_data.first_name, test_data.last_name, test_data.email, test_data.password)

    # Step Four
    sign_in_page.sign_in(test_data.email, test_data.password)

    # Step Five
    course_page = CoursePage(browser)
    course_page.search_and_count(test_data.search_word)
    BrowserManager.close_browser(browser)
