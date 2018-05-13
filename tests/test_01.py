import pytest
from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = 'P'
desired_caps['deviceName'] = 'Nexus 5X API P'
desired_caps['app'] = 'app/build/outputs/apk/release/app-release-unsigned.apk'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

def test_click():
  button = driver.find_element_by_id('button')
  button.click()
  textView =  driver.find_element_by_id('textView')
  assert textView.text == "OMG! CLICKED!"
