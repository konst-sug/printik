import datetime
import logging
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from config import test_data, db_path, chrome_options, url_d
from sqliter import SQLiter

logging.basicConfig(level=logging.INFO)

driver = webdriver.Chrome(options=chrome_options)
db = SQLiter(db_path)
timer = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
site_id = 4


def index_test(send_status = False):
    driver.get(url=url_d['pled_main'])
    driver.implicitly_wait(5)
    time.sleep(1)
    driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    try:
        close_click = driver.find_element(By.CSS_SELECTOR, "span[class='button']")
        close_click.click()
        time.sleep(1)
    except Exception as error:
        logging.error(str(error))    
    try:
        driver.get(url=url_d['pled_order'])
        test = driver.find_element(By.CSS_SELECTOR, "input[name='surname']")
        test.send_keys(test_data[1]) 
        test = driver.find_element(By.CSS_SELECTOR, "input[name='name']")
        test.send_keys(test_data[0]) 
        test = driver.find_element(By.CSS_SELECTOR, "input[name='phone']")
        test.send_keys(test_data[3]) 
        test = driver.find_element(By.CSS_SELECTOR, "input[name='email']")
        test.send_keys(test_data[2]) 
        test = driver.find_element(By.CSS_SELECTOR, "select[name='delivery']")
        test.click()
        ActionChains(driver).move_by_offset(250,250).click().perform()
        test.send_keys(test_data[5]) 
        test = driver.find_element(By.CSS_SELECTOR, "textarea[name='comment']")
        test.send_keys('Заказ добавлен при помощи автотеста. Не требуется обратного звонка. Удалить после прохождения теста') 
        time.sleep(1)
        driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        driver.save_screenshot("screen1.png")
        test = driver.find_element(By.CSS_SELECTOR, "input[id='form-submit']")
    #----- От значения time ниже зависит отправится ли форма заказа. ПРИ == 1 ОТПРАВКА ИДЕТ! оТКЛЮЧЕНО!!
        #test.click()
        test_status1 = True
        test_text1 = "Fotopled_order_test - OK" 
    except Exception as error:
        test_status1 = False
        test_text1 = "Fotopled_order_test - Error" 
        logging.error("Error in Fotopled_order_test " + str(error))
    logging.info(f'{timer}-{str(test_text1)}')
    db.post_info("result_table",timer,site_id,"pled_orderform_test",test_status1,test_text1)
    #-------------------- pled constructor test ----------------------------- 
    try:
        test_text2 = "Fotopled_constructor_test - ?"
        driver.get(url=url_d['pled_constr'])
        driver.execute_script("window.scrollTo(0,650)","")
        driver.find_element(By.ID, "step-1").click()
        driver.find_element(By.ID, "5").click()
        time.sleep(3)
        driver.find_element(By.ID, "step-13").click()
        razm = driver.find_element(By.ID, "146")
        razm.find_element(By.CLASS_NAME,"param-title").click()
        time.sleep(5)
        upload = driver.find_element(By.CLASS_NAME, "step-5-content")
        upload.find_element(By.ID, "dropzone-0")
        #upload.send_keys("/home/konst/Изображения/i.jpeg")
        driver.find_element(By.CLASS_NAME, "total-calculator").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//span[text()='Добавить картинку']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//span[text()='Добавить надпись']").click()
        test_status2 = True
        test_text2 = "Fotopled_constructor_test - OK"
        time.sleep(1)
        driver.execute_script("window.scrollTo(0,1300)","")
        hover = driver.find_element(By.XPATH, "//span[text()='Помощь дизайнера']")
        ActionChains(driver).move_to_element(hover).click_and_hold().perform()
        hover = driver.find_element(By.CLASS_NAME, "ui-tooltip-content")
        hover.click()
        driver.find_element(By.ID, "to-order").click()
        modal = driver.find_element(By.ID, "order-form-calc")
        modal.find_element(By.ID, "senderName").send_keys("test")
        logging.info(f'Constructor order is visible -{modal.is_displayed()}')
        #---- заполнение формы незакончено ------
        test_status3 = True
        test_text3 = "Fotopled_constructor_order - OK"
        time.sleep(5)
    except Exception as error:
        test_status2, test_status3, test_text3 = False, False, "Fotopled_constructor_order - Error"
        logging.error("Error in sozdat-fotokollazh-online-block" + str(error))      
    finally:
        driver.close()
    loginfo = f'{timer}-{str(test_text2)}' 
    logging.info(loginfo)
    loginfo1 = f'{timer}_{str(test_text3)}' 
    logging.info(loginfo1)     
    
    db.post_info("result_table", timer, site_id,"pled_constructor_test",test_status2,test_text2)
    db.post_info("result_table", timer, site_id, "pled_constructor order_test",test_status3,test_text3)
    

def main():
    index_test()
    

if __name__ == '__main__':
    main()    