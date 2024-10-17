import time
import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from config_data.config_one_test import foto_url, update_path
from utils import get_settings



# --------------------flagWinder order test -----------------------
def winderOrder_to_tg(driver, url: list ,test_data: list, send_status: bool) -> list:
    '''Для проверки через телеграм бота
    Адаптировано для запуска тестовых наборов через starter'''
    # timer = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # res_file = os.path.join(*update_path,f'results/{timer}-scr.png')
    timer, res_file = get_settings(update_path)
    
    try:
        driver.get(url=url[5])
        driver.implicitly_wait(10)
        driver.delete_all_cookies()
        driver.get(url=url[6])
        driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        time.sleep(1)
        test_status = False
        test = driver.find_element(By.XPATH, "/html/body/div[11]/div/form/div/div/div[2]/div/div[1]/input")
        phone_field = driver.find_element(By.XPATH, "/html/body/div[11]/div/form/div/div/div[2]/div/div[2]/input")
        email_form = driver.find_element(By.XPATH, "/html/body/div[11]/div/form/div/div/div[2]/div/div[3]/input")
        fil_field = driver.find_element(By.CSS_SELECTOR, "div.qq-upload-button-selector.qq-upload-button input")
        fil_field.send_keys(foto_url)
        time.sleep(2)
        test.send_keys(f"{test_data[0]} {test_data[1]}") 
        phone_field.send_keys(test_data[3])
        email_form.send_keys(test_data[2])
        if not send_status:
            time.sleep(2)
            fil_field = driver.find_element(By.CSS_SELECTOR, "div.qq-upload-button-selector.qq-upload-button input")
            upload_tr = driver.find_element(By.XPATH, "/html/body/div[11]/div[1]/form/div/div/div[3]/div/div/ul/li")
            test_text = "qq-file-id-0"
            test_st = upload_tr.get_attribute("class").split(" ")
            if test_text in test_st:
                test_status = True
        test_text = "Winder_order_form - OK"
        sub_btn =driver.find_element(By.CLASS_NAME, "submit-order")
        if send_status:
             sub_btn.click()
        #----- От значения time ниже зависит отправится ли форма заказа. ПРИ == 5 ОТПРАВКА ИДЕТ!
        driver.save_screenshot(res_file)
        time.sleep(5)
        test_status = True
    except Exception as error:
        test_status = False
        test_text = "Winder_order_form - Error"
        logging.error("Winder_order_form - Error' " + str(error))  
    logging.info(f'{timer} {str(test_text)}')
    return timer, test_status, test_text, res_file


 # --------------------flagWinder flag&Order test -----------------------
def winderConstr_to_tg(driver, url: list ,test_data: list, send_status: bool) -> list:
    '''Для проверки через телеграм бота
    Адаптировано для запуска тестовых наборов через starter'''
    # timer = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # res_file = os.path.join(*update_path,f'results/{timer}-scr.png')
    timer, res_file = get_settings(update_path)
    
    try:
        driver.get(url=url[5])
        driver.delete_all_cookies()
        driver.implicitly_wait(7)
        cnt_btn = driver.find_element(By.CLASS_NAME,"btn-order_width_xl")
        driver.get('https://flagwinder.ru/#calculator')
        cnt_fl = driver.find_element(By.CLASS_NAME, "shop-q")
        time.sleep(2)
        step_2 = driver.find_element(By.ID, "step-2")
        cnt_fl.clear()
        time.sleep(1)
        cnt_fl.send_keys("1")
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
        h_flag = driver.find_element(By.CSS_SELECTOR, "div[price='2700']")
        h_flag.click()
        step_2 = driver.find_element(By.CLASS_NAME, "total-calculator")
        step_2.click()
        
        time.sleep(1)
        driver.save_screenshot(res_file)
        test_status1, test_text1 = True, "Winder_flag_calculator - OK"
    except Exception as error:
                test_status1, test_text1 = False, 'Winder_flag_calculator - Error'
                logging.error("Error in Winder-flag-calculator" + str(error))            
    logging.info(f'{timer} {str(test_text1)}')
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
       #---- для отправки заказа применить click к элементу send ---------
        time.sleep(1)
        if send_status:
            send.click()
            alert = driver.find_element(By.CLASS_NAME, "modal-content")
            sub_btn = alert.find_element(By.CSS_SELECTOR, "button[type='button']")
            sub_btn.click()
            #print(sub_btn.is_enabled()) 
        test_status2, test_text2 = True, "Winder_flag_calculator_order - OK"
        #print(timer, test_status2, test_text2)           
    except Exception as error:
           test_status2, test_text2 = False, "Winder_flag_calculator_order - Error"
           logging.error("Error in Winder_flag_calculator_order" + str(error))

    logging.info(f'{timer} {str(test_text1)}')
    logging.info(f'{timer} {str(test_text2)}')

    return timer, test_status1, test_text1, test_status2, test_text2, res_file
    
    

