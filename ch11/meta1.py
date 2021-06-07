import re
p = re.compile("Crow|Servo") # | 는 or
m = p.match("CrowHello")
print(m)
p = re.search('^Life',"Life is too short" ) # ^는 시작
print(p)
p = re.search('^Life', 'MyLife')
print(p)