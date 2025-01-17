direction=input()
wrong_str=list(input())
right_str=[]
list_1=list('qwertyuiopasdfghjkl;zxcvbnm,./')
if direction=="R":
    for i in wrong_str:
        right_str.append(list_1[list_1.index(i)-1])
else:
    for i in wrong_str:
        right_str.append(list_1[list_1.index(i)+1])
print(''.join(right_str))
