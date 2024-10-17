import logging
import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from sqliter import SQLiter

from config import test_data, db_path, site_id, url_d, chrome_options

logging.basicConfig(level=logging.INFO)

driver = webdriver.Chrome(options=chrome_options)
db = SQLiter(database=db_path)
timer = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def products_test(send_status=False):
    driver.get(url=url_d['parus_prod'])
    driver.implicitly_wait(5)
    time.sleep(3)
    #driver.execute_script("window.scrollTo(0,800)","")
    try:
        button = driver.find_element(By.CLASS_NAME, "make-order-button_w").click()
        modal_w = driver.find_element(By.CLASS_NAME,"modal-body")
        modal = driver.find_element(By.CLASS_NAME, "form-control")
        modal.send_keys("2")
        row = driver.find_elements(By.CLASS_NAME, "row")
        inp_name = driver.find_element(By.XPATH, "/html/body/div[9]/div/div/div/div[7]/div/div/div[2]/form/div[2]/div[1]/input").send_keys(test_data[1])
        input_email = driver.find_element(By.XPATH, "/html/body/div[9]/div/div/div/div[7]/div/div/div[2]/form/div[2]/div[2]/input").send_keys(test_data[2])
        input_phone = driver.find_element(By.XPATH, "/html/body/div[9]/div/div/div/div[7]/div/div/div[2]/form/div[2]/div[3]/input").send_keys(test_data[3])
        modal = driver.find_element(By.CLASS_NAME, "add-detail-modal").click()
        delivery = driver.find_element(By.TAG_NAME, "select")
        #print("delivery change label is enable", delivery.is_enabled())
        textarea = driver.find_element(By.XPATH, "/html/body/div[9]/div/div/div/div[7]/div/div/div[2]/form/div[3]/div/div[2]/div/textarea")
        ActionChains(driver).move_to_element(textarea).click(textarea).perform()
        textarea.send_keys(test_data[4])
        #driver.execute_script("arguments[0].scrollTop = arguments[1]", modal_w)
        modal = driver.find_element(By.CLASS_NAME, "add-detail-modal").click()
        submit = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        #print("submit button is ready", submit.is_enabled())
        if submit.is_enabled() & delivery.is_enabled():
            test_status = True
            test_text = "Flag-parus_our_products_order - OK"
        time.sleep(1)
    except Exception as error:
        test_status = False
        test_text = 'Flag-parus_our_products_order - Error'
        logging.error("Error in products-block" + str(error))  
    finally:
        driver.close()   
    db.post_info("result_table",timer,site_id,"products-test",test_status,test_text)    
    logging.info(f'{timer}-{(test_text)}') 


def main():
    products_test()


if __name__ == '__main__':
      main()