import time
import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from config_data.config_one_test import foto_url, update_path
from utils import get_settings


logging.basicConfig(level=logging.INFO)


# --------------------flagparus order test -----------------------
def parusOrder_to_tg(driver, url: list ,test_data: list, send_status: bool) -> list:
    '''Для проверки через телеграм бота
    Адаптировано для запуска тестовых наборов через starter'''

    timer, res_file = get_settings(update_path)
    try:
        driver.get(url=url[7])
        driver.delete_all_cookies()
        driver.implicitly_wait(5)
        ActionChains(driver).move_by_offset(250,250).click().perform()
        button = driver.find_element(By.CLASS_NAME, "make-order-button")
        button.click()
        name = driver.find_element(By.XPATH, '/html/body/div[11]/div/div/div[1]/form/div[1]/div[1]/input')
        sname = driver.find_element(By.XPATH, "/html/body/div[11]/div/div/div[1]/form/div[1]/div[2]/input")
        e_mail = driver.find_element(By.XPATH, "/html/body/div[11]/div/div/div[1]/form/div[2]/div[1]/input")
        phone_name = driver.find_element(By.XPATH, "/html/body/div[11]/div/div/div[1]/form/div[2]/div[2]/input")
        comment = driver.find_element(By.XPATH, "/html/body/div[11]/div/div/div[1]/form/div[3]/div/textarea")
        submit_button = driver.find_element(By.CLASS_NAME,"questions__button")
        #logging.info("Element is visible? " + str(submit_button.is_displayed()))
        ActionChains(driver).move_to_element(name).click(name).perform()
        name.send_keys(test_data[0])
        sname.send_keys(test_data[1])
        e_mail.send_keys(test_data[2])
        phone_name.send_keys(test_data[3])
        comment.send_keys(test_data[4])
        sub_btn =driver.find_element(By.CLASS_NAME,"questions__button")
        ActionChains(driver).move_to_element(sub_btn).perform()
        #logging.info("Element is visible? " + str(sub_btn.is_displayed()))
        if send_status:
            sub_btn.click()
        test_status1, test_text1 =  True, "Flag-parus_order_test - OK"
        time.sleep(1)
    except Exception as error:
        test_status1, test_text1 =  False, "Flag-parus_order_test - Error"
        logging.error("Error in Flag-parus order test " + str(error))
    logging.info(f'{timer}-{(test_text1)}')    
    return timer, test_status1, test_text1


 # --------------------flagparus cosuv constructor test -----------------------
def parusCosuv_to_tg(driver, url: list ,test_data: list, send_status: bool) ->list:
    '''Для проверки через телеграм бота
    Адаптировано для запуска тестовых наборов через starter'''

    timer, res_file = get_settings(update_path)
    
    try:
        driver.get(url=url[9])
        driver.delete_all_cookies()
        driver.implicitly_wait(7)
        time.sleep(1)
        driver.execute_script("window.scrollTo(0,300)","")
        driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))
        up_butn = driver.find_element(By.XPATH, "/html/body/div/nav/ul/li[12]")
        ActionChains(driver).move_to_element(up_butn).click(up_butn).perform()
        driver.find_element(By.CSS_SELECTOR, "li[class='btn icon text']").click()
        time.sleep(1)
        text_area = driver.find_element(By.XPATH, "/html/body/div/aside/div/div[3]/div/textarea")
        text_area.clear()
        text_area.send_keys("test line\\n")
        ActionChains(driver).move_by_offset(150,150).click().perform()
        ord_btn = driver.find_element(By.XPATH, "/html/body/div[1]/nav/ul/li[15]")
        ord_btn.click()
        test_status1, test_text1 = True, "Flag-parus_cosuv_constructor - OK"
    except Exception as error: 
                test_status1, test_text1 = False, "Flag-parus_cosuv_constructor - Error"
                logging.info(f"Error in parus cosuv test {str(error)}")
    logging.info(f'{timer}-{(test_text1)}')
    try:
        driver.execute_script("window.scrollTo(0,300)","")
        name_order = driver.find_element(By.CLASS_NAME, "inp-style1")
        order_mail = driver.find_element(By.CSS_SELECTOR, "div.row.field-email input.inp-style1")
        order_phone = driver.find_element(By.CSS_SELECTOR, "div.row.field-text input.inp-style1:last-child")
        order_comment = driver.find_element(By.CSS_SELECTOR, "div.row.field-textarea textarea.inp-style1")
        name_order.send_keys(test_data[0])
        order_mail.send_keys(test_data[2])
        order_phone.send_keys(test_data[3])
        order_comment.clear()
        order_comment.send_keys(test_data[4])
        driver.execute_script("window.scrollTo(0,500)","")
        driver.save_screenshot(res_file)
        orange_btn = driver.find_element(By.CLASS_NAME, "orange")
        driver.execute_script("window.scrollTo(0,700)","")
        if send_status:
            orange_btn.click()
        time.sleep(2)    
        test_status2, test_text2 = True, "Flag-parus_cosuv_constructor_order - OK"
        ActionChains(driver).move_to_element(orange_btn).click().perform()
    except Exception as error:
        test_status2, test_text2 = False, "Flag-parus_cosuv_constructor_order - Error"
        logging.info(f'Error in Flag-Parus Cosuv order {str(error)}')
    logging.info(f'{timer}-{(test_text2)}')    
    return timer, test_status1, test_text1, test_status2, test_text2, res_file
    

