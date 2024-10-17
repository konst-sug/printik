from fake_useragent import UserAgent
from selenium.webdriver.chrome.options import Options
import pathlib


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
chrome_options.add_argument("--zoom=0.8")
chrome_options.page_load_strategy="eager"#---'normal', 'eager', 'none'

#site_id : 1-printnatkani, 2-flagwinder, 3-flag-parus, 4-fotopled, 5-print-na-tkani.kz  #

# ------------ test data to upload ----------------------------------
test_phone = '+79180000001'
test_data = ['TestTestTest', 'qa engineer', 'max.step26@gmail.com', '+79096300001', 'Aвтотест проверки работы сайта ','Самовывоз']
test_data2 = []

#--------- path to image to upload, file name to screenshot----------
foto_url1 = '/home/konst/Изображения/cat_eyes.png'
scr_file = 'screen1.png'
db_path_old = '/home/konst/snake/selenium_tests/func/result.db'
site_id =5

#--------- get the path to image, db file ,screenshots folder--------
BASE_DIR = pathlib.Path(__file__).resolve().parent.parent
path = pathlib.PosixPath(BASE_DIR)
index = path.parts.index('printik')
project_dir = pathlib.PurePosixPath(*path.parts[:index+1])
print(BASE_DIR)
db_path = project_dir.joinpath('database/result.db')
target_fold = project_dir.joinpath('results')
foto_url = project_dir.joinpath('93.jpg')