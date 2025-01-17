from collections import deque
def bfs(mx,start,m,n):
    visited=[[False]*n for _ in range(m)]
    queue=deque([(start,0)])
    directions=[(0,1),(0,-1),(1,0),(-1,0)]
    while queue:
        (x,y),steps=queue.popleft()
        if mx[x][y]==1:
            return steps
        visited[x][y]=True
        for dx,dy in directions:
            nx=x+dx
            ny=y+dy
            if 0<=nx<m and 0<=ny<n and not visited[nx][ny] and mx[nx][ny] in[0,1]:
                queue.append(((nx,ny),steps+1))
                visited[nx][ny]=True
    return 'NO'
m1,n1=map(int,input().split())
mx1=[]
for _ in range(m1):
    mx1.append(list(map(int,input().split())))
if mx1[0][0]==2:
    print('NO')
else:
    print(bfs(mx1,(0,0),m1,n1))