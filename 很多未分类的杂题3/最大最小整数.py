import math

n=int(input())
s=input().split()
t=len(max(s))
m=[() for _ in range(n)]
for i in range(n):
    dp=list(s[i])
    m[i]=(dp*(math.ceil(t/len(dp)+1)),i)
m.sort()
z=[0]*n
for i in range(n):
    z[i]=s[m[i][1]]
a=''.join(z)
z.reverse()
b=''.join(z)
print(f'{b} {a}')
