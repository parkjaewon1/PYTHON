import cx_Oracle,sys
try :
    con = cx_Oracle.connect("scott/tiger@127.0.0.1:1521/xe")
    cur = con.cursor()
    cur.execute("update dept set dname='우리팀' where deptno=17")
    con.commit();
    print("수정 성공")
except: print("에이 : ", sys.exc_info())
finally: cur.close(); con.close()