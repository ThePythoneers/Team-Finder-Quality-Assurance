from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def run_signup_test(credentials):
    # Initialize Chrome WebDriver
    driver = webdriver.Chrome()

    try:
        start_time = time.time()  # Capture start time
        driver.get("https://testing-ebon-chi.vercel.app/")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[name='username']")))
        end_time = time.time()  # Capture end time

        load_time = end_time - start_time
        print(f"Page loaded in {load_time:.2f} seconds")

        # Fill in the form fields using credentials dictionary
        username_input = driver.find_element(By.CSS_SELECTOR, "[name='username']")
        username_input.send_keys(credentials['username'])

        email_input = driver.find_element(By.CSS_SELECTOR, "[name='email']")
        email_input.send_keys(credentials['email'])

        password_input = driver.find_element(By.ID, "password")
        password_input.send_keys(credentials['password'])

        organization_name_input = driver.find_element(By.CSS_SELECTOR, "[name='organization_name']")
        organization_name_input.send_keys(credentials['organization_name'])

        hq_name_input = driver.find_element(By.CSS_SELECTOR, "[name='hq_address']")
        hq_name_input.send_keys(credentials['hq_address'])

        # Click the submit button
        submit_button = driver.find_element(By.XPATH, "//button[contains(text(),'Sign Up')]")
        submit_button.click()

        print("Test run successful")

    except Exception as e:
        print("Test run failed:", e)

    finally:
        # Add a small sleep
        time.sleep(2)  # Sleep for 2 seconds
        driver.quit()


# Example usage:
credentials = {
    'username': "testuser",
    'email': "test@example.com",
    'password': "password123",
    'organization_name': "TestOrg",
    'hq_address': "123 Test St"
}

if __name__ == "__main__":
    run_signup_test(credentials)
