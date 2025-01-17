n=int(input())
for i in range(n):
    a=list(input())
    if len(a)<=10:
        print(''.join(a))
    else:
        b=[a[0],str(len(a)-2),a[-1]]
        print(''.join(b))
