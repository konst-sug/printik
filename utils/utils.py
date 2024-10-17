from fake_useragent import UserAgent
from selenium.webdriver.chrome.options import Options
import os
import datetime

ua = UserAgent()
ua_ag = ua.random
chrome_options = Options()
#chrome_options.add_argument('--headless')
chrome_options.add_argument(f'user-agent={ua_ag}')
chrome_options.add_experimental_option('excludeSwitches',["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension',False)
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--remote-debugging-port=9222")


def func():
    pass


def get_settings(update_path):
    timer = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    res_file = os.path.join(*update_path,f'results/{timer}-scr.png')
    return timer, res_file