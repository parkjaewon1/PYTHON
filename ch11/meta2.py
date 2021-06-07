import re
print(re.search('short$','Life is too short, you need python')) # $는 끝문자
print(re.search('short$','Life is too short'))
print(re.search('short[$]','Life is too short')) # 문자$
print(re.search('short\$','Life is too short'))  # 문자$