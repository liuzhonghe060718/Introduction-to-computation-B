n,k,d=map(int,input().split())
dp=[[0,0]for _ in range(n+1)]
dp[0]=[1,1]
dp[d][1]=1
if d!=1:
    dp[1][0]=1
for i in range(2,n+1):
    if i<d:
        dp[i][1]=0
    elif i>d:
        dp[i][1]=dp[i-d][0]
    for j in range(1,k+1):
        if i<j:
            continue
        if i>d:
            dp[i][1]+=dp[i-j][1]
        if j==d:
            continue
        dp[i][0]+=dp[i-j][0]
print(dp)