from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

try:
    driver.get("https://qawithdrawal.ccbp.tech/")
    driver.maximize_window()
    time.sleep(1)

    username_element = driver.find_element(By.CSS_SELECTOR, "div[class*='details'] > p")
    actual_username = username_element.text.strip()
    expected_username = "Sarah Williams"

    if actual_username == expected_username:
        print("Username is correct")
    else:
        print("Incorrect username")

    balance_element = driver.find_element(By.CSS_SELECTOR, "p.balance")
    actual_balance = int(balance_element.text)
    expected_balance = 2000

    if actual_balance == expected_balance:
        print("Initial balance is correct")
    else:
        print("Incorrect initial balance")

    denomination_buttons = driver.find_elements(By.CSS_SELECTOR, "li.denomination-item")

    for button in denomination_buttons:
        denomination = int(button.text)
        for _ in range(2):
            button.click()
            time.sleep(0.5)
            expected_balance -= denomination
            updated_balance = int(driver.find_element(By.CSS_SELECTOR, "p.balance").text)

            if updated_balance != expected_balance:
                print("Mismatch found in balance")
            else:
                print("Withdrawal App working as expected")
    
    driver.quit()
except:
    print("Exception occured")
