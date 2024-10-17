import datetime
import logging
import time

from config_data.config_one_test import url, db_path, test_data, foto_url, chrome_options, functions_in_acc
from database.sqliter import SQLiter
from config_starter import test_list
from utils.parusToTg import parusFlag_to_tg, parusProds_to_tg, parusCosuv_to_tg, parusOrder_to_tg
from utils.winderToTg import winderConstr_to_tg, winderOrder_to_tg
from utils.pledToTg import pledConstr_to_tg, pledCosuv_to_tg, pledrOrder_to_tg
from utils.printToTg import printCosuv_to_tg, printFlagconstr_to_tg, printOrder_to_tg, printPlatki_to_tg, printConstr_to_tg
from utils.kazToTg import kazOrder_to_tg, kazConstructor_to_tg
from selenium import webdriver

db = SQLiter(db_path)
logging.basicConfig(level=logging.INFO)

driver = webdriver.Chrome(options=chrome_options)

timer = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')



#-------------------format & save data to database ------------------
def db_saver(data: list, site_id: int, func: str):
    test_name1 = f"{data[2].split('-')[0]}--{func}"
    if len(data) <= 4:
        db.post_info("result_table", data[0], site_id, test_name1, data[1], data[2])
    else:
        test_name2 = f"{data[4].split('-')[0]}--{func}"
        db.post_info("result_table", data[0], site_id, test_name1, data[1], data[2])
        db.post_info("result_table", data[0], site_id, test_name2, data[3], data[4])    


#site_id : 1-printnatkani, 2-flagwinder, 3-flag-parus, 4-fotopled, 5-print-na-tkani.kz  #
def full_test(send=False):
    '''Наборы одиночных тестов. Раскомментировать для выполнения. 
       send - определяет, требуется ли отправка формы заказа с сайта в СРМ. По умолчанию - False'''
    #------ printnatkani tests -----------------------------------
    # test_res = printOrder_to_tg(driver, url, test_data, send)
    # logging.info(test_res)
    # time.sleep(5)

    # test_res = printFlagconstr_to_tg(driver, url, test_data, send)
    # logging.info(test_res)
    # time.sleep(5)

    # test_res = printCosuv_to_tg(driver, url, test_data, send)
    # logging.info(test_res)
    # time.sleep(5)

    # test_res = printPlatki_to_tg(driver, url, test_data, send)
    # logging.info(test_res)
    # time.sleep(5)

    # test_res = printConstr_to_tg(driver, url, test_data, send)
    # logging.info(test_res)
 

#------ flag winder tests -----------------------------------
    # test_res = winderOrder_to_tg(driver, url, test_data, send)
    # logging.info(test_res)
    # time.sleep(5)

    # test_res = winderConstr_to_tg(driver, url, test_data, send)
    # logging.info(test_res)
    # time.sleep(5)


#------ flag parus tests -----------------------------------
    # test_res = parusFlag_to_tg(driver, url, test_data, send)
    # logging.info(test_res)
    # time.sleep(5)

    # test_res = parusProds_to_tg(driver, url, test_data, send)
    # logging.info(test_res)
    # time.sleep(5)

    # test_res = parusOrder_to_tg(driver, url, test_data, send)
    # logging.info(test_res)
    # time.sleep(5)

    # test_res = parusCosuv_to_tg(driver, url, test_data, send)
    # logging.info(test_res)
    # time.sleep(5)


#------ fotopled  tests -----------------------------------
    # test_res = pledrOrder_to_tg(driver, url, test_data, send)
    # logging.info(test_res)
    # time.sleep(5)

    # test_res = pledCosuv_to_tg(driver, url, test_data, send)
    # logging.info(test_res)
    # time.sleep(5)

    # test_res = pledConstr_to_tg(driver, url, test_data, send)
    # logging.info(test_res)
    # time.sleep(5)


#-------------------------- kaz  tests -----------------------------------
    # test_res = kazOrder_to_tg(driver, url, test_data, send)
    # logging.info(test_res)

    # test_res = kazConstructor_to_tg(driver, url, test_data, send)
    # logging.info(test_res)
    time.sleep(1)

def order_tests(send=False, stat=False, tests=test_list):
    '''send -- отправка заказа с сайта в СРМ, по умолчанию - False;
       stat -- запись результата в БД, по умолчанию - False;
       tests -- список номеров тестовых сценариев, по умолчанию загружается из config_starter; '''
    time_begin = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    for i in tests:
        func = functions_in_acc[i]
        res = globals()[func](driver, url, test_data, send)
        time.sleep(2)
        site_id = (i // 10)
        if stat:
            db_saver(res, site_id, func) 
        logging.info(f'{time_begin}--{i}--{func}')


def main():
    full_test()
    order_tests(stat=True)
    

if __name__ == '__main__':
    main()
