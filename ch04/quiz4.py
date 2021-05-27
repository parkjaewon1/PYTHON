#        01234567
jumin = "881120-1068234"
if int(jumin[7]) == 1:
    print("1900년 태어난 남자")
elif int(jumin[7])  == 2:
    print("1900년 태어난 여자")
elif int(jumin[7])  == 3:
    print("2000년 태어난 남자")
elif int(jumin[7]) == 4:
    print("2000년 태어난 여자")
elif int(jumin[7]) == 5:
    print("외국인 남자")
elif int(jumin[7]) == 6:
    print("외국인 여자")
else:
    print("외계인")