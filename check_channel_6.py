

#!/usr/bin/python
# -*- coding: utf-8 -*-
# auther: qianxd
# date: 2019/3/1917:41
import pymysql
import  sys


def select_channel(storecode):
    con = pymysql.connect(host="172.16.3.29", user="root", password="dicos8888", database="dicos_ios")
    cur = con.cursor()
    sql = "select * from t_storechannel where  channel = 4 and  storeCode = '%s'" % storecode
    print  sql
    cur.execute(sql)
    result = cur.fetchone()
    cur.close()
    con.close()
    print  result
# def insert_channel(storecode):
#     con = pymysql.connect(host="172.16.3.29", user="root", password="dicos8888", database="dicos_ios")
#     cur = con.cursor()
#     sql1 = "INSERT INTO `dicos_ios`.`t_storechannel`(`channel`, `storeCode`, `startTime`, `endTime`, `deliveryType`, `status`, `shutReason`, `shutMapTime`, `consignerId`, `consignerShowName`, `serviceFeeRate`) VALUES ( %s, %s, '07:30', '23:59', '2', '1', NULL, NULL, NULL, NULL, null)" % (channel, storecode)
#
#     try:
#         cur.execute(sql1)
#
#     except Exception as e:
#         con.rollback()
#         print "Transaction failure",e
#     else:
#         con.commit()
#         print "Transaction success"
#     cur.close()
#     con.close()

# def chose(kinds,storecode):
#
#     if kinds == 'select':
#       print   select_channel(storecode)
#     elif kinds == 'insert':
#         insert_channel(storecode)

def bl_storecode_list(storecode_list):
    for storecode in range(len(storecode_list)):
        select_channel(storecode_list[storecode])
        print storecode_list[storecode]

if __name__ == "__main__":



    # storecode = sys.argv[1]
    #1
    # select_channel(storecode)
    storecode_list = raw_input("please input storecode:").split(',')

    bl_storecode_list(storecode_list)
