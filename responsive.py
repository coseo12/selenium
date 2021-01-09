import time
import os
from math import ceil
from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

class ResponsiveTester:
    def __init__(self, urls):
        self.urls = urls
        # self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        self.browser.maximize_window()
        self.sizes = [480, 960, 1366, 1920]

    def screenshot(self, url):
        try:
            if not(os.path.isdir(f"screenshots/{url}")):
                os.makedirs(os.path.join(f"screenshots/{url}"))
        except OSError:
            print("Failed to create directory!!!!!")
            raise
        self.browser.get(url)
        window = self.browser.get_window_size()
        BROWSER_HEIGHT = window["height"]
        for size in self.sizes:
            self.browser.set_window_size(size, BROWSER_HEIGHT)
            self.browser.execute_script(f"window.scrollTo(0, 0)")
            time.sleep(2)
            scroll_size = self.browser.execute_script("return document.body.scrollHeight")
            total_section = ceil(scroll_size / BROWSER_HEIGHT)
            for section in range(total_section + 1):
                self.browser.execute_script(f"window.scrollTo(0, {(section) * BROWSER_HEIGHT})")
                self.browser.save_screenshot(f"screenshots/{url}/{size}x{section+1}.png")
                time.sleep(1)

    def start(self):
        for url in self.urls:
            self.screenshot(url)

    def finished(self):
        self.browser.quit()


test = ResponsiveTester(["https://nomadcoders.co", "https://google.com"])
test.start()
test.finished()