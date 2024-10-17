import logging
import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from sqliter import SQLiter

from config import test_data, site_id, url_d, chrome_options, db_path

logging.basicConfig(level=logging.INFO)

driver = webdriver.Chrome(options=chrome_options)
db = SQLiter(database=db_path)
timer = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def index_test(send_status = False):
    time.sleep(1)
    driver.get(url=url_d['parus_main'])
    driver.implicitly_wait(5)
    # -----------------------callback test ----------------------
    try:
        test = driver.find_element(By.CLASS_NAME, "make-call-button")
        test.click()
        phone_field = driver.find_element(By.CLASS_NAME, "callback-input")
        submit_form = driver.find_element(By.CLASS_NAME, "callback-call")
        phone_field.send_keys(test_data[3])
        call_button_res = submit_form.is_enabled()
        text_call_button = "Flag-parus_call_me_test - OK"
        #submit_form.click()
    except Exception as error:
        call_button_res = False
        text_call_button = "Flag-parus_call_me_test - Error"
        logging.error("Error in Flag-parus 'call-me-block' " + str(error))   
    logging.info(f'{timer}-{(text_call_button)}') 
    db.post_info("result_table",timer, site_id, 'call-button',call_button_res,text_call_button)
    # ----------------------send order test ---------------------
    try:
        ActionChains(driver).move_by_offset(250,250).click().perform()
        time.sleep(1)
        button = driver.find_element(By.CLASS_NAME, "make-order-button")
        button.click()
        name = driver.find_element(By.XPATH, '/html/body/div[11]/div/div/div[1]/form/div[1]/div[1]/input')
        sname = driver.find_element(By.XPATH, "/html/body/div[11]/div/div/div[1]/form/div[1]/div[2]/input")
        e_mail = driver.find_element(By.XPATH, "/html/body/div[11]/div/div/div[1]/form/div[2]/div[1]/input")
        phone_name = driver.find_element(By.XPATH, "/html/body/div[11]/div/div/div[1]/form/div[2]/div[2]/input")
        comment = driver.find_element(By.XPATH, "/html/body/div[11]/div/div/div[1]/form/div[3]/div/textarea")
        submit_button = driver.find_element(By.CLASS_NAME,"questions__button")
        #print("Element is visible? " + str(name.is_displayed()))
        #print(submit_button.is_enabled())
        ActionChains(driver).move_to_element(name).click(name).perform()
        name.send_keys(test_data[0])
        sname.send_keys(test_data[1])
        e_mail.send_keys(test_data[2])
        phone_name.send_keys(test_data[3])
        comment.send_keys(test_data[4])
        test_status, test_text = True, "Flag-parus_order_test - OK"
        time.sleep(1)
        #--- клик на кнопку отправить заказ не дописан -----
    except Exception as error:
        test_text = "Flag-parus_order_test - Error"
        test_status = False
        logging.error("Error in make order block " + str(error))
        
    finally:
        driver.quit()
    db.post_info("result_table",timer, site_id, 'Flag_parus_send-order',test_status, test_text)
        
    logging.info(f'{timer}-{(test_text)}') 


def main():
    index_test()


if __name__ == '__main__':
      main()