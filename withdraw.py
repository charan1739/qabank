from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Create driver instance
driver = webdriver.Chrome()

try:
    # Navigate to the URL
    driver.get("https://qawithdrawal.ccbp.tech/")
    driver.maximize_window()
    time.sleep(1)

    # --- Step 1: Verify Username ---
    username_element = driver.find_element(By.CSS_SELECTOR, "div[class*='details'] > p")
    actual_username = username_element.text.strip()
    expected_username = "Sarah Williams"

    if actual_username == expected_username:
        print("Username is correct")
    else:
        print("Incorrect username")

    # --- Step 2: Verify Initial Balance ---
    balance_element = driver.find_element(By.CSS_SELECTOR, "p.balance")
    actual_balance = int(balance_element.text)
    expected_balance = 2000

    if actual_balance == expected_balance:
        print("Initial balance is correct")
    else:
        print("Incorrect initial balance")

    # --- Step 3: Find all 4 denomination buttons ---
    denomination_buttons = driver.find_elements(By.CSS_SELECTOR, "li.denomination-item")

    for button in denomination_buttons:
        # Get denomination amount from button text
        denomination = int(button.text)
        
        # Click 2 times
        for _ in range(2):
            button.click()
            time.sleep(0.5)
            expected_balance -= denomination

            # Get updated balance
            updated_balance = int(driver.find_element(By.CSS_SELECTOR, "p.balance").text)

            if updated_balance != expected_balance:
                print("Mismatch found in balance")
            else:
                print("Withdrawal App working as expected")
    
    driver.quit()
except:
    print("Exception occured")