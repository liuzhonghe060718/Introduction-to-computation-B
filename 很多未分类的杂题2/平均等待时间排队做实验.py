n=int(input())
price=list(map(int,input().split()))
time=sorted([(price[m-1],m) for m in range(1,n+1)])
m,s=0,[0]*n
for i in range(1,n+1):
    m+=(i-1)*time[-i][0]
    s[i-1]=time[i-1][1]
print(' '.join(map(str, s)))
print('%.2f'% (m/n))
