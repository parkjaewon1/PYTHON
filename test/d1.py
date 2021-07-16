import requests
import json
import pandas as pd
url = 'http://openapi.seoul.go.kr:8088/4f6a6547456b6368333355736a714f/json/RealtimeCityAir/1/25/'
# 서울역 광장 미세먼지 데이터 가져오기
data = requests.get(url)
# JSON형태로 변환
result = json.loads(data.text)
# 대기질 데이터를 DFRAME으로 변환
dust = pd.DataFrame(result['RealtimeCityAir']['row'], columns=['MSRDT', 'MSRSTE_NM','PM10','PM25','IDEX_NM'])
# lambda를 이용하여 날자데이터 변환
f1 = lambda x: x[:8]+" "+x[8:10]+":"+x[10:]
dust['MSRDT']=dust['MSRDT'].apply(f1)
# 1. 대기질 데이터 변환
# 1) 테이블 형식으로 저장
dust_table = [dust.values]
# 2) 요청한 형식으로 콘솔에 출력
for i in dust_table:
    for j in i:
        for k in j:
            print(k, end=" ")
        print()
# 데이터 시각화
# 3) 오라클에 테이블을 생성하고 저장
import cx_Oracle
try:
    con = cx_Oracle.connect('scott/tiger@127.0.0.1:1521/xe')
    csr = con.cursor()
    csr.execute("create table dust (num number(5) primary key, msrdt varchar2(20), \
                msrste_nm varchar2(20),pm10 varchar2(20), pm25 varchar2(20), state varchar2(20))")
    sql = "insert into dust values({},'{}','{}','{}','{}','{}')"
    num = 0
    for i in dust_table:
        for j in i:
            num = num + 1
            msrdt = j[0]
            msrste_nm = j[1]
            pm10 = j[2]
            pm25 = j[3]
            state = j[4]
            csr.execute(sql.format(num,msrdt,msrste_nm,pm10,pm25,state));
    con.commit();
    csr.execute("select * from dust order by num")
    data = csr.fetchall()
    print('번호\t연월일\t지역구\t미세먼지(pm10)\t미세먼지(pm25)\t상태')
    for imsi in data:
        for i in imsi:
            print(i, end="\t")
        print()
    csr.close()
except cx_Oracle.DatabaseError as ex:
    print('에러 :',ex)
else :
    print("테이블 생성하고 데이터 저장")
# 4) dust.csv에 데이터 저장
dust.to_csv("dust.csv", index=False)