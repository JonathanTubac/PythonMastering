from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://es.wikipedia.org/wiki/Wikipedia:Portada")

total_es_articles = driver.find_element(By.CSS_SELECTOR, ".main-top-articleCount b a")
total_formatted = total_es_articles.text.replace(" ", ",", 2)
print(f"Wikipedia has {total_formatted} aricles in  spanish")

driver.quit()