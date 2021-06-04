import pymysql,sys
try:
    con = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='mysql',
                          db='test', charset='utf8')
    cursor = con.cursor()
    cursor.execute("select * from dept where deptno=10")
    data = cursor.fetchone()
    # print(data)
    for i in data:
        print(i)
except:  print('에외 : ',sys.exc_info())
finally: cursor.close();  con.close()