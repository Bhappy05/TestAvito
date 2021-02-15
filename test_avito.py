from selenium import webdriver
import pytest

@pytest.fixture
def browser():
     browser = webdriver.Chrome()
     browser.implicitly_wait(15)
     yield browser 
     browser.quit()


class TestAvito(): 
    def test_phone_is_empty(self, browser):
        browser.get("https://www.avito.ru/sochi/lichnye_veschi?cd=1&d=1")
        authentification = browser.find_element_by_class_name("header-services-menu-link-not-authenticated-3kAga").click()
        login = browser.find_element_by_name("login").send_keys("kovalev15_93@mail.ru")
        password = browser.find_element_by_name("password").send_keys("Ragnarok1336")
        submit = browser.find_element_by_name("submit").click()
        item = browser.find_element_by_css_selector("h3.title-root-395AQ").click()
        new_window = browser.window_handles[1]
        browser.switch_to.window(new_window)
        buybutton = browser.find_element_by_class_name("item-buyer-button-1-zak").click()
        phone = browser.find_element_by_name("phone").text
        assert phone == "", "Phone is not empty"


if __name__ == "__main__":
    pytest.main()

    
