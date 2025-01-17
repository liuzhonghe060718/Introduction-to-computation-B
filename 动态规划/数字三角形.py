n=int(input())
dp=[]
for i in range(n):
    dp.append(list(map(int,input().split())))
dp.reverse()
for i in range(1,n):
    for j in range(n-i):
        dp[i][j]=max(dp[i-1][j],dp[i-1][j+1])+dp[i][j]
print(dp[-1][0])