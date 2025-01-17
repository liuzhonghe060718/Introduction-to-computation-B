dire=[(0,1),(0,-1),(1,0),(-1,0)]
R,C=map(int,input().split())
matrix=[]
for _ in range(R):
    matrix.append(list(map(int,input().split())))
visited=[[False]*C for _ in range(R)]
def dfs(x,y,path):
    global result
    if len(path)>len(result):
        result=path.copy()
    for dx,dy in dire:
        nx,ny=dx+x,dy+y
        if 0<=nx<R and 0<=ny<C and matrix[nx][ny]<matrix[x][y]:
            if visited[nx][ny]:
                dfs(visited[nx][ny][-1][0],visited[nx][ny][-1][1],path+visited[nx][ny])
            else:
                dfs(nx,ny,path+[[nx,ny]])
    return result
pq=[]
for i in range(R):
    for j in range(C):
        if visited[i][j]:
            continue
        result=[]
        ans=dfs(i,j,[[i,j]])
        if len(ans)>len(pq):
            pq=ans
        for p in range(len(ans)):
            visited[ans[p][0]][ans[p][1]]=ans[p:]
print(len(pq))