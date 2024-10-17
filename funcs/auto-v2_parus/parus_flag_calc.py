import logging
import time
import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from sqliter import SQLiter

from config import test_data, db_path, url_d, chrome_options

logging.basicConfig(level=logging.INFO)

driver = webdriver.Chrome(options=chrome_options)
db = SQLiter(db_path)
timer = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
site_id = 3


def form_flag_test(send_status=False):
    driver.get(url=url_d['parus_flag'])
    driver.delete_all_cookies()
    driver.implicitly_wait(10)
    time.sleep(5)
    driver.execute_script("window.scrollTo(0,1500)","") 
    try:
        step_container = driver.find_element(By.CLASS_NAME, "step-container")
        flag_number = step_container.find_element(By.CLASS_NAME, "shop-q")
        time.sleep(.8)
        flag_number.send_keys("1")
        time.sleep(.8)
        step_2 = driver.find_element(By.ID, "step-2")
        step_2.click()
        time.sleep(.8)
        h_flag = driver.find_element(By.CLASS_NAME, "height_flag")
        h_flag.click()
        time.sleep(1)
        step_3 = driver.find_element(By.ID, "step-3")
        step_3.click()
        time.sleep(1)
        h_flag = driver.find_element(By.CLASS_NAME, "form_flag ")
        h_flag.click()
        step_3 = driver.find_element(By.ID, "step-4")
        step_3.click()
        time.sleep(1)
        h_flag = driver.find_element(By.CLASS_NAME, "size_flag")
        h_flag.click()
        step_3 = driver.find_element(By.ID, "step-5")
        step_3.click()
        time.sleep(1)
        h_flag = driver.find_element(By.CLASS_NAME, "type_print")
        h_flag.click()
        step_3 = driver.find_element(By.ID, "step-6")
        step_3.click()
        time.sleep(1)
        h_flag = driver.find_element(By.CSS_SELECTOR, "div[price='2700']")
        h_flag.click()
        time.sleep(1)
        step_2 = driver.find_element(By.CLASS_NAME, "total-calculator")
        step_2.click()
        time.sleep(1)
        submit_button = driver.find_element(By.CLASS_NAME, "button-calculator")
        #print(submit_button.is_enabled())
        test_status1, test_text1 = True, 'Flag-parus_flag_calculator - OK'
    except Exception as error:
        test_status1, test_text1 = True, 'Flag-parus_flag_calculator - Error'
        logging.error("Error in flag order block " + str(error))
    db.post_info("result_table",timer, site_id, 'flag-calculator', test_status1, test_text1)
    logging.info(f'{timer}-{(test_text1)}')

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
        #driver.execute_script("window.scrollTo(0,2000)","")
        time.sleep(1)
        area = driver.find_element(By.CSS_SELECTOR, "div.field-textarea textarea#inp-comment.inp-style1")
        ActionChains(driver).move_to_element(area).click().perform()
        area.clear()
        area.send_keys(test_data[4])
        time.sleep(3)
        send = driver.find_element(By.CSS_SELECTOR, "input#form-submit.buttons.order-button")
        #driver.execute_script("window.scrollTo(0,2500)","")
        ActionChains(driver).move_to_element(send)
        driver.execute_script("window.scrollTo(0,2800)","")
       #---- для отправки заказа применить click к элементу send ---------
        time.sleep(1)
        if send_status:
            send.click()
            alert = driver.find_element(By.CLASS_NAME, "modal-content")
            sub_btn = alert.find_element(By.CSS_SELECTOR, "button[type='button']")
            sub_btn.click()
            logging.info(f'Flag-Parus flag calculator button {sub_btn.is_enabled()}')
        test_status2, test_text2 = True, "Flag-parus_flag_calculator_order - OK"
        time.sleep(3)        
    except Exception as error:
           test_status2, test_text2 = False, "Flag-parus_flag_calculator_order - Error"
           logging.error("Error in Flag-parus_flag_calculator_order " + str(error))    
    logging.info(f'{timer}-{(test_text2)}')        

    driver.quit()     
    db.post_info("result_table",timer, site_id, 'flag-calculator', test_status2, test_text2)


def main():
    form_flag_test()


if __name__ == '__main__':
      main()       