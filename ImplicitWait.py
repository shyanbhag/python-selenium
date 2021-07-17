from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

cap = DesiredCapabilities().FIREFOX

cap["marionette"] = False

driver=webdriver.Firefox(capabilities=cap, executable_path="E:\Software\WebDrivers\geckodriver")

driver.get("http://newtours.demoaut.com/")

driver.implicitly_wait(3)

UserName=driver.find_element_by_name("userName")

print(UserName.is_displayed()) #Returns boolean value
print(UserName.is_displayed()) #Returns boolean value

driver.close()