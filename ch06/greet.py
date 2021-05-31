def hello_korean():
    print("안녕하세요")
def hello_english():
    print("Hello")
def greet(k):
    k()
def get_greet(k):
    if k == 'k':
        return hello_korean
    else:
        return hello_english
g = get_greet('k')
g()
g = get_greet('e')
g()
# 함수를 매개변수 사용하여 호출도 가능
greet(hello_korean)
greet(hello_english)