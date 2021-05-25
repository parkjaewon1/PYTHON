#    01234
a = "Hello"
print(a.startswith("H")) # H로 시작하느냐
print(a.endswith("o"))   # o로 끝나느냐
print(a.endswith("h"))   # h로 끝나는냐
print(a.find("l"))       # l문자의 인덱스 번호
print(a.rfind("l"))      # 뒤부터 찾아서 발견된 l의 인덱스 번호
print(a.count("l"))      # l의 갯수
b = "ABCdef"
print(b.isalpha())    # b가 알파벳이냐
print(b.isalnum())    # b가 알파벳 또는 숫자냐
print(b.isnumeric())  # 가 숫자냐
c = "Hello, World"
print(c.replace("Hello", "안녕"))
print(c.split(',')) # 컴마(,)를 기준으로 분리해서 list로 변경해라
print(b.upper()) # b를 대문자로 변경해라
print(b.lower()) # b를 소문자로 변경해라
