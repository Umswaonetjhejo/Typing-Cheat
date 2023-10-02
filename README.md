<!DOCTYPE html>
<html>
<head>
    
</head>
<body>
    <h1>Typing Test Automation</h1>
    <p>This program automates a typing test for you from <a href="https://www.gmrtranscription.com">www.gmrtranscription com</a>.</p><br>
    <h2>Prerequisites</h2>
    <p>Before running the program, ensure you have the following prerequisites:</p>
    <ol>
        <li><strong>Python</strong>: If you don't have Python installed, <a href="https://www.python.org/downloads/">download and install it</a>.</li>
        <li><strong>Required Libraries</strong>: Download and install the necessary Python libraries by including the following lines at the beginning of your code:
            <pre><code>
                import os
                from selenium import webdriver
                from selenium.webdriver.common.by import By
                from selenium.webdriver.common.keys import Keys
                from selenium.webdriver.chrome.service import Service
                from bs4 import BeautifulSoup
                import pyautogui
            </code></pre>
        </li>
        <li><strong>GeckoDriver for Firefox</strong>: Download the <a href="https://github.com/mozilla/geckodriver/releases">GeckoDriver</a> for the Firefox browser. Make sure to define the path to the GeckoDriver executable in your code (see line 14).</li>
    </ol><br>
    <h2>Usage</h2>
    <p>Follow these steps to use the program:</p>
    <ol>
        <li><strong>Type Your Email Address</strong>: In the code (line 36), enter the email address you want to use for the typing test.</li>
        <li><strong>Run the Program</strong>: Execute the program.</li>
    </ol>
    <p><strong>Note</strong>: After running the code, please refrain from clicking any keys or moving the mouse until it has completed typing for you. Allow the program to finish the typing test without interruption.</p>
</body>
</html>
