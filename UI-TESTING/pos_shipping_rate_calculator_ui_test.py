from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Setting up the WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

try:
    # Navigate to the rate calculator page
    driver.get("https://pos.com.my/send/ratecalculator")

    # Enter "Malaysia" as the "From" country and enter "35600" as the postcode
    input_field = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Postcode"]')
    input_field.send_keys("35600")

    # Enter "Albania" as the "To" country
    # Locate the country dropdown and click to open it
    dropdown_icon = driver.find_element(By.CLASS_NAME, "mat-icon")
    dropdown_icon.click()

    # Wait for the dropdown options to appear
    country_item = driver.find_element(By.XPATH, "//small[@title='Albania - AL']")
    country_item.click()

    # Leave the "To" postcode field empty
    # (Assuming no action needed since it's already empty)

    # Enter "1" as the "Weight"
    weight = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="eg. 0.1kg"]')  
    weight.send_keys("1")


    # Click the "Calculate" button
    
    calculate_button = driver.find_element(By.XPATH, "//a[contains(@class, 'no-underline') and contains(text(), 'Calculate')]")
    print("Calculating ...")
    calculate_button.click()

    # Verifying multiple quotes are displayed
    time.sleep(10)
    quotes = driver.find_elements(By.XPATH, "//a[contains(text(), 'Book Now')]") 

    assert len(quotes) > 1, "Multiple quotes were not found!"

    print("Test Passed: Multiple quotes are displayed.")
    print(len(quotes))

except Exception as e:
    print(f"Test Failed: {e}")

finally:
    # Close the browser
    driver.quit()
