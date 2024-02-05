from datetime import datetime

from .lib.sqlite3_lib import DBClass


class UserData(DBClass):
    def __init__(self, sqlite3_name):
        super(UserData, self).__init__(sqlite3_name)
        self.table_name = "user"

        self.create_user_table()

    def create_user_table(self):
        columns = ["id integer primary key autoincrement",
                   "first_name text",
                   "last_name text",
                   "email text",
                   "create_time text"]

        return self.create_table(self.table_name, columns)

    def insert_user(self, **kwargs):
        values = [kwargs['first_name'], kwargs['last_name'], kwargs['email'], datetime.now()]

        return self.sqlite_insert_data(self.table_name, values)

    def delete_user(self, where):
        return self.sqlite_delete_data(self.table_name, where)

    def update_user(self, columns_values_dict_list, where):
        return self.sqlite_update_data(self.table_name, columns_values_dict_list, where)

    def query_user(self, where):
        query_sql = f"select * from {self.table_name} where {where}"
        return self.cursor.execute(query_sql)

    def query_all_user(self):
        query_sql = f"select * from {self.table_name}"
        return self.cursor.execute(query_sql)

    def close(self):
        super(UserData, self).close()
