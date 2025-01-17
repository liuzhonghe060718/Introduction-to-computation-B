directions=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

def dfs(x,y,mx,n,m,visited):
    mx[x][y]='.'
    visited[x][y]=True
    q=1
    for i in directions:
        nx=x+i[0]
        ny=y+i[1]
        if 0<=nx<=n-1 and 0<=ny<=m-1:
            if not visited[nx][ny] and mx[nx][ny]=='W':
                mx[nx][ny]='.'
                q+=dfs(nx,ny,mx,n,m,visited)[2]
    return (mx,visited,q)
t=int(input())
for _ in range(t):
    mx1=[]
    k=0
    n1,m1=map(int,input().split())
    visited=[[False for _ in range(m1)]for _ in range(n1)]
    for _ in range(n1):
       mx1.append(list(input()))
    for i in range(n1):
        for j in range(m1):
            if mx1[i][j]=='W':
                mx1,visited,k1=dfs(i,j,mx1,n1,m1,visited)
                k=max(k,k1)
    print(k)