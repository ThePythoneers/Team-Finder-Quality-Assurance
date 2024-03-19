import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def run_signin_test(credentials):
    # Initialize Chrome WebDriver
    driver = webdriver.Chrome()

    try:
        start_time = time.time()  # Capture start time
        driver.get("https://assist-tech-challenge-the-pythoneers.vercel.app/authentication/signIn")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[name='email']")))
        end_time = time.time()  # Capture end time

        load_time = end_time - start_time
        print(f"Page loaded in {load_time:.2f} seconds")

        # Fill in the form fields using credentials dictionary
        email_input = driver.find_element(By.CSS_SELECTOR, "[name='email']")
        email_input.send_keys(credentials['email'])

        password_input = driver.find_element(By.CSS_SELECTOR, "[name='password']")
        password_input.send_keys(credentials['password'])

        # Click the submit button
        submit_button = driver.find_element(By.XPATH, "//button[contains(text(),'Sign In')]")
        submit_button.click()

        print("Test run successful")

        # Create a directory for screenshots if it doesn't exist
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")
        # Take screenshot after sign-in and save it in the screenshots folder
        screenshot_dir = "screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)
        screenshot_filename = f"signup_{credentials['email']}_{time.strftime('%Y%m%d_%H%M%S')}.png"
        screenshot_path = os.path.join(screenshot_dir, screenshot_filename)
        driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved at: {screenshot_path}")


    except Exception as e:
        print("Test run failed:", e)

    finally:
        driver.quit()

# If script is run standalone
if __name__ == "__main__":
    # Prompt user to enter credentials
    email = input("Enter email: ")
    password = input("Enter password: ")

    # Create credentials dictionary
    credentials = {
        'email': email,
        'password': password,
    }

    # Run the test with provided credentials
    run_signin_test(credentials)