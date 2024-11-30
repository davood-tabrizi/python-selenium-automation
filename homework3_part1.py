from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

#amazon logo
driver.find_element(By.CSS_SELECTOR, ".a-icon-logo")
#create account header
driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small")
#name field
driver.find_element(By.ID, "ap_customer_name")
#mobile number or email field
driver.find_element(By.ID, "ap_email")
#password field
driver.find_element(By.ID, "ap_password")
#password alert
driver.find_element(By.XPATH, "//div[contains(text(), 'Enter a password')]")
#re-enter password field
driver.find_element(By.ID, "ap_password_check")
#continue field(for create account)
driver.find_element(By.ID, "continue")
#conditions of use link
driver.find_element(By.CSS_SELECTOR, 'a[href*="notification_condition_of_use?ie=UTF8&nodeId=508088"]')
#privacy notice field
driver.find_element(By.CSS_SELECTOR, 'a[href*="notification_privacy_notice?ie=UTF8&nodeId=468496"]')
#sign in link
driver.find_element(By.CSS_SELECTOR, 'a.a-link-emphasis')