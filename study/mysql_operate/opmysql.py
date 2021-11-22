# coding = utf8
import os

from study.mysql_operate import config

os.path.abspath(".")
"""
    @Project:Interface_Project
    @File:opmysql.py
    @Author:十二点前要睡觉
    @Date:2021/11/22 10:52
"""

"""
    Define the package for operations of the MySQL database
    1、Include the basic single operate statement,such like delete、modify、update
    2、Independent query single、multiple statements
    3、Independent add multiple statements
"""
import logging
import pymysql

"""
    the import is not FIND, after whole code input, 
    see whether the config is used, 
    now we can't confirm.
"""


# from public import config
class OperationDbInterface(object):
    def __init__(self, host_db="127.0.0.1", user_db="root",
                 password_db="seevision", name_db="test_interface",
                 port_db=3306, link_type=0):
        """
        Define database init connection
        @param host_db:database service host, if mysql in local, the host_db is the pc ip address
        @param user_db:database user name
        @param password_db:database password
        @param name_db:database name
        @param port_db:database port, integer type
        @param link_type:connection type, to identify the output data is tuple or dictionary, default is dictionary, link_type=0
        @param return:cursor
        """
        try:
            if link_type == 0:
                # Create database connection and return dictionary
                self.conn = pymysql.connect(host=host_db,
                                            user=user_db,
                                            passwd=password_db,
                                            db=name_db,
                                            port=port_db,
                                            charset="utf8",
                                            cursorclass=pymysql.cursors.DictCursor)
            else:
                # Create database connection and return tuple
                self.conn = pymysql.connect(host=host_db,
                                            user=user_db,
                                            passwd=password_db,
                                            db=name_db,
                                            port=port_db,
                                            charset="utf8")
            self.cur = self.conn.cursor()
        except pymysql.Error as e:
            print("Create database connection failed | Mysql Error %d: %s" % (e.args[0], e.args[1]))
            self.log_print(e, level=logging.DEBUG)

    def log_print(self, e, level=logging.DEBUG):
        """
        log saved statement
        @param e: deliver a exception into for saving log
        @param level: deliver the log's level
        @return:None
        """
        if not os.path.exists(config.src_path + "/log"):
            os.mkdir(config.src_path + "/log")
            print("Create log folder!")
        if e:
            logging.basicConfig(filename=config.src_path + "/log/system_error.log", level=level,
                                format="%(asctime)s_%(filename)s[line:%(lineno)d]_%(levelname)s %(message)s")
            logger = logging.getLogger(__name__)
            logger.exception(e)

    def op_sql(self, condition):
        """
        Define single statement's operation, include delete、update.
        @param condition:Common SQL statement, the common use function can replace updateone\deleteone
        @return:dictionary type
        """
        try:
            # execute SQL statement
            self.cur.execute(condition)
            # commit cursor data
            self.conn.commit()
            result = {"code": "0000", "message": "Operation execute success", "data": []}
        except pymysql.Error as e:
            self.conn.rollback()
            result = {"code": "9999", "message": "Operation execute abnormal", "data": []}
            print("Database failure | op_sql %d: %s" % (e.args[0], e.args[1]))
            self.log_print(e, level=logging.DEBUG)
        return result

    def select_one(self, condition):
        """
        single query data
        @param condition:Query SQL statement
        @return:dictionary type
        """
        try:
            rows_affect = self.cur.execute(condition)
            # if query result count is bigger than zero
            if rows_affect > 0:
                # gain a result
                result = self.cur.fetchone()
                result = {"code": "0000", "message": "Single query operation execute success", "data": result}
            else:
                result = {"code": "0000", "message": "Single query operation execute success", "data": []}
        except pymysql.Error as e:
            self.conn.rollback()
            result = {"code": "9999", "message": "Single query operation execute abnormal", "data": []}
            print("Database failure | select_one %d: %s" % (e.args[0], e.args[1]))
            self.log_print(e, level=logging.DEBUG)
        return result

    def select_all(self, condition):
        """
        multiple query data
        @param condition:Query SQL statement
        @return:dictionary type with multiple data contained
        """
        try:
            rows_affect = self.cur.execute(condition)
            if rows_affect > 0:
                # move mouse cursor to initial site
                self.cur.scroll(0, mode="absolute")
                results = self.cur.fetchall()
                result = {"code": "0000", "message": "Multiple query operation execute success", "data": results}
            else:
                result = {"code": "0000", "message": "Multiple query operation execute success", "data": []}
        except pymysql.Error as e:
            self.conn.rollback()
            result = {"code": "9999", "message": "Multiple query operation execute abnormal", "data": []}
            print("Database failure | select_all %d: %s" % (e.args[0], e.args[1]))
            self.log_print(e, level=logging.DEBUG)
        return result

    def insert_data(self, condition, params):
        """
        Define insert operation
        @param condition:Insert SQL statement, such like:insert into config_total (key_config, value_config, description, status) values (%s, %s, %s, %s)
        @param params:insert data ,use list form such like:[("3", "Tom", "1 year 1 class", "6"), ("3", "Tom", "1 year 1 class", "6")]
        @return:dictionary multiple insert result
        """
        try:
            results = self.cur.executemany(condition, params)
            self.conn.commit()
            result = {"code": "0000", "message": "Multiple insert operation execute success", "data": results}
        except pymysql.Error as e:
            self.conn.rollback()
            result = {"code": "9999", "message": "Multiple insert operation execute abnormal", "data": []}
            print("Database failure | insert_more %d: %s" % (e.args[0], e.args[1]))
            self.log_print(e, level=logging.DEBUG)
        return result

    def close_db(self):
        """
        close database
        @return:None
        """
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()
        print("Database close success!")


if __name__ == '__main__':
    print(config.src_path)
    a = OperationDbInterface()
    # result = a.select_one("select * from config_total where id=1")
    # results = a.select_all("select * from config_total")
    # for key, value in result["data"].items():
    #     print("{} : {}".format(key, value))
    # for item_i in results["data"]:
    #     for key, value in item_i.items():
    #         print("{} : {}".format(key, value))
    # a.op_sql("delete from config_total where id>1")
    # Make auto_increment from 1 for beginning
    # a.op_sql("alter table config_total auto_increment=1")
    # a.op_sql(
    #     "insert into config_total (key_config, value_config, description, status) values ('test', 'value_test', '测试配置', '1')")
    # for i in range(9999):
    #     a.op_sql(
    #         "insert into config_total (key_config, value_config, description, status) values ('test', 'value_test', '测试配置', '1')")
    insert_count = \
        a.insert_data(
            "insert into config_total (key_config, value_config, description, status) values (%s, %s, %s, %s)",
            [("5", "Tom", "1 year 1 class", "6"), ("6", "Jimmy", "2 year 2 class", "8")])["data"]
    print("insert success affect number:{}".format(insert_count))
    a.close_db()
    # upload to zhihu.com
