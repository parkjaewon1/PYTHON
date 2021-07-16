import requests
import json
import pandas as pd
url = 'http://openapi.seoul.go.kr:8088/4f6a6547456b6368333355736a714f/json/RealtimeCityAir/1/25/'
# 미세 데이터 가져오기
data = requests.get(url)
# python에서 Json으로 변경하여 사용하기
result = json.loads(data.text)
print(result)
# 대기질 데이터를 가지고 와서 pandas저장
#    RealtimeCityAir, row에서 데이터를 가지고 온다
dust = pd.DataFrame(result['RealtimeCityAir']['row'],
                    columns=['MSRDT','MSRSTE_NM','PM10','PM25','IDEX_NM'])
# 가지고 온 데이터 출력
print(dust)
# 1. 서울 대기질 데이터를 수집
# 1) 테이블에 저장
f1 = lambda x:x[:8]+" "+x[8:10]+":"+x[10:]
dust['MSRDT']=dust['MSRDT'].apply(f1)
print(dust)
dust_table = [dust.values]
print(dust_table)
# writer = pd.ExcelWriter('dust.xlsx')
# dust.to_excel(writer, sheet_name='Sheet1')
# writer.save()
# print("엑셀 저장 성공")
# 2) 요청한 형식으로 콘솔에 출력
for i in dust_table:
    for j in i:      # 데이터 한건을 가지고 와서 i에 저장
        for k in j:  # 데이터 컬럼별로 가지고 와서
            print(k, end="  ") # 컬럼 데이터 출력하고 두칸 띄고
        print() # 줄바꿈
# 2. 시각화
# 3) db(ORACLE)에 적재하고 콘솔에 컬럼명을 보기좋게 변경하여 출력
# import cx_Oracle
# try:
#    conn = cx_Oracle.connect("scott/tiger@127.0.0.1:1521/xe")
#    csr = conn.cursor()
#    # table 생성
#    csr.execute("create table dust (num number(5) primary key, msrdt varchar2(20)," \
#              "msrste_nm varchar2(20), pm10 varchar2(20), pm25 varchar2(20),"  \
#              "state varchar2(20))" )
#    sql = "insert into dust values({},'{}','{}','{}','{}','{}')"
#    num = 0
#    # 테이블에 데이터 저장
#    for i in dust_table:
#        for j in i:
#            num = num + 1
#            msrdt = j[0]
#            msrste_nm = j[1]
#            pm10 = j[2]
#            pm25 = j[3]
#            state = j[4]
#            csr.execute(sql.format(num,msrdt,msrste_nm,pm10,pm25,state))
#    conn.commit()
#    # 저장된 테이블 데이터 읽기
#    csr.execute("select * from dust order by num")
#    data = csr.fetchall()
#    print('번호\t연월일\t지역구\t미세먼지(pm10)\t미세먼지(pm25)\t상태')
#    for imsi in data:
#        for i in imsi:
#            print(i, end="\t")
#        print()
#    csr.close()
# except cx_Oracle.DataError as ex:
#     print("에러 :", ex)
# else:
#    print("테이블 생성하고 저장 성공")
# 2) dust.csv에 데이터 저장
dust.to_csv("dust.csv",index=False)
print("csv로 저장 성공")