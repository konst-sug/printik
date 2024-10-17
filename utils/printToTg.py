import time
import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from config_data.config_one_test import foto_url, update_path
from utils import get_settings


logging.basicConfig(level=logging.INFO)


# --------------------printnatkani order test -----------------------
def printOrder_to_tg(driver, url: list ,test_data: list, send_status: bool) -> list:
    '''Для проверки через телеграм бота
    Адаптировано для запуска тестовых наборов через starter'''
    timer, res_file = get_settings(update_path)
# --------------------send order test -------------------------------
    try:
        driver.get(url=url[1])
        driver.delete_all_cookies()
        driver.implicitly_wait(6)

        driver.find_element(By.CLASS_NAME, "order").click()
        driver.execute_script("window.scrollTo(0,470)","")
        driver.find_element(By.CSS_SELECTOR, "input[name='surname']").send_keys(test_data[1])
        driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys(test_data[0])
        driver.find_element(By.CSS_SELECTOR, "input[name='phone']").send_keys(test_data[3])
        driver.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys(test_data[2])
        driver.find_element(By.CSS_SELECTOR, "input[name='qqfile']").send_keys(foto_url)
        driver.find_element(By.CSS_SELECTOR, "textarea[name='comment']").send_keys(test_data[4])
        driver.find_element(By.CSS_SELECTOR, "select[name='delivery']").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, "select[name='delivery']").click()
        driver.find_element(By.CSS_SELECTOR, "option[value='1']").click()
        #driver.find_element(By.CSS_SELECTOR, "select[name='item-type']").click() 
        time.sleep(1)
        #driver.find_element(By.CSS_SELECTOR, "select[name='item-type']").click() 
        # driver.find_element(By.CSS_SELECTOR, "option[text()='Баннер']").click()
        driver.execute_script("window.scrollTo(0,480)","")
        time.sleep(3)
        sb_btn = driver.find_element(By.CSS_SELECTOR, "input[id='form-submit']")
        logging.info(f'submit button {sb_btn.is_enabled()}')
        if send_status:
            sb_btn.click()
        test_res1 = True
        test_text1 = "Printnatkani_order_form - OK"
        time.sleep(3)
    except Exception as error:
        test_res1 = False
        test_text1 = "Printnatkani_order_form - Error"
        logging.error(str(error))
    logging.info(f'{timer}-{(test_text1)}')
    return timer, test_res1, test_text1


def printFlagconstr_to_tg(driver, url: list, test_data: list, send_status: bool) -> list:
# --------------------constructor order test -----------------------
    '''Для проверки через телеграм бота
    Адаптировано для запуска тестовых наборов через starter'''
    timer, res_file = get_settings(update_path)
    try:
        driver.get(url=url[3])
        driver.delete_all_cookies()
        driver.implicitly_wait(5)
        driver.execute_script("window.scrollTo(0,300)","")
        time.sleep(1)
        step_container = driver.find_element(By.CLASS_NAME, "step-container")
        flag_number = step_container.find_element(By.CLASS_NAME, "shop-q")
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
        test_status1, test_text1 = True, 'Printnatkani_flag_calculator - OK'
    except Exception as error:
        test_status1, test_text1 = False, 'Printnatkani_flag_calculator - Error'
        logging.error("Error in Printnatkani_flag_calculator " + str(error))

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
        time.sleep(2)
        if send_status:
            send.click()
            alert = driver.find_element(By.CLASS_NAME, "modal-content")
            sub_btn = alert.find_element(By.CSS_SELECTOR, "button[type='button']")
            sub_btn.click()
        logging.info(f'Send order button in Printnatkani flag calculator {send.is_enabled()}')
        test_status2, test_text2 = True, "Printnatkani_flag_calculator_order - OK"        
    except Exception as error:
        test_status2, test_text2 = False, "Printnatkani_flag_calculator_order - Error"
        logging.info("Error in Printnatkani_flag_calculator_order" + str(error))
    logging.info(f'{timer}-{(test_text2)}')        
    return timer, test_status1, test_text1, test_status2, test_text2


def printCosuv_to_tg(driver, url: list ,test_data: list, send_status: bool) -> list:
# --------------------Cosuv constructor test -------------------------------
    '''Для проверки через телеграм бота
    Адаптировано для запуска тестовых наборов через starter'''
    timer, res_file = get_settings(update_path)
    try:
        driver.get(url=url[2])
        driver.delete_all_cookies()
        driver.implicitly_wait(10)
        driver.execute_script("window.scrollTo(0,2900)","")
        time.sleep(2)
        driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))
        app = driver.find_element(By.CLASS_NAME, "app")
        app.find_element(By.CLASS_NAME, "base").click()
        popup = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[2]")
        time.sleep(4)
        popup.find_elements(By.CLASS_NAME,"item")[3].click()
        time.sleep(4)
        driver.find_element(By.CLASS_NAME, "text").click()
        time.sleep(3)
        driver.find_element(By.CLASS_NAME, "orange").click()
        time.sleep(3)
        test_status1 = True
        test_text1 = "Printnatkani_Cosuv_constructor - OK"
    except Exception as error:
        test_status1, test_text1 = False, "Printnatkani_Cosuv_constructor - Error" 
        logging.error("Error in sozdat-fotokollazh-cosuv-block: " + str(error))          
    logging.info(f'{timer}-{(test_text1)}')      
    
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
        driver.save_screenshot(res_file)
        time.sleep(1)
        driver.execute_script("window.scrollTo(0,500)","")
        orange_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        ActionChains(driver).move_to_element(orange_btn)
        if send_status:
            orange_btn.click()
    #    driver.execute_script("alert('submit is ready')")
    #    alert = driver.switch_to.alert
    #    alert.accept()
        time.sleep(1)
        test_status2, test_text2 = True, "Printnatkani_Cosuv_send_order - OK"
    except Exception as error:
           test_status2, test_text2 = False, 'Printnatkani_Cosuv_send_order - Error'
           logging.error("Error in Cosuv send order " + str(error))
    logging.info(f'{timer}-{(test_text2)}')        
    return timer, test_status1, test_text1, test_status2, test_text2, res_file
    

