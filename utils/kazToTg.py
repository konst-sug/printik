import time
import datetime
import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from config_data.config_one_test import foto_url, update_path
from utils import get_settings

timebegin = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
logging.basicConfig(level=logging.INFO)


# --------------------print-kaz order test -----------------------
def kazOrder_to_tg(driver, url: list ,test_data: list, send_status: bool) -> list:
    '''Для проверки через телеграм бота
    Адаптировано для запуска тестовых наборов через starter'''

    timer, res_file = get_settings(update_path)
    test_text1 = "Print-na-tkani.kz_uploadFile_test - ?"
    # ----------------------send order test ------------------
    try:
        driver.get(url=url[16])
        driver.delete_all_cookies()
        driver.implicitly_wait(5)
        close_cookie(driver)
        driver.get(url=url[17])
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
        fil_field = driver.find_element(By.CLASS_NAME, "qq-upload-list-selector")
        upload_success = fil_field.find_elements(By.TAG_NAME, "li")[0]
        test_text = "qq-file-id-0"
        test_st = upload_success.get_attribute("class").split(" ")
        #print(test_st)
        if test_text in test_st:
            test_status1, test_text1 = True, "Print-na-tkani.kz_uploadFile_test - OK!"
        loginfo = f'{timer}-{str(test_text1)}' 
        logging.info(loginfo)    
        test = driver.find_element(By.CSS_SELECTOR, "textarea[name='comment']")
        test_text = "Print-na-tkani.kz uploadFile test"
        test.send_keys(test_text)
        time.sleep(.5)
        driver.save_screenshot(res_file)
        driver.execute_script("window.scrollTo(0,550)","")
        sub_btn =driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
        if send_status:
           sub_btn.click()
        #----- От значения time ниже зависит отправится ли форма заказа. ПРИ == 5 ОТПРАВКА ИДЕТ!
        time.sleep(3)
        test_status2 = True
        test_text2 = "Print-na-tkani.kz_order_test - OK!"
    except Exception as error:
        test_status2, test_text2 = False, "Print-na-tkani.kz_order_test - Error"
        logging.error("Error in printKz order block " + str(error))
    logging.info(f'{timer}-{test_text2}')       
    return timer, test_status1, test_text1, test_status2, test_text2, res_file


# --------------------printkaz constructor test -----------------------
def kazConstructor_to_tg(driver, url: list ,test_data: list, send_status: bool) -> list:
    '''Для проверки через телеграм бота
    Адаптировано для запуска тестовых наборов через starter'''
    timer, res_file = get_settings(update_path)
    
    # ----------------------send order test ------------------
    try:
        driver.get(url=url[16])
        driver.delete_all_cookies()
        driver.implicitly_wait(5)
        time.sleep(1)
        action = ActionChains(driver)
        popup = driver.find_element(By.CSS_SELECTOR, "span[class='button']")
        popup.click()
        menu=driver.find_element(By.CSS_SELECTOR, "nav[class='menu-header-top']")
        menu.find_element(By.XPATH, "//*[@id='online-editor']").click()
        test_status1 =False
        test_text1 = 'Print-na-tkani.kz_Constructor not enabled'
        popup = driver.find_element(By.CLASS_NAME, "popup")
        popup.find_element(By.CLASS_NAME,"close_window").click()
        #ActionChains(driver).move_by_offset(250,250).click().perform()
        driver.execute_script("window.scrollTo(0, 870)","")
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
        action.move_to_element(color).click().perform()
        action. move_by_offset(50,10).click().perform()
        action.move_to_element(color).click().perform()
        driver.execute_script("window.scrollTo(0, 1600)","")
        time.sleep(1)
        menu = driver.find_element(By.CSS_SELECTOR, "div[id='left-bottom-menu']")
        menu.find_element(By.CSS_SELECTOR, "div[id='simple-editor']").click()
        driver.find_element(By.CSS_SELECTOR, "li[id='simple-image']").click()
        content = driver.find_element(By.CSS_SELECTOR, "li[class='content']")
        item = content.find_element(By.ID, "8")
        item.find_element(By.CLASS_NAME, "item-bg")
        send_menu = driver.find_element(By.CSS_SELECTOR, "ul[id='third-menu-part']")
        send_menu.find_element(By.TAG_NAME, "a")
        hover = send_menu.find_element(By.XPATH, "//span[text()='Сделайте за меня']")
        hover.click()
        time.sleep(1)
        test_status1 = True
        test_text1 = "Print-na-tkani.kz_constructor - OK"
        time.sleep(1)
    except Exception as error:
        test_status1, test_text1 = False, 'Print-na-tkani.kz_constructor - Error'
        logging.error("Error in Printnatkani kaz Constructor " + str(error))
    logging.info(f'{timer}-{str(test_text1)}')
    try:    
        modal = driver.find_element(By.ID, "order-form-calc")
        modal.find_element(By.ID, "senderName").send_keys(test_data[0])
        modal.find_element(By.ID, "senderMail").send_keys(test_data[2])
        modal.find_element(By.ID, "senderPhone").send_keys(test_data[3])
        modal.find_element(By.ID, "delivery").send_keys(test_data[5])
        modal.find_element(By.ID, "senderAddress").send_keys(test_data[5])
        modal = driver.find_element(By.ID, "form-submit")
        logging.info(f'Submit form kaz {modal.is_displayed()}')
        time.sleep(1)
        if send_status:
            modal.click()
            time.sleep(3)
        driver.save_screenshot(res_file)
        test_status2 = True
        test_text2 = "Print-na-tkani.kz_constructor_order - OK "
        #--- клик на кнопку отправить заказ отключен -----
    except Exception as error:
        test_status2, test_text2 = False, 'Print-na-tkani.kz_constructor_order - Error' 
        logging.error("Error in Printnatkani-kaz constructor order " + str(error))   
        
    loginfo = f'{timer} {str(test_text2)}' 
    logging.info(loginfo)
    return timer, test_status1, test_text1, test_status2, test_text2, res_file
        

def close_cookie(driver):
    """Close cookie info window"""
    try:
        close_click = driver.find_element(By.CSS_SELECTOR, "span[class='button']")
        driver.implicitly_wait(10)
        close_click.click()
        time.sleep(1)
        test_status1, test_text1 = True, 'Window closed'
    except Exception as error:
        test_status1 = False
        test_text1 = str(error)
        logging.error(str(error))
    return test_status1, test_text1 