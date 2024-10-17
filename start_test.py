import datetime
import logging
from time import sleep

from config_data.config_one_test import url, db_path, test_data, foto_url, functions_in_acc, chrome_options
from config_starter import cron_test_list
from selenium import webdriver
from database.sqliter import SQLiter
from utils import *

db = SQLiter(db_path)
logging.basicConfig(level=logging.INFO)


timer = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
driver = webdriver.Chrome(options=chrome_options)
table = "result_table"

#site_id : 1-printnatkani, 2-flagwinder, 3-flag-parus, 4-fotopled, 5-print-na-tkani.kz  #
def full_test():
    pass


def db_saver(data: list, site_id: int, func: str):
    test_name1 = f"{data[2].split('-')[0]}--{func}"
    if len(data) <= 4:
        db.post_info(table, data[0], site_id, test_name1, data[1], data[2])
    else:
        test_name2 = f"{data[4].split('-')[0]}--{func}"
        db.post_info(table, data[0], site_id, test_name1, data[1], data[2])
        db.post_info(table, data[0], site_id, test_name2, data[3], data[4]) 


def order_tests(send=False, stat=False, tests=cron_test_list):
    '''send -- отправка заказа с сайта в СРМ, по умолчанию - False;
       stat -- запись результата в БД, по умолчанию - False;
       tests -- список номеров тестовых сценариев, по умолчанию загружается из config_starter; '''
    time_begin = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    for i in tests:
        func = functions_in_acc[i]
        res = globals()[func](driver, url, test_data, send)
        sleep(3)
        site_id = (i // 10)
        if stat:
            db_saver(res, site_id, func) 
        logging.info(f'time {time_begin}--test № {i}--from {func}')     

 
def main():
    #full_test()
    order_tests(stat=True)


if __name__ == '__main__':
    main()