def printPlatki_to_tg(driver, url: list, test_data: list, send_status: bool) -> list:
# --------------------Print platki constructor test -----------------------
    '''Для проверки через телеграм бота
    Адаптировано для запуска тестовых наборов через starter'''
    timer, res_file = get_settings(update_path)
   
    try:
        driver.get(url=url[4])
        driver.delete_all_cookies()
        driver.get('https://printnatkani.ru/izgotovlenie_platkov#raschet')
        driver.implicitly_wait(5)
        time.sleep(1)
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
        time.sleep(1)
        logging.info(param.is_enabled())
        driver.save_screenshot(res_file)
        driver.find_element(By.CSS_SELECTOR, "div[class='total-calculator desctop-total']").click()
        time.sleep(1)
        test_status1, test_text1 = True, 'Printnatkani_Platki_calculator - OK'
    except Exception as error:
        test_status1, test_text1 = False, 'Printnatkani_Platki_calculator - Error'
        logging.error("Error in Printnatkani_Platki_calculator " + str(error))
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
    return timer, test_status1, test_text1, test_status2, test_text2, res_file


 # --------------------printnatkani constructor test -----------------------
def printConstr_to_tg(driver, url: list ,test_data: list, send_status: bool) ->list:
    '''Для проверки через телеграм бота
    Адаптировано для запуска тестовых наборов через starter'''
    url_t = 'https://printnatkani.ru/constructor-test'
    timer, res_file = get_settings(update_path)
    test_status1 =False
    test_text1 = ''
    try:
        driver.get(url=url_t)
        driver.delete_all_cookies()
        driver.implicitly_wait(10)
        time.sleep(1)
        action = ActionChains(driver)
        popup = driver.find_element(By.CSS_SELECTOR, "div[id='popups']")
        popup.find_element(By.CLASS_NAME, "close_window").click()
        driver.execute_script("window.scrollTo(0,650)","")
        menu = driver.find_element(By.ID, "left-top-menu")
        menu.find_element(By.CSS_SELECTOR, "div[class='menu-icon menu-18']").click()
        driver.find_element(By.ID, "5").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, "div[class='menu-icon menu-12']").click()
        driver.find_element(By.ID, "147").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, "div[class='menu-icon menu-30']").click()
        driver.find_element(By.CSS_SELECTOR, "div[class='menu-icon menu-30']").click()
        action.move_by_offset(400,400).click().perform()
        driver.find_element(By.CSS_SELECTOR, "div[id='simple-editor']").click()
        text = driver.find_element(By.CSS_SELECTOR, "li[id='simple-text']")
       
        action.move_to_element(text).click().perform()
        driver.execute_script("window.scrollTo(0,1200)","")
        # upload = driver.find_element(By.CLASS_NAME, "step-5-content")
        # upload.find_element(By.ID, "dropzone-0")
        #upload.send_keys("/home/konst/Изображения/i.jpeg")
        send_menu = driver.find_element(By.CSS_SELECTOR, "ul[id='third-menu-part']")
        send_menu.find_element(By.TAG_NAME, "a")
        hover = send_menu.find_element(By.XPATH, "//span[text()='Сделайте за меня']")
        hover.click()
        time.sleep(1)
        test_status1 = True
        test_text1 = "Printnatkani_constructor - OK"
        time.sleep(1)
    except Exception as error:
        test_status1, test_text1 = False, "Printnatkani_constructor - Error"
        logging.error(f'Printnatkani_constructor {str(error)}')   
    logging.info(f'{timer}-{(test_text1)}') 
    try:    
        modal = driver.find_element(By.ID, "order-form-calc")
        modal.find_element(By.ID, "senderName").send_keys(test_data[0])
        modal.find_element(By.ID, "senderMail").send_keys(test_data[2])
        modal.find_element(By.ID, "senderPhone").send_keys(test_data[3])
        modal.find_element(By.ID, "delivery").send_keys(test_data[5])
        modal = driver.find_element(By.ID, "form-submit")
        logging.info(f'form-submit {modal.is_displayed()}')
        time.sleep(1)
        if send_status:
            modal.click()
            time.sleep(3)
            driver.save_screenshot(f"{timer}print-zakaz.png")
        test_status2 = True
        test_text2 = "Printnatkani_constructor_order - OK "
    except Exception as error:
        test_status2, test_text2 = False, "Printnatkani_constructor_order - Error"
        logging.error("Error in printnatkani constructor order" + str(error))          
    
    logging.info(f'{timer}-{(test_text2)}')   
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