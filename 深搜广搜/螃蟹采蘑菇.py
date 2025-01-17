n=int(input())
matrix=[]
visited=[[[False,False]for _ in range(n)]for _ in range(n)]
dire=[(0,1),(0,-1),(1,0),(-1,0)]
for _ in range(n):
    matrix.append(list(map(int,input().split())))
def dfs(x1,y1,x2,y2):
    for dx,dy in dire:
        nx1=dx+x1
        nx2 = dx + x2
        ny1 = dy + y1
        ny2 = dy + y2
        if 0<=nx1<n and 0<=nx2<n and 0<=ny1<n and 0<=ny2<n:
            if not (visited[nx1][ny1][0] and visited[nx2][ny2][1]):
                if (matrix[nx1][ny1]==0 or matrix[nx1][ny1]==5) and (matrix[nx2][ny2]==0 or matrix[nx2][ny2]==5):
                    visited[nx1][ny1][0]=True
                    visited[nx2][ny2][1]=True
                    if dfs(nx1, ny1, nx2, ny2):
                        return True
                elif (matrix[nx1][ny1] == 9 and (matrix[nx2][ny2]==0 or matrix[nx2][ny2]==5)) or (matrix[nx2][ny2] == 9 and (matrix[nx1][ny1]==0 or matrix[nx1][ny1]==5)):
                    return True
    return False
def c():
    for i in range(n):
        for j in range(n):
            if matrix[i][j]==5:
                xx1,yy1=i,j
                for dx, dy in dire:
                    nxx2 = dx + xx1
                    nyy2 = dy + yy1
                    if 0<=nyy2<n and 0<=nxx2<n and matrix[nxx2][nyy2]==5:
                        xx2,yy2=nxx2,nyy2
                        print('yes' if dfs(xx1,yy1,xx2,yy2) else 'no')
                        return
c()
