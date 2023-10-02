# Import necessary libraries
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import pyautogui

# Define the URL of the webpage you want to interact with
url = 'https://www.gmrtranscription.com/careers-test/typist-test.aspx'

# Define the path to the Firefox driver executable
driver_path = 'thePathWhereTheDriveIsFound/{0}'.format('geckodriver.exe')

# Create a service object for the WebDriver, specifying the driver path
service = Service(executable_path=driver_path)

# Configure options for the Firefox WebDriver
options = webdriver.FirefoxOptions()

# Create a Firefox WebDriver instance using the service and options
browser = webdriver.Firefox(service=service, options=options)

try:
    # Open the website
    browser.get(url)

    # Find the email input element by its ID
    email_input = browser.find_element(By.ID, 'txtemail')

    # Clear any existing text in the email input
    email_input.clear()

    # Type the email address into the input
    email_input.send_keys('example@youremail.com')

    # Find the submit button by its ID
    submit_button = browser.find_element(By.ID, 'btnsubmit')

    # Click the submit button to submit the form
    submit_button.click()

    # Wait for the page to load (you may need to adjust the wait time)
    browser.implicitly_wait(10)  # Adjust the wait time as needed

    # Find the div element with class "words"
    words_div = browser.find_element(By.CLASS_NAME, 'words')

    # Find all the span elements inside the div
    span_elements = words_div.find_elements(By.TAG_NAME, 'span')

    # Find the textarea element by its TAG_NAME
    textarea = browser.find_element(By.TAG_NAME, 'textarea')  # Replace 'yourmessage' with the actual textarea ID

    # Clear any existing text in the textarea
    textarea.clear()

    # Iterate through all the span elements and type their text into the textarea
    for span_element in span_elements:
        span_text = span_element.text
        if span_text:
            textarea.send_keys(span_text)  # Add space between span texts if needed
        else:
            textarea.send_keys(' ')

except Exception as e:
    # Print an error message if an exception occurs
    print(f"An error occurred: {str(e)}")


