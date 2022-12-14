# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTest1():
  def setup_method(self, method):
    self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_test1(self):
    self.driver.get("https://www.asocietygroup.com/")
    self.driver.set_window_size(1920, 1032)
    self.driver.find_element(By.CSS_SELECTOR, ".cntr-logo-link").click()
    self.driver.find_element(By.LINK_TEXT, "Consultant").click()
    self.driver.find_element(By.LINK_TEXT, "Customer").click()
    self.driver.find_element(By.LINK_TEXT, "News & Events").click()
    self.driver.find_element(By.LINK_TEXT, "About us").click()
    self.driver.find_element(By.LINK_TEXT, "Contact").click()
    self.driver.find_element(By.LINK_TEXT, "Assignments").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ls-button").click()
    self.driver.find_element(By.CSS_SELECTOR, "#hs_cos_wrapper_module_1538553245903532_ > #hs-cta-wrapper-efb8af24-d09c-4d42-9dee-4cb32ba4840b > #hs-cta-efb8af24-d09c-4d42-9dee-4cb32ba4840b span").click()
    self.driver.find_element(By.NAME, "company").click()
    self.driver.find_element(By.NAME, "company").send_keys("QA at Silicon Valley California")
    self.driver.find_element(By.NAME, "name").send_keys("Tetiana Koziychuk")
    self.driver.find_element(By.NAME, "address").send_keys("1825 Bridgetown pike apt 213, 213")
    self.driver.find_element(By.NAME, "postcode").send_keys("19053")
    self.driver.find_element(By.NAME, "city").send_keys("Feasterville Trevose")
    self.driver.find_element(By.NAME, "country").send_keys("United States")
    self.driver.find_element(By.NAME, "phone").send_keys("2157794239")
    self.driver.find_element(By.NAME, "email").click()
    self.driver.find_element(By.NAME, "email").send_keys("tetianarybii@gmail.com")
    self.driver.find_element(By.CSS_SELECTOR, ".igm-checkbox > span").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    self.driver.find_element(By.CSS_SELECTOR, ".close").click()
    self.driver.close()
  
