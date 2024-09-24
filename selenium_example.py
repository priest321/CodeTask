from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import selenium

print(selenium.__version__)
# Create a new instance of the Chrome driver
driver = webdriver.Firefox()  # Ensure chromedriver.exe is in your PATH
driver2 = webdriver.Firefox()
# Go to a website
driver.get("http://www.python.org")
time.sleep(1)
# Find the search box
search_box = driver.find_element(By.ID, "id-search-field")

time.sleep(1)
# Type in the search box
search_box.send_keys("getting started with python1111")
time.sleep(1)
# Simulate hitting the return key
search_box.send_keys(Keys.RETURN)
time.sleep(1)
search_boxs = driver.find_elements("name", "q")
count = 1
for box in search_boxs:
    box.clear()
    count += 1
    box.send_keys(f"Robert {count}")

time.sleep(10)
# Close the browser
driver.quit()