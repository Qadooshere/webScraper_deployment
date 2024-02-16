import unittest
from main import init_webdriver, scrape_website_and_save_h2

class TestGcpCode(unittest.TestCase):

    def test_init_webdriver(self):
        driver = init_webdriver()
        self.assertIsNotNone(driver)

    def test_scrape_website_and_save_h2(self):
        url = "https://ilmiguide.com"
        result = scrape_website_and_save_h2(url)
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()