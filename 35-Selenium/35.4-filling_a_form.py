from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get("https://secure-retreat-92358.herokuapp.com")

first_name = driver.find_element(By.NAME, "fName")
last_name = driver.find_element(By.NAME, "lName")
email = driver.find_element(By.NAME, "email")
sign_up = driver.find_element(By.CSS_SELECTOR, ".btn")

first_name.send_keys("David")
last_name.send_keys("Quinteros")
email.send_keys("test@gmail.com")
sign_up.click()
