# -*- coding: utf-8 -*-
import time
from selenium import webdriver

profile = webdriver.FirefoxProfile()
profile.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0")
profile.add_argument("window-size=500,800")

path = "E:\\Programmes\\Python\\browsersdrivers\\geckodriver.exe"

driver = webdriver.Firefox(firefox_profile=profile,executable_path=path)

driver.get("http://nqo15.minitroopers.fr")
driver.find_element_by_id("name").send_keys('fehicuhcsd53')
driver.find_element_by_id("tr_1000").click()
time.sleep(3)
driver.find_element_by_id("submit").click()
