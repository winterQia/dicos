#!/usr/bin/python
# -*- coding: utf-8 -*-
# auther: qianxd
# date: 2019/4/1613:57

import pymysql

class Login_Mysql(object):

    def __init__(self, host, database, user, password, port=3306, charset='utf8'):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port
        self.charset = charset

    def connect(self):
        try:
           self.conn = pymysql.connect(host=self.host, database=self.database, user=self.user, password=self.password,
                                    port=self.port, charset=self.charset)
        except Exception as a:
            print "数据库连接失败，%s" %a
        self.cursor = self.conn.cursor()


    def close(self):
        self.cursor.close()
        self.conn.close()

    def execute(self, sql, params=None):
        self.connect()
        self.cursor.execute(sql, params)
        self.conn.commit()

    def fetchall(self, sql,params=None):
        self.execute(sql, params)
        print  self.cursor.fetchall()


if __name__ == '__main__':
    dbhelp = Login_Mysql(host='172.16.3.29',database='dicos_3rd', user='root', password='dicos8888')
    sql = 'select * from tstore limit 11  '
    dbhelp.fetchall(sql)





