from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import logging


def init_webdriver():
    # Configure webdriver options for headless operation
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Initialize the WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver


def scrape_website_and_save_h2(url):
    global driver
    try:
        # Initialize Selenium WebDriver
        driver = init_webdriver()

        # Navigate to the URL
        driver.get(url)

        # Find all h2 elements
        h2_elements = driver.find_elements(By.TAG_NAME, "h2")
        h2_texts = [element.text for element in h2_elements]

        # Save the scraped h2 data to a text file
        with open("/mnt/data/scraped_h2_texts.txt", "w", encoding="utf-8") as file:
            for text in h2_texts:
                file.write(f"{text}\n")

        logging.info("Scraped h2 data saved successfully.")
        return f"Scraped h2 data saved successfully to scraped_h2_texts.txt"

    except Exception as e:
        logging.error(f"Error occurred during web scraping: {e}")
        return f"An error occurred: {e}"

    finally:
        # Ensure the driver is quit to free resources
        driver.quit()


url = "https://ilmiguide.com"
result = scrape_website_and_save_h2(url)
