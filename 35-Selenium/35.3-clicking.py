from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get("https://es.wikipedia.org/wiki/Wikipedia:Portada")

search = driver.find_element(By.NAME, "search")
search.send_keys("Python", Keys.ENTER)

