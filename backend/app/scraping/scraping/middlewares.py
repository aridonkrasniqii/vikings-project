import logging
import random
from scrapy.utils.response import response_status_message
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from scrapy.http import HtmlResponse
from webdriver_manager.chrome import ChromeDriverManager

logger = logging.getLogger('scraping')

class SeleniumMiddleware:
    def __init__(self, driver_name, browser_executable_path, driver_arguments):
        self.driver = None
        self.driver_name = driver_name
        self.browser_executable_path = browser_executable_path
        self.driver_arguments = driver_arguments
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/89.0",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/91.0.864.41",
        ]
        self._initialize_driver()

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        driver_name = crawler.settings.get('SELENIUM_DRIVER_NAME', 'chrome')
        browser_executable_path = crawler.settings.get('SELENIUM_BROWSER_EXECUTABLE_PATH', None)
        driver_arguments = crawler.settings.get('SELENIUM_DRIVER_ARGUMENTS', [])

        return cls(driver_name, browser_executable_path, driver_arguments)

    def _initialize_driver(self):
        if self.driver:
            return

        try:
            logger.info("Initializing Selenium with Google Chrome and WebDriver Manager")


            chrome_options = self._get_chrome_options(self.driver_arguments)
            # Automatically get the right driver using WebDriver Manager
            service = Service(ChromeDriverManager().install())  # WebDriver Manager will fetch the correct ChromeDriver
            self.driver = webdriver.Chrome(service=service, options=chrome_options)
            self.driver.set_window_size(1120, 550)
            self.driver.set_page_load_timeout(30)
            self.driver.logger = logging.getLogger('SeleniumMiddleware')

        except Exception as e:
            logging.error(f"Error initializing Selenium WebDriver: {str(e)}")

    def _get_chrome_options(self, driver_arguments):
        chrome_options = Options()

        # If you don't want to specify the browser executable path, WebDriver Manager handles it
        # But if needed, set it here like in the Brave setup
        if self.browser_executable_path:
            chrome_options.binary_location = self.browser_executable_path  # Path to Chrome binary

        # Add arguments to Chrome options
        for arg in driver_arguments:
            chrome_options.add_argument(arg)

        # Optional: Headless mode for scraping
        chrome_options.add_argument('--headless')  # Run headless mode
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-webgl')  # Disable WebGL if not needed
        chrome_options.add_argument('--ignore-certificate-errors')

        return chrome_options

    def process_request(self, request, spider):
        if not self.driver:
            spider.logger.error("Selenium WebDriver is not initialized.")
            return
        else:
            spider.logger.info(f"Selenium WebDriver initialized: {self.driver.name}")

        try:
            user_agent = random.choice(self.user_agents)
            self.driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": user_agent})
            self.driver.get(request.url)
            spider.logger.info("Page is loaded")

            body = self.driver.page_source
            return HtmlResponse(self.driver.current_url, body=body, encoding='utf-8', request=request)

        except Exception as e:
            spider.logger.error(f"Failed to load page: {request.url}. Error: {str(e)}")
            return self._retry(request, str(e), spider)

    def process_response(self, request, response, spider):
        if response.status in [403, 500, 502, 503, 504]:
            reason = response_status_message(response.status)
            return self._retry(request, reason, spider) or response
        return response

    def process_exception(self, request, exception, spider):
        spider.logger.error(f"Exception during request processing: {str(exception)}")
        return self._retry(request, str(exception), spider)

    def _retry(self, request, reason, spider):
        retries = request.meta.get('retry_times', 0) + 1
        retry_times = spider.settings.getint('RETRY_TIMES', 2)

        if retries <= retry_times:
            user_agent = random.choice(self.user_agents)
            spider.logger.info(f"Retrying {request.url} (failed {retries} times): {reason} with User-Agent: {user_agent}")
            retry_req = request.copy()
            retry_req.meta['retry_times'] = retries
            retry_req.headers['User-Agent'] = user_agent
            retry_req.dont_filter = True
            return retry_req
        else:
            spider.logger.error(f"Gave up retrying {request.url} (failed {retries} times): {reason}")
            return None
