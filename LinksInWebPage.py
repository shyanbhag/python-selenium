from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

cap = DesiredCapabilities().FIREFOX

cap["marionette"] = False

driver=webdriver.Firefox(capabilities=cap, executable_path="E:\Software\WebDrivers\geckodriver")

driver.get("http://newtours.demoaut.com/")

links= driver.find_elements(By.TAG_NAME,"a")

print(len(links))

for link in links:
    print(link.text)

driver.close()


