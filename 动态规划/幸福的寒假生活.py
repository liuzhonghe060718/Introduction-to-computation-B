n=int(input())
plan=[]
def change(x):
    a,b=x.split('.')
    if a=='1':
        return int(b)-7
    else:
        return int(b)+24
for _ in range(n):
    start,end,love=input().split()
    start,end=change(start),change(end)
    if end>=45:
        n-=1
        continue
    plan.append((start,end,int(love)))
plan.sort(key=lambda x:x[1])
dp=[0]*n
dp[0]=plan[0][2]
ans=0
for i in range(1,n):
    dp[i]=plan[i][2]
    for j in range(i):
        if plan[j][1]<plan[i][0]:
            dp[i]=max(dp[i],dp[j]+plan[i][2])
    ans=max(dp[i],ans)
print(ans)