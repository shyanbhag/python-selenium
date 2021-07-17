from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

cap = DesiredCapabilities().FIREFOX

cap["marionette"] = False

driver=webdriver.Firefox(capabilities=cap, executable_path="E:\Software\WebDrivers\geckodriver")

#driver=webdriver.Ie(executable_path="E:\Software\WebDrivers\IEDriverServer")

driver.get("https://www.google.com/")

print(driver.title)

print(driver.current_url)

#print(driver.page_source)

driver.close()


