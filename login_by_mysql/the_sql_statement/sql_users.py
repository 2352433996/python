import time
import pymysql


class MySql:
    def __init__(self):
        self.connect = pymysql.connect(host="localhost", port=3306, user="root", passwd="123456", db="my_python",
                                       charset="utf8")
        self.cur1 = self.connect.cursor()

    now = time.strftime('%Y-%m-%d %H:%M:%S')

    user_name = 'admin'
    password = '123456'
    login_type = 0
    login_time = now
    user_wro = [user_name, password]
    select = 'select * from users where user_name=%s and password=%s'

    def select_user(self):
        self.cur1.execute(self.select, self.user_wro)
        psw = self.cur1.fetchall()
        print(psw)


d = MySql()
d.select_user()
