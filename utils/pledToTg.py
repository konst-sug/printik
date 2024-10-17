import time
import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from config_data.config_one_test import foto_url,update_path
from utils import get_settings


logging.basicConfig(level=logging.INFO)


# --------------------fotopled order test -----------------------
def pledrOrder_to_tg(driver, url: list ,test_data: list, send_status: bool) -> list:
    '''Для проверки через телеграм бота'''
    timer, res_file = get_settings(update_path)

    try:
        driver.get(url=url[12])
        driver.delete_all_cookies()
        driver.implicitly_wait(10)
        time.sleep(1)
        driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        close_click = driver.find_element(By.CSS_SELECTOR, "span[class='button']")
        close_click.click()
        time.sleep(1)
    except Exception as error:
        logging.error(str(error))    
    try:
        driver.get(url=url[13])
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
        
        test = driver.find_element(By.CSS_SELECTOR, "input[id='form-submit']")
    #----- От значения time ниже зависит отправится ли форма заказа. ПРИ == 1 ОТПРАВКА ИДЕТ! оТКЛЮЧЕНО!!
        if send_status:
            test.click()
        time.sleep(2)    
        driver.save_screenshot(res_file)
        test_status1 = True
        test_text1 = "Fotopled_order_test - OK" 
    except Exception as error:
        test_status1 = False
        test_text1 = "Fotopled_order_test - Error" 
        logging.error("Error in 'Fotopled send-order block'" + str(error))
    
    logging.info(f'{timer}-{str(test_text1)}')
    return timer, test_status1, test_text1, res_file


 # --------------------fotopled constructor test -----------------------
def pledConstr_to_tg(driver, url: list ,test_data: list, send_status: bool) ->list:
    '''Для проверки через телеграм бота'''
    timer, res_file = get_settings(update_path)
    
    try:
        driver.get(url=url[15])
        driver.delete_all_cookies()
        driver.implicitly_wait(5)
        test_text2 = ""
        driver.execute_script("window.scrollTo(0,650)","")
        driver.find_element(By.ID, "step-1").click()
        driver.find_element(By.ID, "5").click()
        time.sleep(1)
        driver.find_element(By.ID, "step-13").click()
        razm = driver.find_element(By.ID, "146")
        razm.find_element(By.CLASS_NAME,"param-title").click()
        time.sleep(1)
        upload = driver.find_element(By.CLASS_NAME, "step-5-content")
        upload.find_element(By.ID, "dropzone-0")
        driver.find_element(By.CLASS_NAME, "total-calculator").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//span[text()='Добавить картинку']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//span[text()='Добавить надпись']").click()
        test_status1 = True
        test_text1 = "Fotopled_constructor_test - OK"
        time.sleep(1)
        driver.execute_script("window.scrollTo(0,1300)","")
        hover = driver.find_element(By.XPATH, "//span[text()='Помощь дизайнера']")
        ActionChains(driver).move_to_element(hover).click_and_hold().perform()
        hover = driver.find_element(By.CLASS_NAME, "ui-tooltip-content")
        hover.click()
        driver.find_element(By.ID, "to-order").click()
        modal = driver.find_element(By.ID, "order-form-calc")
        modal.find_element(By.ID, "senderName").send_keys(test_data[0])
        modal.find_element(By.ID, "senderMail").send_keys(test_data[2])
        modal.find_element(By.ID, "senderPhone").send_keys(test_data[3])
        modal.find_element(By.ID, "delivery").send_keys(test_data[5])
        modal = driver.find_element(By.ID, "form-submit")
        logging.info(f'Order form constructor {modal.is_displayed()}')
        time.sleep(1)
        if send_status:
            modal.click()
        test_status2 = True
        test_text2 = "Fotopled_constructor_order - OK "
    except Exception as error:
        test_status1, test_status2, test_text2 = False, False,'Fotopled_constructor_order - Error'
        logging.error("Error in sozdat-fotokollazh-online" + str(error))          
    
    logging.info(f'{timer}-{str(test_text1)}')
    loginfo = f'{timer}-{str(test_text2)}' 
    logging.info(loginfo)  
    return timer, test_status1, test_text1, test_status2, test_text2
    

#--------------------- fotopled Cosuv test --------------------------------------
def pledCosuv_to_tg(driver, url: list ,test_data: list, send_status: bool) ->list:
    '''Для проверки через телеграм бота'''
    timer, res_file = get_settings(update_path)
    
    try:
        driver.get(url=url[14])
        driver.delete_all_cookies()
        driver.implicitly_wait(8)
        driver.execute_script("window.scrollTo(0,650)","")
        close_cookie(driver)   
        driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))
        # up_butn = driver.find_element(By.CSS_SELECTOR, "div.app nav ul li.btn.icon.text")
        up_butn = driver.find_element(By.CSS_SELECTOR," .app > nav:nth-child(1)")
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, "li[class='btn icon text']").click()
        ActionChains(driver).move_to_element(up_butn).click(up_butn).perform()
        up_butn.click()
        time.sleep(1)
        text_area = driver.find_element(By.CSS_SELECTOR, "textarea[class='inp-style1']")
        text_area.click()
        text_area.clear()
        text_area.send_keys("test data line")
        time.sleep(1)
        ActionChains(driver).move_by_offset(150,150).click().perform()
        ord_btn = driver.find_element(By.CSS_SELECTOR, "li[data-lang='78']")
        ord_btn.click()
        test_status1, test_text1 = True, "Fotopled_cosuv_block - OK"
    except Exception as error:
            test_status1 = False
            test_text1 = "Fotopled_cosuv_block - Error"
            logging.error("Error in 'upload-block' in the driver object block " + str(error))
    logging.info(f'{timer}-{str(test_text1)}')         
    try:
        name_order = driver.find_element(By.CLASS_NAME, "inp-style1")
        order_mail = driver.find_element(By.CSS_SELECTOR, "div.row.field-email input.inp-style1")
        order_phone = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/form/div[1]/div[3]/input")
        order_comment = driver.find_element(By.CSS_SELECTOR, "div.row.field-textarea textarea.inp-style1")
        name_order.send_keys(test_data[0])
        order_mail.send_keys(test_data[2])
        order_phone.send_keys(test_data[3])
        order_phone = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/form/div[1]/div[4]/input")
        order_phone.clear()
        order_comment.clear()
        order_phone.send_keys('my_adress')
        order_comment.send_keys(test_data[4])
        time.sleep(1)
        driver.execute_script("window.scrollTo(0,550)","")
        orange_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        ActionChains(driver).move_to_element(orange_btn)
        logging.error(orange_btn.is_enabled())
        if send_status:
            orange_btn.click()
    #    driver.execute_script("alert('submit is ready')")
    #    alert = driver.switch_to.alert
    #    alert.accept()
        test_status2, test_text2 = True, "Fotopled Cosuv order - OK"
    except Exception as error:
           test_status2, test_text2 = False, "Fotopled Cosuv order - Error"
           logging.error("Error in Fotopled Cosuv order" + str(error))
    
    logging.info(f'{timer}-{str(test_text2)}')
    return timer, test_status1, test_text1, test_status2, test_text2
    

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
