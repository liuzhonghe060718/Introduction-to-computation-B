from collections import deque
def bfs(n,m,martix,t):
    q=deque()
    visited=[[False for _ in range(m)]for _ in range(n)]
    q.append(((0,0),0))
    directions=[(0,-1),(0,1),(1,0),(-1,0)]
    while q:
        (x,y),steps=q.popleft()
        if (x,y)==(n-1,m-1):
            return steps
        visited[x][y] = True
        if martix[x][y]==2:
            if visited[t[0][0]][t[0][1]] and not visited[t[1][0]][t[1][1]]:
                q.append(((t[1][0],t[1][1]),steps))
            if visited[t[1][0]][t[1][1]] and not visited[t[0][0]][t[0][1]]:
                q.append(((t[0][0], t[0][1]),steps))
        for dx,dy in directions:
            nx=dx+x
            ny=dy+y
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and martix[nx][ny]:
                q.append(((nx,ny),steps+1))
    return -1
n1,m1=map(int,input().split())
t1,lp=[],[]
for i in range(n1):
    s=list(map(int,input().split()))
    if 2 in s:
        t1.append([i,s.index(2)])
    lp.append(s)
print(bfs(n1,m1,lp,t1))
