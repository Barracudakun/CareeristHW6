from behave import *
from selenium.webdriver.common.by import By
from selenium import webdriver

TOP_LINKS = (By.CSS_SELECTOR, '#CardInstanceYzdhPioi5BhAZTPsnJCcHw a')
HEADER = (By.CSS_SELECTOR, '#zg_banner_text')

@given('Open Amazon bestseller page')
def open_amazon_bestseller_page(context):
    context.driver = webdriver.Chrome('/Users/seashore/Dropbox/My Mac (MacBook-Air.lan)/Downloads/chromedriver')
    context.driver.maximize_window()
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers_8a080d3d7b55497ea1bdd97b7cff8b7b')
    context.driver.implicitly_wait(10)


# @then('Verify there are {expected_links} links')
# def verify_links_count(context, expected_links):
#     actual_links = context.driver.find.elements(*TOP_LINKS)
#     assert len(actual_links) == int(expected_links), f'Expected {expected_links}, but got{len(actual_links)}'

@then('Verify User can click through top links and verify correct page opens')
def click_through_top(context):
    top_links = context.driver.find.elements(*TOP_LINKS)

    for x in range(len(top_links)):
        link = context.driver.find.elements(*TOP_LINKS)[x]

        link_text = link.text
        link.click()

        header_text = context.driver.find_element(*HEADER).text
        assert link_text in header_text, f'Expected{link_text} not in {header_text}'

