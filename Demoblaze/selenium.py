import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

# Constants
USERNAME = 'Mallikarjun'
PASSWORD = 'Suvijaya123@'
ITEM_NAMES = ['Samsung galaxy s6', 'Nokia lumia 1520', 'Nexus 6']

# Path to the manually downloaded ChromeDriver
CHROMEDRIVER_PATH = 'C:/Users/MALLIKARJUN NAIK/Downloads/chromedriver-win64/chromedriver.exe'
 # Update this path

# Initialize WebDriver
service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10)

def find_item_by_name(name):
    """Find an item by its name and return the element if found."""
    items = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.hrefch')))
    for item in items:
        if name in item.text:
            return item
    print(f"Item '{name}' not found.")
    return None

def add_item_to_cart(item_name):
    """Add an item to the cart by its name."""
    try:
        # Find the item
        item = find_item_by_name(item_name)
        if not item:
            return

        # Click on the item
        item.click()
        print(f"Clicked on item '{item_name}'")

        # Wait for the item detail page to load
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.btn-success')))
        print("Item detail page loaded")
        
        time.sleep(2)  # Added delay

        # Add to cart
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-success')))
        add_to_cart_button.click()
        print("Clicked Add to Cart")

        # Accept alert
        wait.until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert.accept()
        print("Alert accepted")
        
        time.sleep(2)  # Added delay

        # Go to cart
        cart_button = wait.until(EC.element_to_be_clickable((By.ID, 'cartur')))
        cart_button.click()
        print("Navigated to cart")

        time.sleep(2)  # Added delay

        # Return to home page
        home_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.nav-link[href="index.html"]')))
        home_button.click()
        print("Navigated back to home page")

        time.sleep(2)  # Added delay

    except StaleElementReferenceException:
        print(f"Encountered stale element reference while adding '{item_name}'. Retrying...")
        add_item_to_cart(item_name)  # Retry

try:
    # Step 1: Navigate to DemoBlaze
    driver.get('https://www.demoblaze.com/')
    time.sleep(2)  # Added delay
    
    # Step 2: Click on the log in button
    login_button = wait.until(EC.element_to_be_clickable((By.ID, 'login2')))
    login_button.click()

    # Wait for the login modal to be visible
    wait.until(EC.visibility_of_element_located((By.ID, 'logInModal')))
    time.sleep(2)  # Added delay

    # Step 3: Enter username and password
    username_field = wait.until(EC.element_to_be_clickable((By.ID, 'loginusername')))
    username_field.send_keys(USERNAME)
    
    password_field = wait.until(EC.element_to_be_clickable((By.ID, 'loginpassword')))
    password_field.send_keys(PASSWORD)
    
    # Click the login button
    driver.find_element(By.CSS_SELECTOR, 'button[onclick="logIn()"]').click()

    # Wait for login to complete
    wait.until(EC.presence_of_element_located((By.ID, 'nameofuser')))
    time.sleep(2)  # Added delay

    # Step 4: Add the specified items to the cart
    for item_name in ITEM_NAMES:
        add_item_to_cart(item_name)

    # Step 5: Log out
    logout_button = wait.until(EC.element_to_be_clickable((By.ID, 'logout2')))
    logout_button.click()
    print("Logged out of the website")

finally:
    # Close the driver
    driver.quit()
