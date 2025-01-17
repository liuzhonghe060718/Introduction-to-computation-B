n,m=map(int,input().split())
a=[0]+list(map(int,input().split()))
answer=0
active=False
la=0
for x in range(n):
    if active:
        answer+=(a[x]-la)
        active=False
        if a[x+1]-a[x]>=2:
            answer+=(a[x+1]-a[x]-2)
    else:
        active=True
        la=a[x]
print(answer)
