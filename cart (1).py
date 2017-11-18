import unittest
import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

class Cart():
  globaldriver = ""

  def __init__(self, driver):
    global globaldriver
    globaldriver = driver
    url = driver.current_url #saves the driver's url to a variable
    if not("https://www-secure.target.com/co-cart" in url): #compare the current url with the desired one
      raise ValueError("Current page is not Cart") #raises the error

  def count_items(self):
    global globaldriver
    driver = globaldriver
    items = driver.find_elements_by_class_name("js-cartQuantitySr") 
    quantity = int(items[0].text.partition(" ")[0])
    return quantity


  def clear_cart(self):
    global globaldriver
    driver = globaldriver
    time.sleep(3)
    if not(self.count_items == 0):
      buttons = driver.find_elements_by_class_name("remove-btn")
      while buttons:
        buttons[0].click()
        driver.find_element_by_class_name("remove-sflitem").click()
        time.sleep(6)
        buttons = driver.find_elements_by_class_name("remove-btn")

  def increment_item(self, item_index):
    global globaldriver
    driver = globaldriver
    time.sleep(1)
    items = driver.find_elements_by_class_name("js-cart-qty-increase")
    item = items[item_index-1]
    item.click() 

  def decrement_item(self, item_index):
    global globaldriver
    driver = globaldriver
    time.sleep(1)
    if (self.count_items() != 1):
      items = driver.find_elements_by_class_name("js-cart-qty-decrease")
      item = items[item_index-1]
      item.click() 
