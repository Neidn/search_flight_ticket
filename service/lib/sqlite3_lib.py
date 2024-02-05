import sqlite3


class DBClass(object):
    def __init__(self, sqlite3_name):
        self.sqlite3_dbname = ''
        self.db = None
        self.cursor = None

        self.open(sqlite3_name)

    def open(self, sqlite3_name):
        self.sqlite3_dbname = sqlite3_name
        self.db = sqlite3.connect(self.sqlite3_dbname)
        self.cursor = self.db.cursor()

    def close(self):
        if self.db is not None:
            self.db.close()

    def commit(self):
        self.db.commit()

    def sql_exec(self, sql):
        self.cursor.execute(sql)
        self.commit()

        return self.cursor

    def create_table(self, table_name, columns):
        create_table_sql = "create table if not exists " + table_name + "("

        for col in columns:
            create_table_sql += col + ","

        create_table_sql = create_table_sql.rstrip(",") + ")"

        return self.sql_exec(create_table_sql)

    def drop_table(self, table_name):
        drop_table_sql = "drop table if exists " + table_name
        return self.sql_exec(drop_table_sql)

    def sqlite_insert_data(self, table_name, values):
        insert_into_value_sql = "insert into " + table_name + " values("

        for val in values:
            insert_into_value_sql += val + ","

        insert_into_value_sql = insert_into_value_sql.rstrip(",") + ")"

        return self.sql_exec(insert_into_value_sql)

    def sqlite_delete_data(self, table_name, where):
        delete_from_where_sql = "delete from " + table_name + " where " + where
        return self.sql_exec(delete_from_where_sql)

    def sqlite_update_data(self, table_name, columns_values_dict_list, where):
        update_set_where_sql = "update " + table_name + " set "
        for columns_values_dict in columns_values_dict_list:
            update_set_where_sql += columns_values_dict.keys()[0] + "=" + columns_values_dict.values()[0] + ","

        update_set_where_sql = update_set_where_sql.rstrip(",") + " where " + where

        return self.sql_exec(update_set_where_sql)

    def sqlite_select_data(self, table_name, columns, where):
        select_from_where_sql = "select "

        for column in columns:
            select_from_where_sql += column + ","

        select_from_where_sql = select_from_where_sql.rstrip(",") + " from " + table_name + " where " + where

        return self.sql_exec(select_from_where_sql)
