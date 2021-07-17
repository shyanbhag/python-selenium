from selenium import webdriver

driver=webdriver.Firefox(executable_path="E:\Software\WebDrivers\geckodriver.exe")

driver.get("https://www.google.com/")

driver.save_screenshot("E:\Software\Pyhton-Sel\screenshots\home.jpg")

#driver.get_screenshot_as_file("E:\Software\Pyhton-Sel\screenshots\home2.png")

driver.close()