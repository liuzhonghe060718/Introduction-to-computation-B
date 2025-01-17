dp=[0for _ in range(5000)]
dp[0]=1
dp[1]=2
s=0
n=int(input())
for i in range(2,n):
    dp[i]=sum(dp[:i])+1
print(dp[n-1])
