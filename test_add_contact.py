# -*- coding: utf-8 -*-
#from selenium import webdriver

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from contact import Contact
from application2 import Application2

class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.app = Application2()

    
    def test_add_contact(self):
        self.app.open_home_page()
        self.app.login(user="admin", password="secret")
        self.app.add_contact(Contact(firstname="dsf", dlename="gdfg", lastname="ew", nickname="gdf", title="wer", company="dg",
                         address="dg", home="dg", mobile="43", work="sdg", fax="213", email="243", email2="234",
                         email3="245", homepage="fsdf", address2="dsf", phone2="sg", notes="sfghh"))
        self.app.return_home_page()
        self.app.logout()


    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    


    def tearDown(self):
        self.app.destroy()


if __name__ == "__main__":
    unittest.main()
