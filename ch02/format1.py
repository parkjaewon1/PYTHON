li = [1, 6, 3]
# {1:3d} 1은 format뒤에 있는 인덱스 번호, 3은 3칸 확보, d는 정수
print("최대값:{1:3d}\t최소값:{0:5d}".format(max(li),min(li)))
#      0123456789012345
str = "c:/data/data.txt"
# test있는 지 확인
print(str.find("test")) # test가 있으면 test가 시작하는 index번호보여주고 없으면 -1
print(str.find('.'))
print(str.rfind('.'))
print(str.find('/'))  # 앞에서 부터 /를 찾아서 첫번째 발견된 /의 인덱스
print(str.rfind('/')) # 뒤에서 부터 /를 찾아서 첫번째 발견된 /의 인덱스
n = str.find('.')
print('확장자 :',str[n+1:]) # str에서 인덱스 (12+1)부터 끝까지 출력
# 폴더명
m = str.rfind('/')
print("패키지명 :",str[:m])
# str를 .기준으로 배열로 만들어라 ['c:/data/data', 'txt']
list = str.split(".")
print(list)
print('총 글자수 :',len(str))
print('배열 갯수 :',len(list))
print('확장자 :',list[len(list) - 1]) # list중에서 인덱스 1번째 것 출력
# 데이터를 python울 변경
print(str.replace('data', 'python'))