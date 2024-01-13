from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

chrome_options = Options()

chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://omayo.blogspot.com/")
driver.maximize_window()

chk = driver.find_element(By.ID,'//*[//*[@id="checkbox1""]')
if chk.is_selected():
    chk.click()
else:
    pass
chk2 = driver.find_element(By.ID,'checkbox2')
if chk2.is_selected():
    pass
else:
    chk2.click()