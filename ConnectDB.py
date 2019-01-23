#!/usr/bin/env python
# coding: utf-8
# 该类提供增删改查四种方法
import pymysql
import configparser
import sys
cfg = configparser.ConfigParser()
#cfg.read("E:\Python_Project\Spiders-master\Weather\Weather\config.ini")
cfg.read("../AnotherProject/config.ini")

class ConnectDatabase():
    config=None
    db_cursor=None
    db=None
    def __init__(self):
        try:
            self.config = cfg
            db_host = self.config.get("db", "host")           #数据库服务器
            db_port = int(self.config.get("db", "port"))      #数据库端口
            db_user = self.config.get("db", "user")           #数据库用户
            db_pass = self.config.get("db", "password")       #数据库用户登陆密码
            db_db = self.config.get("db", "db")               #数据库实例名称
            db_charset = self.config.get("db", "charset")
            self.db = pymysql.connect(host=db_host, port=db_port, user=db_user, passwd=db_pass, db=db_db,
                                      charset=db_charset)
            self.db_cursor = self.db.cursor()
            print("数据库连接成功")
        except Exception as err:
            print(err)
            print("请检查数据库配置")
            sys.exit()

    def addData(self,sql,sql_data):
        self.db_cursor.execute(sql,sql_data)
       # self.db_cursor.commit()
        #self.db_cursor.close()

    def selectData(self):
        pass
    def updateData(self):
        pass
    def deleteData(self):
        pass


if __name__ == '__main__':
    conn=ConnectDatabase()
