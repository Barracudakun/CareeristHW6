from telnetlib import EC

from behave import *
from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By


@given('Open Amazon T&C page')
def open_Amazon_TC_page(context):
    context.driver = webdriver.Chrome('/Users/seashore/Dropbox/My Mac (MacBook-Air.lan)/Downloads/chromedriver')
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/'
                       'ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')

@when('Store original windows')
def store_original_window(context):
    original_window = context.driver.current_window_handle
    return original_window

@when('Click on Amazon Privacy Notice link')
def click_on_amazon_privacy_notice_link(context):
    context.driver.find_element(By.XPATH, "//a[contains(@href,'amazon.com/privacy')]").click()


@when(u'Switch to the newly opened window')
def switch_to_opened_window(context):
    new_window = context.driver.window_handles[1]
    context.driver.switch_to.window(new_window)
    context.driver.wait.until(EC.new_window_is_opened)

@then('Verify Amazon Privacy Notice page is opened')
def verify_privacy_notice_page_is_opened(context):
    actual_page = context.driver.find_element(By.XPATH, "//div[@class='help-content']/h1").text
    assert actual_page == 'Amazon.com Privacy Notice', f'got {actual_page}'
    sleep(3)

@then('User can close new window and switch back to original')
def close_new_window_and_switch_back_original(context):
    context.driver.quit()
    context.driver.switch_to_window(original_window)  #why 'original_window' cannot be executed