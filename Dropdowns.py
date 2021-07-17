from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

cap = DesiredCapabilities().FIREFOX

cap["marionette"] = False

driver=webdriver.Firefox(capabilities=cap, executable_path="E:\Software\WebDrivers\geckodriver")

driver.get("https://www.seleniumeasy.com/test/basic-select-dropdown-demo.html")

#Click Type Drop Downs
element=driver.find_element(By.XPATH,"(//*[@class='caret'])[6]")
element.click()
element=driver.find_element(By.XPATH,"//*[@href='./bootstrap-dual-list-box-demo.html']")
element.click()
driver.back()

#Select Type Drop Downs
element=driver.find_element(By.ID,"select-demo")
dropdown=Select(element)

Value1=dropdown.select_by_visible_text("Sunday") #By Visible Text
Value2=dropdown.select_by_index(7) #By Index
Value3=dropdown.select_by_value("Wednesday") #By Value

#Count No of options
print(len(dropdown.options))

#Capture all available options
all_options=dropdown.options

for options in all_options:
    print(options.text)

driver.close()