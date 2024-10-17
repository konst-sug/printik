import sqlite3


class SQLiter:

    def __init__(self,database) -> None:
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()


    def post_info(self, table: str,  done_time: str, site_id: int,test_name: str, test_status: bool, descr: str) -> bool:
        data = (done_time,site_id,test_name, test_status, descr, )
        try:
            with self.connection:
                query = f"INSERT INTO {table} (done_time, site_id, test_name,test_status,descr) VALUES(?,?,?,?,?);"
                self.cursor.execute(query, data)
        except sqlite3.Error as e:
            print(f"Error: {e.args[0]}")            
        except Exception as error:
            print("Error in add_task block" + error)


    def user_exists(self, user_id: int) -> bool:
        data = (user_id, )
        table = 'users'
        try:
            with self.connection:
                query = f"SELECT * FROM {table} WHERE tg_id=?;"
                #print(query)
                info = self.cursor.execute(query,data).fetchone()
                #print(info)
                #info = self.cursor.execute('SELECT * FROM users WHERE tg_id=?', (user_id, )).fetchone()
    #-------------------Если запрос вернул 0 строк, то...------------
                if info == None: 
                        return False
                else:
                        return True    
        except sqlite3.Error as e:
            print(f"Error: {e.args[0]}")            
        except Exception as error:
            print("Error in add_task block" + error)               


    def save_user(self, user_id, user_name, start_time):
        data = (user_id, user_name, start_time,)
        table = 'users'
        try:
            with self.connection:
                query = f"INSERT INTO users (tg_id, user_name, start_time) VALUES(?,?,?);"
                self.cursor.execute(query, data)   
        except sqlite3.Error as e:
            print(f"Error: {e.args[0]}")            
        except Exception as error:
            print("Error in add_task block" + error)     


    def save_user_entry(self, user_id, user_name, start_time):
        data = (user_id, user_name, start_time,)
        table = 'entries'
        try:
            with self.connection:
                query = f"INSERT INTO {table} (tg_id, user_name, time) VALUES(?,?,?)"
                self.cursor.execute(query, data)   
        except sqlite3.Error as e:
            print(f"Error: {e.args[0]}")            
        except Exception as error:
            print("Error in add_task block" + error) 


    def get_user_entry(self, tg_id):        
        table = 'entries'
        try:
            with self.connection:
                # query = f"SELECT * FROM {table} WHERE tg_id=?;"
                # info = self.cursor.execute(query,tg_id).fetchall()
                info = self.cursor.execute('SELECT * FROM users WHERE tg_id=?', (int(tg_id), )).fetchone()
                #Если запрос вернул 0 строк, то...
                if len(info) == 0: 
                        return False
                else:
                        return info    
        except sqlite3.Error as e:
            print(f"Error: {e.args[0]}")            
        except Exception as error:
            print("Error in add_task block" + error)  


    def close(self):
        self.connection.close()
