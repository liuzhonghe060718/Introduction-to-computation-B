'''
n,m=map(int,input().split())
dp=[0for _ in range(n+1)]
dp[0]=1
for i in range(1,n+1):
    if i<m:
        dp[i]=dp[i-1]*2
    elif i==m:
        dp[i]=dp[i-1]*2-1
    else:
        dp[i]=dp[i-1]*2-dp[i-m-1]
print(dp[n])
'''
n,m=map(int,input().split())
answer=0
def bfs(idx,now):
    global answer
    if idx==n:
        answer+=1
        return
    if now<m-1:
        bfs(idx+1,now+1)
    bfs(idx+1,now)
bfs(0,0)
print(answer)