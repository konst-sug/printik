import logging
import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from sqliter import SQLiter

from config import chrome_options, url_d, test_data, site_id, foto_url, db_path


driver = webdriver.Chrome(options=chrome_options)

logging.basicConfig(level=logging.INFO)

db = SQLiter(db_path)
timer = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def index_test(send_status=False):
    driver.get(url=url_d['kaz'])
    driver.implicitly_wait(10)
    action = ActionChains(driver)
    popup = driver.find_element(By.CSS_SELECTOR, "span[class='button']")
    popup.click()
    
    menu=driver.find_element(By.CSS_SELECTOR, "nav[class='menu-header-top']")
    menu.find_element(By.XPATH, "//*[@id='online-editor']").click()
    test_status1 = False
    test_text1 = 'Print-na-tkani.kz_constructor_test - ?'
    popup = driver.find_element(By.CLASS_NAME, "popup")
    popup.find_element(By.CLASS_NAME,"close_window").click()
    # ----------------------constructor + order test ------------------
    try:
        #ActionChains(driver).move_by_offset(250,250).click().perform()
        driver.execute_script("window.scrollTo(0, 860)","")
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
        action.move_to_element(color).click()
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, 1200)","")
        time.sleep(10)
        # test = driver.find_element(By.CSS_SELECTOR, "input[name='surname']")
        # test.send_keys(test_data[1]) 
        # test = driver.find_element(By.CSS_SELECTOR, "input[name='name']")
        # test.send_keys(test_data[0]) 
        # test = driver.find_element(By.CSS_SELECTOR, "input[name='phone']")
        # test.send_keys(test_data[3]) 
        # test = driver.find_element(By.CSS_SELECTOR, "input[name='email']")
        # test.send_keys(test_data[2]) 
        # test = driver.find_element(By.CSS_SELECTOR, "select[name='delivery']")
        # test.click()
        # test.send_keys("СДЭК до адреса")
        # test = driver.find_element(By.CSS_SELECTOR, "select[name='item-type']")
        # test.send_keys("Баннер")
        # fil_field = driver.find_element(By.CSS_SELECTOR, "div.qq-upload-button-selector.qq-upload-button input")
        # fil_field.send_keys(foto_url)
        # fil_field = driver.find_element(By.CLASS_NAME, "qq-upload-list-selector")
        # upload_success = fil_field.find_elements(By.TAG_NAME, "li")[0]
        # test_text = "qq-file-id-0"
        # test_st = upload_success.get_attribute("class").split(" ")
        # print(test_st)
        # if test_text in test_st:
        #     test_status1 = True
        # loginfo = f'{timer} printkz uploadFile test {str(test_status1)}' 
        # logging.info(loginfo)    
        # test = driver.find_element(By.CSS_SELECTOR, "textarea[name='comment']")
        # test_text1 = "printkz uploadFile test - OK"
        # test.send_keys(test_text1)
        # driver.execute_script("window.scrollTo(0,550)","")
        # sub_btn =driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
        # #sub_btn.click()
        # #----- От значения time ниже зависит отправится ли форма заказа. ПРИ == 5 ОТПРАВКА ИДЕТ!
        # time.sleep(1)
        # test_status2 = True
        # test_text2 = "printKz order form test -OK"
        #--- клик на кнопку отправить заказ отключен -----
    except Exception as error:
        test_status1, test_text1 = False, "'Print-na-tkani.kz_constructor_test - Error'"
        logging.error("Error in printKz order block " + str(error))   
    finally:
         driver.close()
        
    loginfo = f'{timer} printkz order test {str(test_text1)}' 
    logging.info(loginfo)
    db.post_info("result_table",timer, site_id, 'kz-constructor-test',test_status1, test_text1)
    # db.post_info("result_table",timer, site_id, 'kz- order-test', test_status2, test_text2) 


def main():
    index_test()


if __name__ == '__main__':
      main()