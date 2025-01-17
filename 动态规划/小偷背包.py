import math
n,b=map(int,input().split())
values=list(map(int,input().split()))
weighs=list(map(int,input().split()))
a=weighs[0]*1000
weigh=weighs[:]
while len(weigh)>1:
    a=math.gcd(a,weigh.pop(-1)*1000)
a=a//1000
for i in range(n):
    weighs[i]=weighs[i]//a
m=b//a
s=[[0for _ in range(m)]for _ in range(n)]
for i in range(m):
    if i+1>=weighs[0]:
        s[0][i]=values[0]
for j in range(1,n):
    for i in range(m):
        if weighs[j]<=i+1:
            s[j][i]=values[j]
            t=i-weighs[j]
            if t>=0:
                s[j][i]+=s[j-1][t]
            if s[j-1][i]>s[j][i]:
                s[j][i]=s[j-1][i]
        else:
            s[j][i]=s[j-1][i]
print(s[-1][-1])







