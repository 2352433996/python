import pymysql
import time

now = time.strftime("%Y-%m-%d %H:%M:%S")

try:
    user_name = 'admin4'
    password = '123456'
    create_time = now
    user_input = [user_name, password, create_time]
    conn = pymysql.connect(host="localhost", port=3306, user="root", passwd="123456", db="my_python",
                           charset="utf8")
    cus1 = conn.cursor()
    insert_sql = 'insert into users(id,user_name,password,create_time,update_time) values(id,%s,%s,%s,update_time)'
    select_sql = 'select * from users where user_name=%s'
    cus1.execute(select_sql, user_name)
    conn.commit()
    # 判断是否存在用户名    空为false, not false === true
    if not cus1.execute(select_sql, user_name):
        cus1.execute(insert_sql, user_input)
        conn.commit()
        print("【注册成功】")
    else:
        cus1.execute(select_sql, user_name)
        conn.commit()
        # psw = cus1.fetchall()
        # print(psw)
        print("【用户已存在】")
    cus1.close()
    conn.close()
except Exception as e:
    print(e)
