import datetime
import logging
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from sqliter import SQLiter
from config import url_d, test_data, foto_url, scr_file, db_path, chrome_options

logging.basicConfig(level=logging.INFO)
db = SQLiter(db_path)

driver = webdriver.Chrome(options=chrome_options)

timer = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
site_id= 2


def winder_test():
    driver.get(url=url_d['winder_main'])
    driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    driver.implicitly_wait(5)
    try:
        time.sleep(1)
        test = driver.find_element(By.XPATH, "/html/body/div[11]/div/form/div/div/div[2]/div/div[1]/input")
        phone_field = driver.find_element(By.XPATH, "/html/body/div[11]/div/form/div/div/div[2]/div/div[2]/input")
        email_form = driver.find_element(By.XPATH, "/html/body/div[11]/div/form/div/div/div[2]/div/div[3]/input")
        fil_field = driver.find_element(By.CSS_SELECTOR, "div.qq-upload-button-selector.qq-upload-button input")
        test.send_keys(f"{test_data[0]} {test_data[1]}") 
        phone_field.send_keys(test_data[3])
        email_form.send_keys(test_data[2])
        fil_field.send_keys(str(foto_url))
        fil_field = driver.find_element(By.CSS_SELECTOR, "div.qq-upload-button-selector.qq-upload-button input")
        upload_tr = driver.find_element(By.XPATH, "/html/body/div[11]/div[1]/form/div/div/div[3]/div/div/ul/li")
        test_text = "qq-file-id-0"
        test_st = upload_tr.get_attribute("class").split(" ")
        if test_text in test_st:
            test_status = True
        #print(test_st)
        time.sleep(3)
        test_text = "Winder_order_form - OK"
        sub_btn =driver.find_element(By.CLASS_NAME, "submit-order")
        #sub_btn.click()
        #----- От значения time ниже зависит отправится ли форма заказа. ПРИ == 5 ОТПРАВКА ИДЕТ!
        time.sleep(5)
        driver.save_screenshot(scr_file)
   
    except Exception as error:
        test_status = False
        test_text = 'Winder_order_form - Error'
        logging.error("Error in 'send-order block' Flag-winder " + str(error))  
    finally:
        driver.close()

    db.post_info("result_table",timer, site_id, 'winder-order',test_status, test_text)
    loginfo = f'{timer}-{str(test_text)}' 
    logging.info(loginfo)


def main():
    winder_test()


if __name__ == '__main__':
      main()