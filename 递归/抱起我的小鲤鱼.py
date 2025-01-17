def word(n):
    if n>0:
        n-=1
        return '抱着'+word(n)+'的我'
    else:
        return '我的小鲤鱼'
x=int(input())
print('吓得我抱起了'+word(x))