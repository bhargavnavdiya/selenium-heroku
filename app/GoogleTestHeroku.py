# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeServiceManager

# # driver = webdriver.Chrome(executable_path=r"C:\Windows\chromedriver.exe")
# driver = webdriver.chrome(service = Service(ChromeDriverManager().install()))
# driver.get("https://www.google.com")

# driver.implicitly_wait(10)

# driver.maximize_window()

# driver.get("https://google.com")

# driver.find_element_by_name("q").send_keys("Automation Step by step")

# driver.find_element_by_name("btnK").click()

# driver.close()

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest 
import HtmlTestRunner

class GoogleSearhUnitTest(unittest.TestCase):
    @classmethod
    # def setUpClass(cls): 
    def setUpClass(cls):
        cls.driver = webdriver.ChromeOptions()  # Optional argument, if not specified will search path.
        # cls.driver.maximize_window()

        time.sleep(3)# Let the user actually see something!
    
    def test_search_seleniumTestingSearch(self):
        # element = driver.find_element_by_class_name("M6CB1c rr4y5c")
        # element.click()
        self.driver.get('http://www.google.com/');
        search_box = self.driver.find_element(By.NAME, "q")

        search_box.send_keys('Selenium Unit Testing')

        time.sleep(3)

        self.driver.find_element(By.NAME, "btnK").click()

        time.sleep(3) # Let the user actually see something!

    def test_search_UnitTestSoftwareTesting(self):
    
        self.driver.get('http://www.google.com/');
        search_box = self.driver.find_element(By.NAME, "q")

        search_box.send_keys('Software Hacking Tutorials')

        time.sleep(3)

        self.driver.find_element(By.NAME, "btnK").click()

        time.sleep(3) # Let the user actually see something!
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed!")

if __name__ == "__main__":
    print(unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/Om Namah Shivay/Downloads/542 presentation")))
    


