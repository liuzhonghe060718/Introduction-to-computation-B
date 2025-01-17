import heapq
m,n,p=map(int,input().split())
matrix=[]
directions=[(1,0),(-1,0),(0,1),(0,-1)]
for _ in range(m):
    matrix.append(list(input().split()))


def dijkstra(x1,y1,x2,y2):
    if matrix[x1][y1]=='#' or matrix[x2][y2]=='#':
        return 'NO'
    else:

            distances = [[float('inf')] * n for _ in range(m)]
            distances[x1][y1]=0
            pq=[(0,x1,y1)]
            while pq:
                cd,cx,cy=heapq.heappop(pq)
                if (cx,cy)==(x2,y2):
                    return cd
                for dx,dy in directions:
                    nx=dx+cx
                    ny=dy+cy
                    if 0<=nx<m and 0<=ny<n and matrix[nx][ny]!='#':
                        distance=cd+abs(int(matrix[cx][cy])-int(matrix[nx][ny]))
                        if distance<distances[nx][ny]:
                            distances[nx][ny]=distance
                            heapq.heappush(pq,(distance,nx,ny))
            return 'NO'

for _ in range(p):
    x1,y1,x2,y2=map(int,input().split())
    print(dijkstra(x1,y1,x2,y2))