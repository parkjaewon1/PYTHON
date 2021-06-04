import os
# cur_list = os.listdir("./")
cur_list = os.listdir("../ch08/")
print("현재 디렉토리 목록")
for i in cur_list:
    print(i)
print(os.stat("./"))