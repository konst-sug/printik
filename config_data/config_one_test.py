from fake_useragent import UserAgent
from selenium.webdriver.chrome.options import Options
import os

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

#site_id : 1-printnatkani, 2-flagwinder, 3-flag-parus, 4-fotopled, 5-print-na-tkani.kz
# ----------- testing urls list--------------------------------------
url = [
    'https://printnatkani.ru/',
    'https://printnatkani.ru/sdelat_zakaz',
    'https://printnatkani.ru/futbolki_mayki',
    'https://printnatkani.ru/flagi/flag_parus_vinder',
    "https://printnatkani.ru/izgotovlenie_platkov#raschet",
    "https://flagwinder.ru/",
    'https://flagwinder.ru/#make_order',
    "https://flag-parus.ru/",
    "https://flag-parus.ru/?#make_order",
    "https://flag-parus.ru/konstruktor-maketov/",
    "https://flag-parus.ru/?#calculator",
    "https://flag-parus.ru/?#our-production",
    'https://fotopled.ru/',
    'https://fotopled.ru/oformit_zakaz',
    'https://fotopled.ru/pechat_na_futbolkakh',
    'https://fotopled.ru/sozdat-fotokollazh-online',
    "https://print-na-tkani.kz/",
    "https://print-na-tkani.kz/sdelat_zakaz"
]

# ------------ test data to upload ----------------------------------
test_phone = +79180000001
test_data = [
    'TestTestTest',
    'QA Engineer', 
    'max.step26@gmail.com',
    '+79096300001', 
    'Aвтотест проверки работы сайта',
    'Самовывоз'
    ]

#--------- path to image to upload, file name to screenshot----------
#---------get the working directory path, db path, upload path ------
test_data1 = []
directory_path = os.path.dirname(os.path.abspath(__file__))
file_name = os.path.join(directory_path, "result.db")
env_path = os.path.join(directory_path, '.env')
work_dir =  os.path.split(os.path.normpath(directory_path))
update_path = work_dir[:1]
db_path = os.path.join(*update_path, 'database/result.db')
print(db_path) 
foto_url = os.path.join(*update_path,'93.jpg')
env_path = os.path.join(*update_path, '.env')
scr_file = os.path.join(*update_path,'results/scr1.png')
target_fold = os.path.join(*update_path, 'results/')
print(foto_url, env_path, target_fold, sep="\n")

# -------  time to keeping test`s attachments in hours --------------
time_keep = 12
# -------- testing urls dict ----------------------------------------
url_d = {
        'print_main': 'https://printnatkani.ru/',
        'print_order': 'https://printnatkani.ru/sdelat_zakaz',
        'print_cosuv': 'https://printnatkani.ru/futbolki_mayki',
        'print_flagi': 'https://printnatkani.ru/flagi/flag_parus_vinder',
        'print_platki': 'https://printnatkani.ru/izgotovlenie_platkov',
        'winder_main': 'https://flagwinder.ru/',
        'winder_order': 'https://flagwinder.ru/#make_order',
        'winder_flag' : 'https://flagwinder.ru/#calculator',
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

functions_in_acc = {
    11: "printOrder_to_tg",
    12: "printFlagconstr_to_tg",
    13: "printPlatki_to_tg",
    14: "printConstr_to_tg",
    15: "printCosuv_to_tg", 
    20: "winderOrder_to_tg",
    21: "winderConstr_to_tg",
    30: "parusOrder_to_tg",
    31: "parusFlag_to_tg",
    32: "parusProds_to_tg",
    33: "parusCosuv_to_tg", 
    40: "pledrOrder_to_tg",
    41: "pledConstr_to_tg",
    42: "pledCosuv_to_tg",
    50: "kazOrder_to_tg",
    51: "kazConstructor_to_tg"
}