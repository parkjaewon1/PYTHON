s = "usr/local/bin/python"
# 경로 : "usr/local/bin, 파일명 : python
# 뒤부터 찾아서 발견되는 첫번째 /의 인덱스 값
index = s.rfind("/")
print("경로 :",s[:index])
print("파일명 :",s[index+1:])