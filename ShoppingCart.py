import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up Chrome options
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=option)

# Navigate to Amazon website
driver.get('https://www.amazon.in')
driver.maximize_window()
time.sleep(2)

# Search for "Iphone15" in the search bar
driver.find_element(By.ID, "twotabsearchtextbox").send_keys("Iphone15")
time.sleep(2)

# Click on the search button
driver.find_element(By.ID, "nav-search-submit-button").click()
time.sleep(2)

# Click on the first search result's image
driver.find_element(By.CLASS_NAME, "s-image").click()
time.sleep(5)

# Navigate to the specific product page
driver.get('https://www.amazon.in/Apple-iPhone-15-128-GB/dp/B0CHX2F5QT/ref=sr_1_1_sspa?crid=2S2IHQWMG6ZBJ&keywords=iphone%2B15&qid=1700536388&sprefix=iphone%2B15%2B%2Caps%2C201&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1')
driver.maximize_window()
time.sleep(10)

# Click on the "Add to Cart" button
driver.find_element(By.ID, "add-to-cart-button").click()
time.sleep(10)

# View the shopping cart
driver.get('https://www.amazon.in/gp/cart/view.html?ref_=nav_cart')
driver.maximize_window()
time.sleep(5)

# Click on the "Proceed to Checkout" button
driver.find_element(By.ID, "vgsqub-gp2dt3-630jap-wqm3wp").click()
time.sleep(5)

# Close the browser
driver.quit()