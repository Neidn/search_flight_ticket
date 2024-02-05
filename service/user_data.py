from .lib.sqlite3_lib import DBClass


class UserData(DBClass):
    def __init__(self, sqlite3_name):
        super(UserData, self).__init__(sqlite3_name)
        self.table_name = "user"

    def create_user_table(self):
        columns = ["id integer primary key autoincrement",
                   "first_name text",
                   "last_name text",
                   "email text",
                   "create_time text"]

        return self.create_table(self.table_name, columns)

    def insert_user(self, username, password, email, phone, address, create_time, update_time):
        values = [username, password, email, phone, address, create_time, update_time]

        return self.sqlite_insert_data("user", values)

    def delete_user(self, where):
        return self.sqlite_delete_data("user", where)

    def update_user(self, columns_values_dict_list, where):
        return self.sqlite_update_data("user", columns_values_dict_list, where)

    def query_user(self, where):
        query_sql = "select * from user where " + where
        return self.cursor.execute(query_sql)

    def query_all_user(self):
        query_sql = "select * from user"
        return self.cursor.execute(query_sql)

    def close(self):
        super(UserData, self).close()
