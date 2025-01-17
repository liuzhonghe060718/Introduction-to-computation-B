n=int(input())
s=list(map(int,input().split()))
dp=[[0,0,0]for i in range(n)]
dp[0]=[s[0],1,1]
for i in range(1,n):
    if dp[i-1][0]<0:
        dp[i][0]=s[i]
        dp[i][1]=i+1
    else:
        dp[i][0]=dp[i-1][0]+s[i]
        dp[i][1]=dp[i-1][1]
    dp[i][2]=i+1
dp.sort(key=lambda x:(x[0],-x[1],-x[2]),reverse=True)
print(' '.join(map(str,dp[0])))