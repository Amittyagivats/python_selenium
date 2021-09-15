import os
import pytest
from selenium import webdriver
import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep


def test1():
    baseUrl = "https://letskodeit.teachable.com/pages/practice"
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(baseUrl)

    driver.find_element(By.ID, "name").send_keys("Anil")
    driver.find_element(By.ID, "alertbtn").click()
    time.sleep(2)
    alert1 = driver.switch_to.alert
    alert1.accept()
    time.sleep(2)
    driver.find_element(By.ID, "name").send_keys("Anil")
    driver.find_element(By.ID, "confirmbtn").click()
    time.sleep(2)
    alert2 = driver.switch_to.alert
    alert2.dismiss()
test1()


