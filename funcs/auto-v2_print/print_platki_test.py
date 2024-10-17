import logging
import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from sqliter import SQLiter

from config import test_data, url_d, chrome_options, db_path

logging.basicConfig(level=logging.INFO)

driver = webdriver.Chrome(options=chrome_options)
db = SQLiter(database=db_path)
timer = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
site_id= 1


def platki_constructor_test(send_status=False):
    # --------------------constructor order test -----------------------
    driver.get(url=url_d['print_platki'])
    driver.implicitly_wait(5)
    driver.get('https://printnatkani.ru/izgotovlenie_platkov#raschet')
    time.sleep(2)
    driver.execute_script("window.scrollTo(0,600)","")
    try:
        step_container = driver.find_element(By.ID, "shavl-calculator-wrap")
        selector = driver.find_element(By.XPATH, "/html/body/div[1]/div[5]/div/div[2]/div[3]/div[1]/div/div[2]/div[2]/div/div[1]")
        param = selector.find_elements(By.CLASS_NAME,"param-block")[0]
        param.find_elements(By.TAG_NAME, "select")[0].send_keys("Французский платок (косынка)")
        logging.info(param.is_enabled())
        time.sleep(1)
        logging.info(param.is_enabled())
        time.sleep(10)
        param = driver.find_element(By.XPATH,"/html/body/div[1]/div[5]/div/div[2]/div[3]/div[1]/div/div[2]/div[2]/div/div[1]/div[2]/select")
        param.click()
        param = driver.find_element(By.CSS_SELECTOR, "option[value='1272']")
        param.click()
        param = driver.find_element(By.XPATH,"/html/body/div[1]/div[5]/div/div[2]/div[3]/div[1]/div/div[2]/div[2]/div/div[1]/div[2]/select")
        param.click()
        time.sleep(1)
        param = driver.find_element(By.XPATH,"/html/body/div[1]/div[5]/div/div[2]/div[3]/div[1]/div/div[2]/div[2]/div/div[1]/div[3]/select")
        param.click()
        param = driver.find_element(By.CSS_SELECTOR, "option[value='1264']")
        param.click()
        param = driver.find_element(By.XPATH,"/html/body/div[1]/div[5]/div/div[2]/div[3]/div[1]/div/div[2]/div[2]/div/div[1]/div[3]/select")
        param.click()
        time.sleep(1)
        param = driver.find_element(By.XPATH,"/html/body/div[1]/div[5]/div/div[2]/div[3]/div[1]/div/div[2]/div[2]/div/div[1]/div[4]/select")
        param.click()
        param = driver.find_element(By.CSS_SELECTOR, "option[value='1267']")
        param.click()
        param = driver.find_element(By.XPATH,"/html/body/div[1]/div[5]/div/div[2]/div[3]/div[1]/div/div[2]/div[2]/div/div[1]/div[4]/select")
        param.click()
        time.sleep(.3)
        param = driver.find_element(By.XPATH,"/html/body/div[1]/div[5]/div/div[2]/div[3]/div[1]/div/div[2]/div[2]/div/div[1]/div[5]/select")
        param.click()
        param = driver.find_element(By.CSS_SELECTOR, "option[value='1268']")
        param.click()
        param = driver.find_element(By.XPATH,"/html/body/div[1]/div[5]/div/div[2]/div[3]/div[1]/div/div[2]/div[2]/div/div[1]/div[5]/select")
        param.click()
        param= driver.find_element(By.CSS_SELECTOR, "input[class='shop-quantity']")
        param.send_keys('3')
        logging.info(param.is_enabled())
        #driver.save_screenshot(res_file)
        driver.find_element(By.CSS_SELECTOR, "div[class='total-calculator desctop-total']").click()
        time.sleep(1)
        test_status1, test_text1 = True, 'Printnatkani_Platki_calculator - OK'
    except Exception as error:
        test_status1, test_text1 = False, 'Printnatkani_Platki_calculator - Error'
        logging.error("Error in Printnatkani_Platki_calculator " + str(error))
    logging.info(f'{timer}-{(test_text1)}')     
    db.post_info("result_table",timer, site_id, 'platki-calculator',test_status1,test_text1)

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
        time.sleep(1)
        send = driver.find_element(By.CSS_SELECTOR, "input#form-submit.buttons.order-button")
        #driver.execute_script("window.scrollTo(0,2500)","")
        ActionChains(driver).move_to_element(send)
        time.sleep(1)
        if send_status:
            send.click()
            time.sleep(5)
       
        test_status2, test_text2 = True, "Printnatkani_Platki_calculator_order - OK"        
    except Exception as error:
        test_status2, test_text2 = False, "Printnatkani_Platki_calculator_order - Error"
        logging.error("Error in Printnatkani_Platki_calculator_order " + str(error))        
    logging.info(f'{timer}-{(test_text2)}')    
  
    driver.quit()     
    db.post_info("result_table",timer, site_id, 'platki-calculator',test_status2,test_text2)


def main():
    platki_constructor_test()


if __name__ == '__main__':
      main()       