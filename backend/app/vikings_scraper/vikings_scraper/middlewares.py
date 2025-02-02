import logging
from scrapy import signals
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
# Set up logging for the Spider and Downloader middlewares
logger = logging.getLogger('vikings_scraper')


class VikingsScraperSpiderMiddleware:
    # This middleware manages spider-level logic such as start requests and responses
    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider middleware
        return None  # No changes to the response

    def process_spider_output(self, response, result, spider):
        # Called after the spider processes the response
        for i in result:
            yield i  # Forward the output

    def process_spider_exception(self, response, exception, spider):
        # Called when an exception is raised by the spider processing
        pass  # We don't handle any exceptions here, just let Scrapy continue

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests for the spider
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info(f"Spider opened: {spider.name}")


class VikingsScraperDownloaderMiddleware:
    # This middleware handles the downloader-level logic such as requests and responses
    @classmethod
    def from_crawler(cls, crawler):
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader middleware
        return None  # No changes to the request

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader
        return response  # Forward the response

    def process_exception(self, request, exception, spider):
        # Called when an exception occurs during the downloading process
        pass  # No custom handling of exceptions

    def spider_opened(self, spider):
        spider.logger.info(f"Spider opened: {spider.name}")

class SeleniumMiddleware:
    def __init__(self, driver_name, browser_executable_path, driver_arguments):
        self.driver = None
        self.driver_name = driver_name
        self.browser_executable_path = browser_executable_path
        self.driver_arguments = driver_arguments
        self._initialize_driver()

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        # This method is required by Scrapy to configure the middleware using settings
        driver_name = crawler.settings.get('SELENIUM_DRIVER_NAME')
        browser_executable_path = crawler.settings.get('SELENIUM_DRIVER_EXECUTABLE_PATH')
        driver_arguments = crawler.settings.get('SELENIUM_DRIVER_ARGUMENTS', [])

        return cls(driver_name, browser_executable_path, driver_arguments)

    def _initialize_driver(self):
        if self.driver:
            return

        try:
            service = Service(self.browser_executable_path)
            edge_options = self._get_edge_options(self.driver_arguments)
            self.driver = webdriver.Edge(service=service, options=edge_options)
            self.driver.set_window_size(1120, 550)
            self.driver.set_page_load_timeout(30)
            self.driver.logger = logging.getLogger('SeleniumMiddleware')  # Set up logging for SeleniumMiddleware
        except Exception as e:
            logging.error(f"Error initializing Selenium WebDriver: {str(e)}")

    def _get_edge_options(self, driver_arguments):
        edge_options = Options()
        for arg in driver_arguments:
            edge_options.add_argument(arg)
        edge_options.add_argument('--disable-gpu')
        edge_options.add_argument('--no-sandbox')
        edge_options.add_argument('--disable-webgl')  # Disable WebGL if it's not required
        edge_options.add_argument('--enable-unsafe-swiftshader')  # Add this for the WebGL fallback
        return edge_options

    def process_request(self, request, spider):
        if not self.driver:
            spider.logger.error("Selenium WebDriver is not initialized.")
            return
        else:
            spider.logger.info(f"Selenium WebDriver initialized: {self.driver.name}")

        try:
            self.driver.get(request.url)
            spider.logger.info("Page is loaded")
        except Exception as e:
            spider.logger.error(f"Failed to load page: {request.url}. Error: {str(e)}")

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request() raises an exception.
        pass
