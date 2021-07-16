import requests
import json
import pandas as pd
url = 'http://openapi.seoul.go.kr:8088/4f6a6547456b6368333355736a714f/json/RealtimeCityAir/1/25/'
# 서울역 광장 미세먼지 데이터 가졍ㅎ기
dust = requests.get(url)
# JSON형태로 변환
result = json.loads(dust.text)
# 대기질 데이터를 dataframe으로 변환
data = pd.DataFrame(result['RealtimeCityAir']['row'], columns=['MSRDT', 'MSRSTE_NM','PM10','PM25','IDEX_NM'])
# lambda를 이용하여 날자데이터 변환
def f1(x):
    return x[:8]+" "+x[8:10]+":"+x[10:]
data['MSRDT']=data['MSRDT'].apply(f1)
# 1. 대기질 데이터 변환
# 1) 테이블 형식으로 저장
data_table = [data.values]
# 2) 요청한 형식으로 콘솔에 출력
for i in data_table:
    for j in i:
        for k in j:
            print(k, end=" ")
        print()
# 데이터 시각화
# 3) myaql에 테이블을 생성하고 저장
import pymysql
try:
    con = pymysql.connect(host='127.0.0.1', port=3306,
                          user='root', passwd='mysql', db='test', charset='utf8')
    csr = con.cursor()
    csr.execute("create table dust (num int(5) primary key, msrdt varchar(20), \
                msrste_nm varchar(20),pm10 varchar(20), pm25 varchar(20), state varchar(20))")
    sql = "insert into dust values({},'{}','{}','{}','{}','{}')"
    num = 0
    for i in data_table:
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
    data1 = csr.fetchall()
    print('번호\t연월일\t지역구\t미세먼지(pm10)\t미세먼지(pm25)\t상태')
    for imsi in data1:
        for i in imsi:
            print(i, end="\t")
        print()
    csr.close()
except Exception as ex:
    print('에러 :',ex)
else :
    print("테이블 생성하고 데이터 저장")
# 4) dust.csv에 데이터 저장
data.to_csv("data.csv", index=False)