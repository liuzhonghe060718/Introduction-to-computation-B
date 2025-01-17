t=int(input())
for _ in range(t):
    n,m,x0,y0=map(int,input().split())

    directions=[(1,2),(2,1),(1,-2),(2,-1),(-1,-2),(-2,-1),(-1,2),(-2,1)]
    mx=[[False]*m for _ in range(n)]
    def dfs(x,y,idx,k):
        if idx==n*m:
            k.append(0)
            return
        for dx,dy in directions:
            nx=x+dx
            ny=y+dy
            if 0<=nx<n and 0<=ny<m and not mx[nx][ny]:
                mx[nx][ny]=True
                dfs(nx,ny,idx+1,k)
                mx[nx][ny]=False
    k=[]
    mx[x0][y0]=True
    dfs(x0,y0,1,k)
    print(len(k))


t=int(input())
for _ in range(t):
    n,m,x0,y0=map(int,input().split())
    directions=[(1,2),(2,1),(1,-2),(2,-1),(-1,-2),(-2,-1),(-1,2),(-2,1)]
    mx=[[False]*m for _ in range(n)]
    k=0
    def dfs(x,y,idx):
        if idx==n*m:
            global k
            k+=1
            return
        for dx,dy in directions:
            nx=x+dx
            ny=y+dy
            if 0<=nx<n and 0<=ny<m and not mx[nx][ny]:
                mx[nx][ny]=True
                dfs(nx,ny,idx+1)
                mx[nx][ny]=False
    mx[x0][y0]=True
    dfs(x0,y0,1)
    print(k)