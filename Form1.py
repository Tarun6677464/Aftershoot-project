import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Set up Chrome options
option = webdriver.ChromeOptions()

# Initialize Chrome WebDriver
driver = webdriver.Chrome(options=option)

# Navigate to the login page of the admin demo site
driver.get('https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F')
driver.maximize_window()

# Note : Sleep is used to demonstrate the automation flow slowly to understand 
time.sleep(2)

# Login with valid credentials
driver.find_element(By.ID, "Email").clear()
time.sleep(1)
driver.find_element(By.ID, "Password").clear()
time.sleep(1)
driver.find_element(By.ID, "Email").send_keys("admin@yourstores.com")
time.sleep(1)
driver.find_element(By.ID, "Password").send_keys("admin")
time.sleep(1)
driver.find_element(By.CLASS_NAME, "login-button").click()
time.sleep(6)

# Logout and login again with different credentials
driver.find_element(By.ID, "Email").clear()
time.sleep(1)
driver.find_element(By.ID, "Password").clear()
time.sleep(1)
driver.find_element(By.ID, "Email").send_keys("admin@yourstore.com")
time.sleep(1)
driver.find_element(By.ID, "Password").send_keys("admin")
time.sleep(1)
driver.find_element(By.CLASS_NAME, "login-button").click()
time.sleep(6)

# Access user management section
driver.find_element(By.CLASS_NAME, "fa-user").click()
time.sleep(5)
driver.find_element(By.XPATH, "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a/p").click()
time.sleep(3)

# Search for a user with specific details and fill the form
driver.find_element(By.ID, "SearchEmail").send_keys("test11@gmail.com")
time.sleep(1)
driver.find_element(By.ID, "SearchLastActivityFrom").send_keys("12/12/23")
time.sleep(2)
driver.find_element(By.ID, "SearchFirstName").send_keys("Tarun")
time.sleep(2)
driver.find_element(By.ID, "SearchLastActivityTo").send_keys("22/12/23")
time.sleep(2)
driver.find_element(By.ID, "SearchLastName").send_keys("purushottam")
time.sleep(2)
driver.find_element(By.ID, "SearchCompany").send_keys("Wipro")
time.sleep(2)
driver.find_element(By.ID, "SearchMonthOfBirth").send_keys("10")
time.sleep(2)
driver.find_element(By.ID, "SearchDayOfBirth").send_keys("15")
time.sleep(2)
driver.find_element(By.ID, "SearchIpAddress").send_keys("148.156.652.123")
time.sleep(2)
driver.find_element(By.ID, "SearchRegistrationDateFrom").send_keys("05/02/24")
time.sleep(2)

# Perform the search
driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/form[1]/section/div/div/div/div[1]/div/div[2]/div[1]/div[2]/div[5]/div[2]/div/div").click()
time.sleep(2)
driver.find_element(By.ID, "SearchRegistrationDateTo").send_keys("15/03/24")
time.sleep(2)
driver.find_element(By.ID, "search-customers").click()
time.sleep(5)

# Scroll down
driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
time.sleep(5)

# Logout
driver.find_element(By.ID, "Logout").click()
time.sleep(2)

# Close the WebDriver
driver.quit()
