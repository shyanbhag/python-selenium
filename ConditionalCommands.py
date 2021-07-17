from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

cap = DesiredCapabilities().FIREFOX

cap["marionette"] = False

driver=webdriver.Firefox(capabilities=cap, executable_path="E:\Software\WebDrivers\geckodriver")

driver.get("http://newtours.demoaut.com/")

UserName=driver.find_element_by_name("userName")

print(UserName.is_displayed()) #Returns boolean value
print(UserName.is_displayed()) #Returns boolean value

Password=driver.find_element_by_name("password")

UserName.send_keys("mercury")
Password.send_keys("mercury")

driver.find_element_by_name("login").click()

round_trip=driver.find_element_by_css_selector("input[value=roundtrip]")
print("Status of round trip: ",round_trip.is_selected()) #Returns booolean value

oneway=driver.find_element_by_css_selector("input[value=oneway]")
print("Status of Oneway trip: ",oneway.is_selected()) #Returns booolean value

driver.close()



