import logging
import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from sqliter import SQLiter

from config import test_data, url_d, chrome_options, db_path, foto_url

logging.basicConfig(level=logging.INFO)

driver = webdriver.Chrome(options=chrome_options)
db = SQLiter(database=db_path)
timer = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
site_id= 1
send_status= False


def print_constructor_test():
    # --------------------constructor order test -----------------------
    driver.get(url=url_d['print_const'])
    driver.implicitly_wait(5)
    time.sleep(1)
    action = ActionChains(driver)
    popup = driver.find_element(By.CSS_SELECTOR, "div[id='popups']")
    popup.find_element(By.CLASS_NAME, "close_window").click()
    test_status1 =False
    test_text1 = ''
    try:
        driver.execute_script("window.scrollTo(0, 790)","")
        menu = driver.find_element(By.ID, "left-top-menu")
        button = menu.find_element(By.CLASS_NAME,"menu-button")
        button =button.find_element(By.CLASS_NAME, "menu-icon")
        action = ActionChains(driver)
        action.move_to_element(button).perform()
        button.click()
        driver.find_element(By.CLASS_NAME, "item").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, "div[class='menu-icon menu-6']").click()
        time.sleep(1)
        driver.find_element(By.ID, "35").click()
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR, "div[class='menu-icon menu-12']").click()
        time.sleep(1)
        driver.find_element(By.ID, "434").click()
        time.sleep(3)
        color = driver.find_element(By.CSS_SELECTOR, "div[class='menu-icon menu-30']")
        action.move_to_element(color).perform()
        color.click()
        action.move_by_offset(400,400).click().perform()
        #action.move_by_offset(400,900).click().perform()
        time.sleep(1)
      
        action.move_to_element(color).click()
        time.sleep(1)
        upload = driver.find_element(By.CSS_SELECTOR, "li[class='menu-button']")
        upload = driver.find_element(By.CSS_SELECTOR, "div[id='uploader-container']")
        #print("Element is visible? " + str(upload.is_displayed()))
        qqfile = upload.find_element(By.CSS_SELECTOR, "div[class='qq-uploader-selector qq-uploader qq-gallery']")
        #print("Element is visible? " + str(qqfile.is_displayed()))
        time.sleep(3)
        upload = driver.find_element(By.CSS_SELECTOR, "div[id='uploader-bottom']")
        #print("Element is visible? " + str(upload.is_displayed()))
        upload = driver.find_element(By.CSS_SELECTOR,"div[class='qq-upload-list-selector qq-upload-list']")
        #print("Element is visible? " + str(upload.is_displayed()))
        upload.send_keys(foto_url)
        test_status1, test_text1 = True, "Printnatkani_constructor - OK"
    except Exception as error:
        test_status2, test_text2 = True, "Printnatkani_constructor - Error"
        logging.error(str(error))
    logging.info(f'{timer}-{str(test_text1)}')    
    try:
        driver.execute_script("window.scrollTo(0, 1200)","")
        time.sleep(1)
        send = driver.find_element(By.CSS_SELECTOR, "input#form-submit.buttons.order-button")
        driver.execute_script("window.scrollTo(0,2500)","")
        ActionChains(driver).move_to_element(send)
        time.sleep(1)
        if send_status:
            send.click()
            alert = driver.find_element(By.CLASS_NAME, "modal-content")
            sub_btn = alert.find_element(By.CSS_SELECTOR, "button[type='button']")
            sub_btn.click()
            
        test_status2, test_text2 = True, "Printnatkani_constructor_order - OK"        
    except Exception as error:
        test_status2, test_text2 = False, "Printnatkani_constructor_order - Error"
        logging.error("Error in 'Printnatkani_constructor_order " + str(error))       
    finally:
        driver.quit()     
    db.post_info("result_table", timer, site_id, 'flag-calculator',test_status1,test_text1)
    
    db.post_info("result_table", timer, site_id, "flag-order", test_status2, test_text2)
    logging.info(f'{timer}-{str(test_text2)}') 


def main():
    print_constructor_test()


if __name__ == '__main__':
      main()       