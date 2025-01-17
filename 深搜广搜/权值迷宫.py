n,m=map(int,input().split())
matrix,grid=[],[]
directions=[(0,1),(0,-1),(1,0),(-1,0)]
answer=-100000000
for i in range(n):
    matrix.append(list(map(int,input().split())))
for i in range(n):
    grid.append(list(map(int,input().split())))
visited=[[False]*m for _ in range(n)]
def dfs(x,y,value):
    global answer
    if x==n-1 and y==m-1:
        answer=max(answer,value)
        return
    visited[x][y]=True
    for dx,dy in directions:
        nx=x+dx
        ny=y+dy
        if 0<=nx<n and 0<=ny<m and  not visited[nx][ny] and matrix[nx][ny]==0:
            dfs(nx,ny,value+grid[nx][ny])
    visited[x][y]=False
dfs(0,0,0)
print(answer+grid[0][0])