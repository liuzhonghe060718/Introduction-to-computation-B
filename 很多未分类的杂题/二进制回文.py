import math
n=int(input())
m=int(math.log(n,2))
s=[0]*(m+1)
while True:
    t=int(math.log(n,2))
    s[t]=1
    n-=2**t
    if n==0:
        break
    if n==1:
        s[0]=1
        break
S=s[::-1]
if S==s:
    print('Yes')
else:
    print('No')





