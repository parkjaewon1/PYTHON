import pymysql
# DB연결
con = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='mysql',
                      db='test', charset='utf8')
print(con)
con.close()