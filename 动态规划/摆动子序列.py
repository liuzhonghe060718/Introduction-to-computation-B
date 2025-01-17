n=int(input())
nums=list(map(int,input().split()))
dp=[[1,1]for i in range(n)]
for x in range(1,n):
    for y in range(0,x):
        if nums[x]>nums[y]:
            dp[x][1]=max(dp[y][0]+1,dp[x][1])
        elif nums[x]<nums[y]:
            dp[x][0]=max(dp[y][1]+1,dp[x][0])
print(max(dp[-1]))