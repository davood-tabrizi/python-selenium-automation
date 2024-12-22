from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from time import sleep

class MainPage(BasePage):


 def open_main(self):
     self.open_url("https://www.target.com/")
     sleep(5)
