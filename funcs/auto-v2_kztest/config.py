import pathlib
from fake_useragent import UserAgent
from selenium.webdriver.chrome.options import Options


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
# ----------- test url`s -------------------------------

url_d = {
        'print_main': 'https://printnatkani.ru/',
        'print_order': 'https://printnatkani.ru/sdelat_zakaz',
        'print_cosuv': 'https://printnatkani.ru/futbolki_mayki',
        'print_flagi': 'https://printnatkani.ru/flagi/flag_parus_vinder',
        'print_platki': 'https://printnatkani.ru/izgotovlenie_platkov',
        'winder_main': 'https://flagwinder.ru/',
        'winder_order': 'https://flagwinder.ru/#make_order',
        'parus_main': 'https://flag-parus.ru/',
        'parus_order': 'https://flag-parus.ru/?#make_order',
        'parus_cosuv': 'https://flag-parus.ru/konstruktor-maketov/',
        'parus_flag': 'https://flag-parus.ru/?#calculator',
        'parus_prod': 'https://flag-parus.ru/?#our-production',
        'pled_main': 'https://fotopled.ru/',
        'pled_order': 'https://fotopled.ru/oformit_zakaz',
        'pled_cosuv': 'https://fotopled.ru/pechat_na_futbolkakh',
        'pled_constr': 'https://fotopled.ru/sozdat-fotokollazh-online',
        'kaz': 'https://print-na-tkani.kz/'
        }

# ------------ test data to upload -----------------------
test_phone = '+79180000001'
test_data = [
    'Test',
    'Константин', 
    'max.step26@gmail.com',
    '+79096300001', 
    'Aвтотест проверки работы сайта',
    'Самовывоз'
    ]
test_data2 = []

#--------- path to image to upload, file name to screenshot-------
foto_url_old = '/home/alex/snake/print/93.jpg'
foto_url_mx = '/home/konst/Pictures/aut.jpg'
scr_file = 'screen1.png'
db_path_mx = '/home/alex/snake/print/result.db'
site_id =5

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent
path = pathlib.PosixPath(BASE_DIR)
index = path.parts.index('printik')
project_dir = pathlib.PurePosixPath(*path.parts[:index+1])
print(BASE_DIR)
db_path = project_dir.joinpath('database/result.db')
target_fold = project_dir.joinpath('results')
foto_url = project_dir.joinpath('93.jpg')
print(db_path, target_fold, foto_url, sep='\n')

#fun = lambda x : 1 if x == 1 else math.ceil(math.sinh(fun (x-1)))
#print(fun(5))