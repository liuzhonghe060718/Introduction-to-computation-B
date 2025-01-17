n,m=map(int,input().split())
levels=list(map(int,input().split()))
levels.sort()
dp=[0]*(n-1)
for i in range(n-1):
    dp[i]=levels[i+1]-levels[i]
dp.sort(reverse=True)
print(sum(dp[m-1:]))