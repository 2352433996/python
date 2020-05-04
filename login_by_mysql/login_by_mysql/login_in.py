import sys
import os

base_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
print("file：", base_dir)
sys.path.append(base_dir)
print("file：", base_dir)
from the_sql_statement import sql_users

import time
now = time.strftime('%Y-%m-%d %H:%M:%S')
now1 = time.strftime('%Y-%m-%d')
try:
    user_name = 'admin'
    password = '123456'
    login_type = 0
    login_time = now
    user_input = [user_name, password]
    user_wro = [user_name, login_time]
    login_tp = [user_name, login_type, login_time]
    get_user_input = [user_name, password, login_time]

    sql_users.d.select_user()

    select_user = 'select * from users where user_name=%s and password=%s'
    select_dis = 'select count(*) from disable_login where user_name=%s and to_days(login_time) = to_days(\"%r\")'
    insert_dis = 'insert into disable_login(id,user_name,password,login_time) values(id,%s,%s,%s)'
    select_login = 'select login_type from login_in where user_name=%s'
    update_login = 'update login_in set login_type=1 where user_name=%s'
    insert_login = 'insert into login_in(id,user_name,login_type,login_time) values(id,%s,%d,%s)'

    cus1.execute(select_dis, user_wro)
    psw = cus1.fetchall()
    if int(psw[0][0]) >= 10:
        print("【密码错误超过十次，今日禁止登录！】")
    else:
        if not cus1.execute(select_user, user_input):
            cus1.execute(insert_dis, get_user_input)
            conn.commit()
            print("【用户名或密码错误！】")
        else:
            cus1.execute(select_login, user_name)
            psw = cus1.fetchall()
            if int(psw[0][0]) >= 10:
                pass
            print("【登录成功】")
    cus1.close()
    conn.close()
except Exception as e:
    print(e)
