import pymysql


def delete_db(sql_delete_1):
    '''删除操作'''
    # 打开数据库连接
    db = pymysql.connect(host='rm-bp106y19fa3992tt9613.mysql.rds.aliyuncs.com',
                         port=3306,
                         user='tc_dev_oficut',
                         passwd='tc_dev_oficut_e2ae82',
                         db='iyb_officialaccount_00')

    # 使用cursor()方法获取操作游标
    cur = db.cursor()

    try:
        cur.execute(sql_delete_1)  # 执行
        cur.execute(sql_delete_2)
        cur.execute(sql_delete_3)
        cur.execute(sql_delete_4)
        # 提交
        db.commit()
    except Exception as e:
        print("操作异常：%s" % str(e))
        # 错误回滚
        db.rollback()
    finally:
        db.close()

if __name__ == '__main__':
    phone = "(16611111113,16611111114)"
    SQL1 = "delete from iyb_policy where id in (SELECT policy_id from iyb_member_policy where member_id in (SELECT id from iyb_homemember where home_memberid in (SELECT id from iyb_homemember where phone in ({}) )  or id in (SELECT id from iyb_homemember where phone in {} ) ))"
    SQL2 = "delete from iyb_member_phone where member_id in (SELECT id from iyb_homemember where home_memberid in (SELECT id from iyb_homemember where phone in ({}) )  or id in (SELECT id from iyb_homemember where phone in ({}) ) )"
    SQL3 = "delete from iyb_member_policy where member_id in (SELECT id from iyb_homemember where home_memberid in (SELECT id from iyb_homemember where phone in ({}) )  or id in (SELECT id from iyb_homemember where phone in ({}) ) )"
    SQL4 = "delete from iyb_homemember where id in (select id from (SELECT id from iyb_homemember where home_memberid in (SELECT id from iyb_homemember where phone in ({}) )  or id in (SELECT id from iyb_homemember where phone in ({}) )) t )"
    sql_delete_1 = SQL1.format(phone)
    sql_delete_2 = SQL2.format(phone)
    sql_delete_3 = SQL3.format(phone)
    sql_delete_4 = SQL4.format(phone)
    delete_db(sql_delete_1)