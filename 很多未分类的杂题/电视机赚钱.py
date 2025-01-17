
n,m=map(int,input().split())
values=list(map(int,input().split()))
values.sort()
money=0
for i in range(m):
    if values[i]<0:
        money+=values[i]
    else:
        break
print(-money)