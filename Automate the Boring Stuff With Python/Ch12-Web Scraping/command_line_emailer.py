# Vasallius

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
browser = webdriver.Firefox()
browser.get(
    'https://accounts.google.com/signin/v2/challenge/pwd?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=AddSession&cid=1&navigationDirection=forward&TL=AM3QAYYEkyzQ7AJkk0oHERU0GR_qY6l_h0MfbwkR-Q7J-PcPNdpcZq5uQucTitPb')
print("Logging in.")
userElem = browser.find_element_by_id('identifierId')
userElem.send_keys(email)
userElem.send_keys(Keys.ENTER)
time.sleep(3)
passwordElem = browser.find_element_by_css_selector(
    "input[class='whsOnd zHQkBf']")
passwordElem.send_keys(password)
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
