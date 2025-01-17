P = int(input())
potions = []
for i in range(P):
    potions.append((int(input())))
dp=[[0,0]for _ in range(P)]
dp[0][0]=-1000000
dp[0][1]=potions[0]
ans=0
max0,max1=-100000000,potions[0]
for i in range(1,P):
    dp[i][0]=max1-potions[i]
    dp[i][1]=max0+potions[i]
    max1=max(max1,dp[i][1])
    max0=max(max0,dp[i][0])
    ans=max(ans,max1,max0)
print(ans)


