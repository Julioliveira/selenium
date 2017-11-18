#Julio Oliveira nk6549
import unittest
import time
from cart import Cart #imports my cart python file
from selenium import webdriver
from datetime import datetime
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.by import By

#all times.sleep() are used to wait for the page to load
class TestCart(unittest.TestCase):

  def setup(self):
      Cart(driver).clear_cart() #clear the cart to start new tests

  def add_item(self, itemLink): #function to add an item to the cart using its url
    driver.get(itemLink) 
    time.sleep(1)
    buton = driver.find_element_by_class_name("sbc-add-to-cart") #finds the button to add to cart
    buton.click()
    time.sleep(2)
    go_to_cart = driver.find_element_by_class_name("cart-ATC") #click on the button to navigate to the cart
    time.sleep(2)
    go_to_cart.click()
    time.sleep(2)
    
  def test_raise_error(self): #test to verify if the error is risen if the page wasn't right
    
    with self.assertRaises(ValueError):
      driver.get("http://facebook.com") #wrong page
      Cart(driver)
      driver.get("https://www-secure.target.com/co-cart") #goes back to cart in case this is not the last test executed
      time.sleep(3)

  def test_add_item(self): #add item to the cart and verify if it's right.
    self.setup()
    self.add_item("http://www.target.com/p/mens-silver-tie-bar/-/A-15833430")
    item = driver.find_elements_by_link_text("Men's Silver Tie Bar") #use the anchor text to find the element in the cart
    time.sleep(1)
    self.assertTrue(item) 
    # when looking for the element, a list self.assertTrue(Cart(driver).count_items() == 1)is returned. If the element is not found, the list is empty
    #if list is empty, it is evaluated as false

  def test_increase_and_decrease(self):
    self.setup()
    self.add_item("http://www.target.com/p/mens-silver-tie-bar/-/A-15833430")
    Cart(driver).increment_item(1)
    time.sleep(3)
    self.assertTrue(Cart(driver).count_items() == 2)
    Cart(driver).decrement_item(1)
    time.sleep(3)
    self.assertTrue(Cart(driver).count_items() == 1)

  def test_limit(self):
    self.setup()
    self.add_item("http://www.target.com/p/apple-earpods-with-remote-and-mic-white-md827ll-a-/-/A-14213685")
    Cart(driver).increment_item(1)
    time.sleep(3)
    self.assertTrue(Cart(driver).count_items() == 1)

if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get("https://www-secure.target.com/co-cart")
    unittest.main()
    driver.quit()
