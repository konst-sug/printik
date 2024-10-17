import logging
import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from sqliter import SQLiter
from config import chrome_options, test_data, site_id, foto_url, db_path, url_d

logging.basicConfig(level=logging.INFO)

driver = webdriver.Chrome(options=chrome_options)
db = SQLiter(db_path)
timer = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def index_test(send_status=False):
    driver.get(url=url_d['kaz'])
    time.sleep(1)
    popup = driver.find_element(By.CSS_SELECTOR, "span[class='button']")
    driver.implicitly_wait(5)
    popup.click()
    menu=driver.find_element(By.CSS_SELECTOR, "nav[class='menu-header-top']")
    menu.find_element(By.XPATH, "//*[@id='custom-make-order']").click()
    test_status1 =False
    test_text1 = 'Print-na-tkani.kz_uploadFile_test - ?'
    # ----------------------send order test ------------------
    try:
        #ActionChains(driver).move_by_offset(250,250).click().perform()
        driver.execute_script("window.scrollTo(0,520)","")
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
        test.send_keys("СДЭК до адреса")
        test = driver.find_element(By.CSS_SELECTOR, "select[name='item-type']")
        test.send_keys("Баннер")
        fil_field = driver.find_element(By.CSS_SELECTOR, "div.qq-upload-button-selector.qq-upload-button input")
        fil_field.send_keys(str(foto_url))
        test = driver.find_element(By.CSS_SELECTOR, "textarea[name='comment']")
        fil_field = driver.find_element(By.CLASS_NAME, "qq-upload-list-selector")
        upload_success = fil_field.find_elements(By.TAG_NAME, "li")[0]
        test_text = "qq-file-id-0"
        test_st = upload_success.get_attribute("class").split(" ")
        #print(test_st)
        if test_text in test_st:
            test_status1 = True
        loginfo = f'{timer}-{str(test_text1)}' 
        logging.info(loginfo)    
        
        test_text1 = "Print-na-tkani.kz_uploadFile_test - OK"
        test.send_keys(test_text1)
        driver.execute_script("window.scrollTo(0,550)","")
        sub_btn =driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
        #sub_btn.click()
        #----- От значения time ниже зависит отправится ли форма заказа. ПРИ == 5 ОТПРАВКА ИДЕТ!
        time.sleep(3)
        test_status2 = True
        test_text2 = "Print-na-tkani.kz_order_test - OK"
        #--- клик на кнопку отправить заказ отключен -----
    except Exception as error:
        test_status2, test_text2 = False, "Print-na-tkani.kz_order_test - Error"
        logging.error("Error in printKz order block " + str(error))   
    finally:
        driver.quit()
        
    loginfo = f'{timer}-{str(test_text2)}' 
    db.post_info("result_table",timer, site_id, 'kz-uploadFile-test',test_status1, test_text1)
    db.post_info("result_table",timer, site_id, 'kz- order-test', test_status2, test_text2) 


def main():
    index_test()


if __name__ == '__main__':
      main()