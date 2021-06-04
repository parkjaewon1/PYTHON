import cx_Oracle
con = cx_Oracle.connect("scott/tiger@127.0.0.1:1521/xe")
cur = con.cursor()
cur.execute("select * from emp where empno=7839")
for i in cur:
    print(i)
cur.close()
con.close()