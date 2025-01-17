nums=list(map(int,input().split(',')))
n=len(nums)
dp=[[0,0]for _ in range(n)]
dp[0]=[1,1]
for i in range(1,n):
    for j in range(i):
        if nums[i]>nums[j]:
            dp[i][0]=max(dp[i][0],dp[j][1]+1)
        elif nums[i]<nums[j]:
            dp[i][1]=max(dp[i][1],dp[j][0]+1)
print(max(dp[-1]))