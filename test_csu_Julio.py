import unittest
import time
from selenium import webdriver
from datetime import datetime
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.by import By

class TestCSUEB(unittest.TestCase):

    def test_title(self):
        ''' Check content of title
        '''
        self.assertEquals("California State University, East Bay", driver.title)

    def test_logo(self):
        ''' Check logo element
        '''
        logo = driver.find_element(By.ID, "logo")
        logo.find_element(By.XPATH, './a/img[@src="/files/images/csueb-logo-print.png"]')

class TestFooter(unittest.TestCase):
    
    def test_copyright(self):
        footer = driver.find_element(By.ID, "footer-content") #finds the footer in the page
        copyright = "Copyright " + str(datetime.now().year) #creates a string with copyright + current year
        self.assertTrue(footer.text.find(copyright) > -1) #if the copyright with right year is found, it will return
                                                          #an int greater than -1
    
    def test_address(self):
        footer = driver.find_element(By.ID, "footer-content") #finds the footer in the page
        address = "25800 Carlos Bee Boulevard, Hayward, CA 94542"  #sets the address variable
        self.assertTrue(footer.text.find(address) > -1) #returns an int greater than -1 if the value is found

    def test_phone_number(self):
        footer = driver.find_element(By.ID, "footer-content") #finds the footer in the page
        phone = "510-885-3000" #sets the phone variable
        self.assertTrue(footer.text.find(phone) > -1) #returns an int greater than -1 if the value is found

class TestLinks(unittest.TestCase):

    def test_prospective_student_link(self):
      driver.get("http://www.csueastbay.edu/") #redirects to the page to be test
      ps_link = driver.find_element_by_link_text('Prospective Students') #find the anchor based on the text
      ps_link.click() #navigates to the anchor
      self.assertEquals("Prospective Students Home Page", driver.title)

    def test_current_students_link(self):
      driver.get("http://www.csueastbay.edu/") #redirects to the page to be test
      cs_link = driver.find_element_by_link_text('Current Students') #find the anchor based on the text
      cs_link.click()#navigates to the anchor
      time.sleep(1) #waits 1 time before next instructions
      self.assertEquals("Current Students at Cal State East Bay", driver.title)

    def test_current_alumini_friends_link(self):
      driver.get("http://www.csueastbay.edu/")#redirects to the page to be test
      cs_link = driver.find_element_by_link_text('Alumni & Friends')#find the anchor based on the text
      cs_link.click()#navigates to the anchor
      time.sleep(1)#waits 1 time before next instructions
      self.assertEquals("Alumni Association", driver.title)  

class TestLinksBlackboard(unittest.TestCase):

    def test_blackboard_link(self):
        open_dropdown = driver.find_element(By.ID, "quicklinks") #sets the variable as the element found by the ID
        open_dropdown.click() #clicks on the element. Since it's a drop down list, it expands it
        bb_link = driver.find_element_by_link_text("Blackboard") #finds the link to Blackboard that was in the dropdown list
        bb_link.click() #clicks on the link
        time.sleep(1) #waits 1 time before next instructions 
        self.assertEquals(u'My Blackboard \u2013 Blackboard Learn', driver.title)

class TestSearchBox(unittest.TestCase):

    def test_search_box(self):
        driver.get("http://www.csueastbay.edu/")#redirects to the page to be test
        search_bar = driver.find_element(By.ID, "search-query") #finds the search bar based on the ID
        search_bar.clear() #cleans what's writen in the bar
        search_bar.send_keys("housing") #writes the keys in the search bar
        driver.find_element(By.ID, "button-search-go").click() #clicks on the button found
        time.sleep(1) #waits 1 time before next instructions
        housing = driver.find_element_by_tag_name('div') #finds the first DIV in the website and serts the variable as it
        housing = housing.find_element_by_tag_name('a') #sets the variable as the first anchor found in it
        self.assertEquals(housing.text, "Housing")

class TestSlideShow(unittest.TestCase):

    def test_slideshow_div(self):
        driver.get("http://www.csueastbay.edu/")#redirects to the page to be test
        slide_show = driver.find_element(By.ID,'slideShow') #sets the variable as the element with ID equals to "slideShow"
        for div in slide_show.find_elements_by_tag_name("div"): #for to go throuw the list of DIVs in the slide show
            img = div.find_element_by_tag_name("img") #sets the variable as the first IMG element in the DIV
            self.assertTrue(img.get_attribute("src").find('.jpg') > -1)#returns an int greater than -1 if the value is found

if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get("http://www.csueastbay.edu/")
    unittest.main()
    driver.quit()
