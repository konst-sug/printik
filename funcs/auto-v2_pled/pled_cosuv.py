import datetime
import logging
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from sqliter import SQLiter

from config import test_data, db_path, url_d, chrome_options

logging.basicConfig(level=logging.INFO)

driver = webdriver.Chrome(options=chrome_options)
timer = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
db = SQLiter(db_path)
site_id = 4


def constructor_test(send_status=False):
    # --------------------constructor order test -----------------------
    driver.get(url=url_d['pled_cosuv'])
    driver.implicitly_wait(5)
    driver.execute_script("window.scrollTo(0,650)","")
    time.sleep(1)
    try:
        close_click = driver.find_element(By.CSS_SELECTOR, "span[class='button']")
        close_click.click()
        time.sleep(1)
    except Exception as error:
        test_status1 = False
        test_text1 = str(error)
        logging.error(str(error))    
    try:
        driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))
        up_butn = driver.find_element(By.CSS_SELECTOR, "div.app nav ul li.btn.icon.text")
        ActionChains(driver).move_to_element(up_butn).click(up_butn).perform()
        up_butn.click()
        time.sleep(3)
        text_area = driver.find_element(By.CSS_SELECTOR, "textarea[class='inp-style1']")
        text_area.click()
        text_area.clear()
        text_area.send_keys("test text line")
        time.sleep(3)
        ActionChains(driver).move_by_offset(150,150).click().perform()
        ord_btn = driver.find_element(By.CSS_SELECTOR, "li[data-lang='78']")
        ord_btn.click()
        test_status1, test_text1 = True, "Fotopled_cosuv_test - OK"
    except Exception as error:
        test_status1 = False
        test_text1 = "Fotopled_cosuv_test - Error"
        logging.error("Error in 'Fotopled_cosuv_test block " + str(error))
    logging.info(f'{timer}-{str(test_text1)}') 
    db.post_info("result_table",timer,site_id,"Cosuv block fotopled", test_status1, test_text1)        
    try:
        name_order = driver.find_element(By.CLASS_NAME, "inp-style1")
        order_mail = driver.find_element(By.CSS_SELECTOR, "div.row.field-email input.inp-style1")
        order_phone = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/form/div[1]/div[3]/input")
        order_comment = driver.find_element(By.CSS_SELECTOR, "div.row.field-textarea textarea.inp-style1")
        name_order.send_keys(test_data[0])
        order_mail.send_keys(test_data[2])
        order_phone.send_keys(test_data[3])
        order_phone = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/form/div[1]/div[4]/input")
        order_phone.clear()
        order_comment.clear()
        order_phone.send_keys('my_adress')
        order_comment.send_keys(test_data[4])
        time.sleep(3)
        driver.execute_script("window.scrollTo(0,500)","")
        orange_btn = driver.find_element(By.CLASS_NAME, "orange")
        ActionChains(driver).move_to_element(orange_btn)
    # ----------Для отправки расскомментировать -------------------
        #orange_btn.click()
        test_status2, test_text2 = True, "Fotopled_cosuv_order - OK"
    except Exception as error:
        test_status2, test_text2 = False, "Fotopled_cosuv_order - Error"
        logging.error("Error in Fotopled_cosuv_order" + str(error))
    finally:
        driver.quit()
    
    db.post_info("result_table", timer, site_id,"Cosuv send block fotopled",test_status2,test_text2)
    loginfo = f'{timer}_{str(test_text2)}' 
    logging.info(loginfo)


def main():
    constructor_test()


if __name__ == '__main__':
      main()
