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
    # Define database init connection
    def __init__(self, host_db="10.64.30.182", user_db="test",
                 password_db="seevision", name_db="test_interface",
                 port_db=3306, link_type=0):
        """

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
            logging.basicConfig(filename=config.src_path + "/log/system_error.log", level=logging.DEBUG,
                                format="%(asctime)s_%(filename)s[line:%(lineno)d]_%(levelname)s %(message)s")
            logger = logging.getLogger(__name__)
            logger.exception(e)


if __name__ == '__main__':
    print(config.src_path)
