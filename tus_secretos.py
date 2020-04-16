import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class tusecretoBot:
    def __init__(self, age, post_text):
        self.driver = webdriver.Chrome('./chromedriver.exe')
        self.base_url = 'https://tusecreto.io/'

    def _nav(self, url):
        self.driver.get(url)
        time.sleep(3)

    def post(self, age, post_text):
        self._nav(self.base_url)
        self.driver.find_element_by_xpath("//*[contains(text(), 'Escribir')]").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("""//*[@id="post_submit_form"]/div[1]/div/input""").send_keys(age)
        self.driver.find_element_by_xpath("""//*[@id="post_submit_form"]/div[1]/div/select/option[2]""").click()
        self.driver.find_element_by_xpath("""//*[@id="post_submit_form"]/textarea""").send_keys(post_text)
        self.driver.find_element_by_xpath("//*[contains(text(), ' Enviar')]").click()
