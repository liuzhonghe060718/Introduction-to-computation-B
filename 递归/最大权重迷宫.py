c,answer=-1000000,[]
def dfs(visited,x,y,n,m,mx,path,c1):
    if x==n-1 and y==m-1:
        global c,answer
        if c<c1:
            answer=path[:]
            c=c1
        return
    directions = [(0, 1), (1, 0),(-1,0),(0,-1)]
    for i in directions:
        nx=x+i[0]
        ny=y+i[1]
        if 0<=nx<=n-1 and 0<=ny<=m-1 and not visited[nx][ny]:
                visited[nx][ny]=True
                path.append((nx+1,ny+1))
                c1+=mx[nx][ny]
                dfs(visited,nx,ny,n,m,mx,path,c1)
                visited[nx][ny]=False
                c1 -= mx[nx][ny]
                path.pop(-1)
n,m=map(int,input().split())
mx=[]
for _ in range(n):
    mx.append(list(map(int,input().split())))
visited=[[False for _ in range(m)]for _ in range(n)]
visited[0][0]=True
dfs(visited,0,0,n,m,mx,[(1,1)],mx[0][0])
for i in answer:
    print(' '.join(map(str,i)))