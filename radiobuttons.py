from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

chrome_options = Options()

chrome_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://omayo.blogspot.com/")
driver.maxmize_window()

driver.find_element(By.XPATH,'//*[@id="radio1"]').click()






driver.maximize_window()

