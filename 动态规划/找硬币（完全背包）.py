coins=(1,5,10,21,25)
n=int(input())
dp=[100000for _ in range(n+1)]
dp[0],dp[1]=0,1
for i in range(1,n+1):
    for x in coins:
        if i>=x:
            dp[i]=min(dp[i],dp[i-x]+1)
print(dp[n])