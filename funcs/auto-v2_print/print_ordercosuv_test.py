import datetime
import logging
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from sqliter import SQLiter
from config import test_data, foto_url, scr_file, test_phone, url_d, db_path, chrome_options

logging.basicConfig(level=logging.INFO)

driver = webdriver.Chrome(options=chrome_options)
timer = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
db = SQLiter(database=db_path)
site_id = 1


def main_test():
    driver.get(url=url_d['print_main'])
    driver.implicitly_wait(10)
    time.sleep(1)
    try:
        driver.find_element(By.CLASS_NAME, "callback-button").click()
        time.sleep(0.5)
        driver.find_element(By.CLASS_NAME, "callback-input").send_keys(test_phone)
        #---------- отправка номера для связи закомментирована ----------
        #driver.find_element(By.CLASS_NAME, "callback-call").click()
        ActionChains(driver).move_by_offset(0,50).click().perform()
        test_res1 = True
        test_text1 = "Printnatkani_call_me test - OK"
    except Exception as error:
        test_res1 = False
        test_text1 = "Printnatkani_call_me test - Error"
        logging.error(str(error))
    logging.info(f'{timer}-{(test_text1)}')     
    try:
        driver.find_element(By.CLASS_NAME, "order").click()
        driver.execute_script("window.scrollTo(0,480)","")
        driver.find_element(By.CSS_SELECTOR, "input[name='surname']").send_keys(test_data[1])
        driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys(test_data[0])
        driver.find_element(By.CSS_SELECTOR, "input[name='phone']").send_keys(test_data[3])
        driver.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys(test_data[2])
        driver.find_element(By.CSS_SELECTOR, "select[name='delivery']").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, "select[name='delivery']").click()
        driver.find_element(By.CSS_SELECTOR, "option[value='1']").click()
        #driver.find_element(By.CSS_SELECTOR, "select[name='item-type']").click() 
        time.sleep(1)
        #driver.find_element(By.CSS_SELECTOR, "select[name='item-type']").click() 
        # driver.find_element(By.CSS_SELECTOR, "option[text()='Баннер']").click()
        driver.find_element(By.CSS_SELECTOR, "input[name='qqfile']").send_keys(str(foto_url))
        driver.find_element(By.CSS_SELECTOR, "textarea[name='comment']").send_keys(test_data[4])
        driver.execute_script("window.scrollTo(0,480)","")
        submit = driver.find_element(By.ID, "form-submit")
        test_res2 = True
        test_text2 = "Printnatkani_order_form - OK"
        time.sleep(.5)
    except Exception as error:
        test_res2 = False
        test_text2 = "Printnatkani_order_form - Error!"
        logging.error(str(error))
    logging.info(f'{timer}-{(test_text2)}')   
    try:
        driver.get(url=url_d['print_cosuv'])
        driver.implicitly_wait(5)
        time.sleep(3)
        driver.execute_script("window.scrollTo(0,2900)","")
        driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))
        app = driver.find_element(By.CLASS_NAME, "app")
        app.find_element(By.CLASS_NAME, "base").click()
        popup = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[2]")
        popup.find_elements(By.CLASS_NAME,"item")[3].click()
        driver.find_element(By.CLASS_NAME, "text").click()
        driver.find_element(By.CLASS_NAME, "orange").click()
        time.sleep(2)
        test_res3 = True
        test_text3 = "Printnatkani_Cosuv_constructor  - OK"
    except Exception as error:
        test_res3 = False
        test_text3 = "Printnatkani_Cosuv_constructor  - Error"
        logging.error("Error in Cosuv constructor printnatkani: " + str(error))         
    finally:
        driver.close()
    
    logging.info(f'{timer}-{str(test_text2)}')  
    logging.info(f'{timer}-{str(test_text3)}')    
    db.post_info("result_table",timer, site_id, 'call-button', test_res1,test_text1)
    db.post_info("result_table",timer, site_id, 'send-order', test_res2,test_text2)
    db.post_info("result_table",timer, site_id, 'cosuv-constructor', test_res3, test_text3)


def main():
    main_test()
    

if __name__ == '__main__':
    main()    