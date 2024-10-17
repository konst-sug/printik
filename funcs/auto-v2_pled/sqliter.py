import sqlite3


class SQLiter:

    def __init__(self,database) -> None:
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()


    def close(self):
        self.connection.close()


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