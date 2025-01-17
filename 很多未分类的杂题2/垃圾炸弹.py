d=int(input())
n=int(input())
dp={}
for _ in range(n):
    a,b,c=map(int,input().split())
    for x in range(max(0,a-d),min(a+d+1,1025)):
        for y in range(max(0,b-d),min(b+d+1,1025)):
            dp[(x,y)]=dp.setdefault((x,y),0)+c
a=list(dp.values())
m=max(a)
print(f'{a.count(m)} {m}')
