import logging
import time
import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from sqliter import SQLiter
from config import url_d, test_data, db_path, chrome_options

logging.basicConfig(level=logging.INFO)
db = SQLiter(db_path)

driver = webdriver.Chrome(options=chrome_options)

timer = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
site_id= 2


def flag_test():
    driver.get(url=url_d['winder_main'])
    cnt_btn = driver.find_element(By.CLASS_NAME,"btn-order_width_xl")
    cnt_btn.click()
    time.sleep(2)
    driver.implicitly_wait(5)
    try:
        cnt_fl = driver.find_element(By.CLASS_NAME, "shop-q")
        cnt_fl.send_keys("5")
        step_2 = driver.find_element(By.ID, "step-2")
        step_2.click()
        h_flag = driver.find_element(By.CLASS_NAME, "height_flag")
        h_flag.click()
        step_3 = driver.find_element(By.ID, "step-3")
        step_3.click()
        h_flag = driver.find_element(By.CLASS_NAME, "form_flag")
        h_flag.click()
        step_3 = driver.find_element(By.ID, "step-4")
        step_3.click()
        h_flag = driver.find_element(By.CLASS_NAME, "size_flag")
        h_flag.click()
        step_3 = driver.find_element(By.ID, "step-5")
        step_3.click()
        h_flag = driver.find_element(By.CLASS_NAME, "type_print")
        h_flag.click()
        step_3 = driver.find_element(By.ID, "step-6")
        step_3.click()
        h_flag = driver.find_element(By.CSS_SELECTOR, "div[price='5400']")
        h_flag.click()
        driver.save_screenshot("screen-order.png")
        step_2 = driver.find_element(By.CLASS_NAME, "total-calculator")
        step_2.click()
        time.sleep(3)
        test_status1, test_text1 = True, "Winder_flag_calculator - OK"
    except Exception as error:
                test_status1, test_text1 = False, 'Winder_flag_calculator - Error'
                logging.error("Error in Winder_flag_calculator" + str(error))
               
    logging.info(f'{timer}-{str(test_text1)}')
    try:  
        name_order = driver.find_element(By.CLASS_NAME, "button-calculator")
        name_order.click()
        order_name = driver.find_element(By.CSS_SELECTOR, "div.field-text input#inp-name.inp-style1")
        order_phone = driver.find_element(By.CSS_SELECTOR, "div.field-text input#inp-phone.inp-style1")
        order_mail = driver.find_element(By.CSS_SELECTOR, "div.field-email input#inp-email.inp-style1")
        order_name.send_keys(test_data[0])
        order_phone.send_keys(test_data[3])
        order_mail.send_keys(test_data[2])
        time.sleep(1)
        delivery = driver.find_element(By.ID, "delivery")
        delivery.send_keys("Самовывоз")
        driver.execute_script("window.scrollTo(0,2000)","")
        time.sleep(1)
        area = driver.find_element(By.CSS_SELECTOR, "div.field-textarea textarea#inp-comment.inp-style1")
        ActionChains(driver).move_to_element(area).click().perform()
        area.clear()
        area.send_keys(test_data[4])
        time.sleep(1)
        send = driver.find_element(By.CSS_SELECTOR, "input#form-submit.buttons.order-button")
        driver.execute_script("window.scrollTo(0,2500)","")
        ActionChains(driver).move_to_element(send)
        test_status2, test_text2 = True, "Winder_flag_calculator_order - OK"
        #driver.execute_script("alert('SUBMIT FIND')")
       #---- для отправки заказа применить click к элементу send ---------
        time.sleep(3)
        #send.click()
        
    except Exception as error:
           test_status2, test_text2 = False, "Winder_flag_calculator_order - Error"
           logging.error("Error in Winder_flag_calculator_order - OK " + str(error))
    finally:
        driver.quit()
    db.post_info("result_table",timer, site_id, 'winder-flag-calculator',test_status1, test_text1)
    db.post_info("result_table",timer, site_id, 'winder-flag-calculator-order',test_status2, test_text2)
    logging.info(f'{timer}-{str(test_text2)}')


def main():
    flag_test()


if __name__ == '__main__':
      main()