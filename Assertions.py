import unittest

from selenium import webdriver

class testing(unittest.TestCase):

    def testlist(self):
        list={"Java","Python","Selenium"}
        self.assertIn("Python",list)
        print("Yes Pass")
        self.assertNotIn("ruby",list)
        print("Yes Pass as well")
        self.assertGreater(100,10)
        print("Yes Greater")
        self.assertGreaterEqual(100,100)
        print("Yes equal")
        self.assertLess(10,100)
        print("Yes lesser")
        self.assertLessEqual(10,10)
        print("Yes equal again")

    def testName(self):
        driver=webdriver.Firefox(executable_path="E:\Software\WebDrivers\geckodriver.exe")
        driver.get("https://www.google.com/")
        pagetittle=driver.title

        self.assertEqual("Google",pagetittle)
        print("Title are same")

        self.assertNotEqual(pagetittle,"Googlet")
        print("Title are different")

        self.assertTrue(pagetittle=="Google")
        print("Yes True")

        self.assertFalse(pagetittle=="NotGoogle")
        print("Yes Not True")

        driver=None
        self.assertIsNone(driver)
        print("It is null")

        driver=webdriver.Firefox(executable_path="E:\Software\WebDrivers\geckodriver.exe")
        self.assertIsNotNone(driver)
        print("Yes it not empty")

if __name__=="__main__":
        unittest.main()
