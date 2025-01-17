n=int(input())
if n==0:
    print('*')
else:
    for i in range(n-1):
        if i==0:
            print('*')
        elif i==1:
            print('**')
        else:
            print('*'+' '*(i-1)+'*')
    print('*'*n)
