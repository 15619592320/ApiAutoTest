'''
跟业务相关的数据库操作
'''
from JinRongZongHe.caw.Mysql import Mysql


class DbOp:
    def delete_user(self,db,mobilephone):
        '''
        根据手机号码删除用户
        :param db:
        :param mobilephone:
        :return:
        '''
        mysql = Mysql()
        conn = mysql.connect(db)
        mysql.execute(conn, "delete from member where mobilephone=18012345678;")
        mysql.disconnect(conn)