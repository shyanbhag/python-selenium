from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

cap = DesiredCapabilities().FIREFOX

cap["marionette"] = False

driver=webdriver.Firefox(capabilities=cap, executable_path="E:\Software\WebDrivers\geckodriver")

driver.get("https://www.google.com/")

print(driver.title)

facebook=driver.get("https://www.facebook.com/")

print(driver.title)

driver.back() #Backward Navigation

print(driver.title)

driver.forward() #Forward Navigation

print(driver.title)

driver.close()
