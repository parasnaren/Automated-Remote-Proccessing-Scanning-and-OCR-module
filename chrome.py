from selenium import webdriver
import os


chrome_path = "⁩/Users⁩/anirudhrv⁩/⁨Desktop⁩/chromedriver"
driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver"))


def fb_login():
    driver.get ("https://www.facebook.com")
    driver.find_element_by_id("email").send_keys('fakeemail@crossbrowsertesting.com')
    driver.find_element_by_id("pass").send_keys('fakepassword1')
    driver.find_element_by_id("loginbutton").click()


fb_login()
