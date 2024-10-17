import sqlite3
import telebot
import datetime
import logging
import os

from loader import query, functions_in_acc, token, admin, key1
from time import sleep
from keyboards.buttons import markup
from config_data.config_one_test import time_keep, target_fold, db_path

bot = telebot.TeleBot(token)

logger = logging.getLogger(__name__)


def str_formattin(numbers):
    if int(numbers) < 10:
        numbers = '0' + str(numbers) + ' '
    else:
        numbers = str(numbers)
    return numbers 


def sessions_manager():
    while True:
# ---------------- clear old screenshot, time_keep to set a period----------------
        current_date = datetime.datetime.now()
        date_to_delete = current_date - datetime.timedelta(hours=time_keep)

        for root, dirs, files in os.walk(target_fold):
            for file in files:
                file_path = os.path.join(root, file)
                file_mod_date = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
                if file_mod_date < date_to_delete:
                    os.remove(file_path)
        query_copy = query.copy()
        logging.info(query_copy)
        for key, value in query_copy.items():
          
            if datetime.datetime.now() >= value[1]:
                try:
                    if query[key][0] == 'error':
                        hour = str_formattin(str(value[5].hour)) 
                        minute = str_formattin(str(value[5].minute)) 
                        hour_m = str_formattin(str(value[6].hour)) 
                        minute_m = str_formattin(str(value[6].minute))
                        del query[key] 
                        text = f"""
                                    Запрос: {hour} : {minute}
                                    Запрос на рассмотрении: {hour_m} : {minute_m}
                                                        """
                        text_for_admin = f"""
                                    ❎Попытка входа:
                                    Запрос: {hour} : {minute}
                                   """
                        
                        bot.send_message(chat_id=key, text=text, reply_markup=markup)
                        logging.info("Failed to request: invalid data")
                        try:
                            for i in admin:
                                bot.send_message(chat_id=i, text=text_for_admin)
                        except Exception as error:
                            text_error = "Failed to send a message to one of the admins "
                            logging.error(f"{text_error}   {str(error)}")

                        continue

                except Exception as error:
                    logging.error(
                        'Error in the manager when displaying the result to a person with the status "error"    ' + str(
                            error))
                  
                    continue
                try:
                    result = True
                    """ Some new functions"""
                    #result = sign_in(key, value, functions_in_acc[value[0]])
                except Exception as error:
                    """ Some new functions"""
                    text_error = "Error in manager in 'result "
                    continue

# -------------------timeouts for processes calculating  ------------
        with sqlite3.connect(db_path) as connect:
            cs = connect.cursor()
            waybills = cs.execute(f"SELECT * FROM result_table").fetchall()
            if waybills != list():
                logging.info(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}--print_Test_Bot workin")
                    
            connect.commit()
 # -------------------timeouts for processes in sleep ---------------
       
        sleep(1800)
        bot = telebot.TeleBot(token)
        bot.send_message(chat_id=key1, text=f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}--print_Test_Bot workin ...")
        
        
