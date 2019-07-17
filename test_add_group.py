# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from group import Group

class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)


    def test_add_group(self):
        self.login(username="admin", password="secret")
        self.create_group(Group(name="fgrt", header="ghty", footer="ghtyrt"))
        self.logout()


    def test_add_empty_group(self):
        self.login(username="admin", password="secret")
        self.create_group(Group(name="", header="", footer=""))
        self.logout()


       # def is_element_present(self, how, what):
    #     try:
    #         self.wd.find_element(by=how, value=what)
    #     except NoSuchElementException as e:
    #         return False
    #     return True
    #
    # def is_alert_present(self):
    #     try:
    #         self.wd.switch_to_alert()
    #     except NoAlertPresentException as e:
    #         return False
    #     return True

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
