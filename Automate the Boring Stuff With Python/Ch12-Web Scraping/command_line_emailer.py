# Command Line Emailer
# DOESN'T WORK ANYMORE !!!

'''
Description:
Write a program that takes an email address and string of text on the command line 
and then, using selenium, logs in to your email account and
sends an email of the string to the provided address. 
(You might want to set up a separate email account for this program.)
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Initialize variables
print("Greetings user.")
email = input("Please enter email: ")
password = input("Please enter password: ")
recipient_email = input("To whom would you like to send an email? ")
body = input("Please enter message content: ")

# Login Phase
browser = webdriver.Chrome()
gmail = 'https://accounts.google.com/signin/v2/identifier?passive=1209600&continue=https%3A%2F%2Faccounts.google.com%2F&followup=https%3A%2F%2Faccounts.google.com%2F&hl=en-GB&flowName=GlifWebSignIn&flowEntry=ServiceLogin'
browser.get(gmail)
time.sleep(2)
print("Logging in.")
userElem = browser.find_element_by_id('identifierId')
userElem.send_keys(email)
time.sleep(3)
userElem.send_keys(Keys.ENTER)
time.sleep(3)
passwordElem = browser.find_element_by_css_selector(
    "input[class='whsOnd zHQkBf']")
passwordElem.send_keys(password)
time.sleep(3)
passwordElem.send_keys(Keys.ENTER)
time.sleep(5)


# Compose a message
print("Composing message.")
composeElem = browser.find_element_by_css_selector(
    'div.T-I.J-J5-Ji.T-I-KE.L3')
composeElem.click()
time.sleep(5)
toElem = browser.find_element_by_name('to')
toElem.send_keys(recipient_email)
bodyElem = browser.find_element_by_css_selector(
    'div.Am.Al.editable.LW-avf.tS-tW')
bodyElem.send_keys(body)

# Send message
submitElem = browser.find_element_by_css_selector(
    'div.T-I.J-J5-Ji.aoO.v7.T-I-atl.L3')
submitElem.click()
print("Email sent.")

browser.quit()
