from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up WebDriver
driver = webdriver.Chrome()

# Navigate to the w3schools website
driver.get("https://www.w3schools.com/")

# Test Element 1: Click on the "Login button
Login_button = driver.find_element("xpath", "/html/body/div[2]/div[1]/div[3]/a[1]")
Login_button.click()
time.sleep(2)  # Wait for page to load

# Test Element 2: Enter "Email address" in email field
Email_address = driver.find_element("xpath", "/html/body/div[1]/div/div/div[4]/div[1]/div/div[2]/form/div[1]/div[2]/input")
Email_address.send_keys("aqeedah2594@gmail.com")
time.sleep(3)  # Wait for search results to load

# Test Element 3: Enter "password" in password field
password_field = driver.find_element("xpath", "/html/body/div[1]/div/div/div[4]/div[1]/div/div[2]/form/div[2]/div[2]/input")
password_field.send_keys("Humairah@20")
time.sleep(3)  # Wait for search results to load

# Test Element 4: Click on the "Log in" button
Login_button = driver.find_element("xpath", "/html/body/div[1]/div/div/div[4]/div[1]/div/div[4]/div[1]/button")
Login_button.click()
time.sleep(3)  # Wait for page to load

# Test Element 5: Click on the "tutorial" tab
Tutorial_tab = driver.find_element("xpath", "/html/body/div[2]/div[1]/nav/a[1]")
Tutorial_tab.click()
time.sleep(3)  # Wait for page to load

# Test Element 6: Click on the "Learn C#" Option
C_Sharp_option = driver.find_element("xpath", "/html/body/div[2]/div[2]/div/nav[1]/div[1]/div/div[4]/div[1]/div[7]/a[1]")
C_Sharp_option.click()
time.sleep(3)  # Wait for page to load

# Test Element 7: Click on the "My W3Schools" button
Dashboard_button = driver.find_element("xpath", "/html/body/div[2]/div[1]/div[3]/a[4]")
Dashboard_button.click()
time.sleep(3)  # Wait for page to load

# Close the browser
driver.quit()
