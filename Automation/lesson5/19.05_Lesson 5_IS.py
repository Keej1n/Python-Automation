# import section
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# variables section

url = 'https://courses.letskodeit.com/practice'

file = "alert_text.txt"
opened_files = []

mail = 'masdafs@msgagm.mgasga'
password = '12345'

alert_button_css = (By.CSS_SELECTOR, '[value="Alert"]')

mouse_hover_id = (By.ID, 'mousehover')
mouse_hover_top_button = (By.CSS_SELECTOR, ".mouse-hover-content")

footer_css = (By.CSS_SELECTOR, '.jqCopyRight')

sign_in_button_xpath = (By.XPATH, '//a[contains(text(),"Sign In")]')

mail_css = (By.CSS_SELECTOR, "[name='email']")
password_css = (By.CSS_SELECTOR, '[name="password"]')
log_in_css = (By.CSS_SELECTOR, '[value="Login"]')
log_in_alert_xpath = (By.XPATH, "//span[@class='dynamic-text help-block']")

# function section


def write_in_file(log_file, text):
    global opened_files
    if log_file not in opened_files:
        log_file = open(file, "w")
        opened_files.append(log_file)
    log_file.write(text + '\n')


def close_all_opened_files():
    global opened_files
    for _ in opened_files:
        _.close()


def get_text_from_popup(driver):
    popup_window = driver.switch_to.alert
    popup_text = popup_window.text
    popup_window.accept()
    return popup_text


def get_text_from_element(driver, elem):
    element = driver.find_element(*elem)
    return element.text


def found_and_click(driver, elem):
    item = driver.find_element(*elem)
    item.click()


def input_text_into_field(driver, text, elem):
    input_field = driver.find_element(*elem)
    input_field.send_keys(text)


def webdriver_commands_test():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(3)
    driver.get(url)
    found_and_click(driver, alert_button_css)
    write_in_file(log_file, get_text_from_popup(driver))
    found_and_click(driver, mouse_hover_id)
    found_and_click(driver, mouse_hover_top_button)
    write_in_file(log_file, get_text_from_element(driver, footer_css))
    found_and_click(driver, sign_in_button_xpath)
    input_text_into_field(driver, mail, mail_css)
    input_text_into_field(driver, password, password_css)
    found_and_click(driver, log_in_css)
    write_in_file(log_file, get_text_from_element(driver, log_in_alert_xpath))
    close_all_opened_files()
    driver.close()


# main section


if __name__ == '__main__':
    webdriver_commands_test()