#--------------------- flag parus Products form test -----------------------
def parusProds_to_tg(driver, url: list ,test_data: list, send_status: bool) ->list:
    '''Для проверки через телеграм бота
    Адаптировано для запуска тестовых наборов через starter'''

    timer, res_file = get_settings(update_path)
   
    try:
        driver.get(url=url[11])
        driver.delete_all_cookies()
        driver.implicitly_wait(10)
        time.sleep(5)
        button = driver.find_element(By.CLASS_NAME, "make-order-button_w").click()
        time.sleep(3)
        modal_w = driver.find_element(By.CLASS_NAME,"modal-body")
        modal = driver.find_element(By.CLASS_NAME, "form-control")
        modal.send_keys("2")
        time.sleep(1)
        row = driver.find_elements(By.CLASS_NAME, "row")
        inp_name = driver.find_element(By.XPATH, "/html/body/div[9]/div/div/div/div[7]/div/div/div[2]/form/div[2]/div[1]/input").send_keys(test_data[1])
        input_email = driver.find_element(By.XPATH, "/html/body/div[9]/div/div/div/div[7]/div/div/div[2]/form/div[2]/div[2]/input").send_keys(test_data[2])
        input_phone = driver.find_element(By.XPATH, "/html/body/div[9]/div/div/div/div[7]/div/div/div[2]/form/div[2]/div[3]/input").send_keys(test_data[3])
        modal = driver.find_element(By.CLASS_NAME, "add-detail-modal").click()
        delivery = driver.find_element(By.TAG_NAME, "select")
        logging.info(f"delivery change label is enable {delivery.is_enabled()}")
        textarea = driver.find_element(By.XPATH, "/html/body/div[9]/div/div/div/div[7]/div/div/div[2]/form/div[3]/div/div[2]/div/textarea")
        ActionChains(driver).move_to_element(textarea).click(textarea).perform()
        textarea.send_keys(test_data[4])
        #driver.execute_script("arguments[0].scrollTop = arguments[1]", modal_w)
        modal = driver.find_element(By.CLASS_NAME, "add-detail-modal").click()
        submit = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        
        if submit.is_enabled() & delivery.is_enabled():
            logging.info("Parus products form OK")
        if send_status:
            submit.click()
            time.sleep(3)
        test_status = True
        test_text = "Flag-parus_products_order - OK"      
    except Exception as error:
        test_status = False
        test_text = "Flag-parus_products_order - Error"
        logging.info(f"Error in Flag-Parus products test {str(error)}")
    logging.info(f'{timer}-{(test_text)}')     
    return  timer, test_status, test_text
    

#--------------------- flag parus constructor test -----------------------
def parusFlag_to_tg(driver, url: list, test_data: list, send_status: bool) -> list:
    '''Для проверки через телеграм бота
    Адаптировано для запуска тестовых наборов через starter'''

    timer, res_file = get_settings(update_path)
    
    try:
        driver.get(url=url[10])
        driver.delete_all_cookies()
        driver.implicitly_wait(10)
        time.sleep(5)
        driver.execute_script("window.scrollTo(0,1500)","") 
        step_container = driver.find_element(By.CLASS_NAME, "step-container")
        flag_number = step_container.find_element(By.CLASS_NAME, "shop-q")
        time.sleep(1)
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
        driver.save_screenshot(res_file)
        logging.info(f'Flag-Parus Calculator button {submit_button.is_enabled()}')
        test_text1 = 'Flag-parus_flag_calculator - OK'
        test_status1 =True
    except Exception as error:
        test_status1, test_text1 = False, "Flag-parus_flag_calculator - Error"
        logging.error("Error in parus flag calculator" + str(error))
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
        time.sleep(6)
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
          
    return timer, test_status1, test_text1, test_status2, test_text2, res_file