r,c = [int(x) for x in input().split()]
s = [[20000]*(c+2)]
for i in range(r):
    s.append([20000]+[int(x) for x in input().split()]+[20000])
s.append([20000]*(c+2))
stack = []
for i in range(1,r+1):
    for j in range(1,c+1):
        stack.append([s[i][j], i, j])
stack.sort()
dire= [[1,0],[-1,0],[0,1],[0,-1]]
dp = [[1]*(c+2) for x in range(r+2)]
while stack:
    temp = stack.pop()
    for i in range(4):
        if s[temp[1]+dire[i][0]][temp[2]+dire[i][1]]<s[temp[1]][temp[2]]:
            dp[temp[1]+dire[i][0]][temp[2]+dire[i][1]] = max(dp[temp[1]+dire[i][0]][temp[2]+dire[i][1]],dp[temp[1]][temp[2]]+1)
ans = 0
for i in range(1,r+1):
    ans= max(ans,max(dp[i]))
print(ans)


