import logging
import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from sqliter import SQLiter

from config import test_data, url_d, chrome_options, db_path

logging.basicConfig(level=logging.INFO)

driver = webdriver.Chrome(options=chrome_options)
db = SQLiter(db_path)
timer = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
site_id= 3


def constructor_test(send_status=False):
    # --------------------constructor order test -------------------- 
    driver.get(url=url_d['parus_cosuv'])
    driver.implicitly_wait(5)
    driver.execute_script("window.scrollTo(0,300)","")
    time.sleep(1)
    try:
        driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))
        up_butn = driver.find_element(By.XPATH, "/html/body/div/nav/ul/li[12]")
        ActionChains(driver).move_to_element(up_butn).click(up_butn).perform()
        time.sleep(1)
        text_area = driver.find_element(By.XPATH, "/html/body/div/aside/div/div[3]/div/textarea")
        text_area.clear()
        text_area.send_keys("test quest line\n")
        time.sleep(1)
        ActionChains(driver).move_by_offset(150,150).click().perform()
        ord_btn = driver.find_element(By.XPATH, "/html/body/div[1]/nav/ul/li[15]")
        ord_btn.click()
        test_status1, test_text1 = True, "Flag-parus_cosuv_constructor_test - OK"
    except Exception as error:
                test_status1, test_text1 = False, "Flag-parus_cosuv_constructor_test - Error"
                logging.error("Error in 'upload-block' in the driver object block " + str(error))
    logging.info(f'{timer}-{(test_text1)}') 
    db.post_info("result_table",timer, site_id, "cosuv-parus-test", test_status1, test_text1)
    try:
        driver.execute_script("window.scrollTo(0,300)","")
        name_order = driver.find_element(By.CLASS_NAME, "inp-style1")
        order_mail = driver.find_element(By.CSS_SELECTOR, "div.row.field-email input.inp-style1")
        order_phone = driver.find_element(By.CSS_SELECTOR, "div.row.field-text input.inp-style1:last-child")
        order_comment = driver.find_element(By.CSS_SELECTOR, "div.row.field-textarea textarea.inp-style1")
        name_order.send_keys(test_data[0])
        order_mail.send_keys(test_data[2])
        order_phone.send_keys(test_data[3])
        order_comment.clear()
        order_comment.send_keys(test_data[4])
        time.sleep(1)
        driver.execute_script("window.scrollTo(0,500)","")
        orange_btn = driver.find_element(By.CLASS_NAME, "orange")
        test_status2, test_text2 = True, "Flag-parus_cosuv_constructor_order - OK"
        ActionChains(driver).move_to_element(orange_btn).click().perform()
    #-------------отправка заказа не дописана ---------------------------
    except Exception as error:
        test_status2, test_text2 = False, 'Flag-parus_cosuv_constructor_order - Error'
        logging.error("Error in Flag_parus Cosuv'Constructor-order " + str(error))
    finally:
        driver.quit()
  
    db.post_info("result_table",timer, site_id, "cosuv-send-test", test_status2, test_text2)
    logging.info(f'{timer}-{(test_text2)}') 


def main():
    constructor_test()


if __name__ == '__main__':
      main()