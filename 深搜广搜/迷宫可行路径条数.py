
def dfs(visited,x,y,n,m,mx):
    if x==n-1 and y==m-1:
        return 1
    c=0
    directions = [(0, 1), (1, 0),(-1,0),(0,-1)]
    for i in directions:
        nx=x+i[0]
        ny=y+i[1]
        if 0<=nx<=n-1 and 0<=ny<=m-1 and mx[nx][ny]==0 and not visited[nx][ny]:
                visited[nx][ny]=True
                c+=dfs(visited,nx,ny,n,m,mx)
                visited[nx][ny]=False
    return c
n,m=map(int,input().split())
mx=[]
for _ in range(n):
    mx.append(list(map(int,input().split())))
visited=[[False for _ in range(m)]for _ in range(n)]
visited[0][0]=True
print(dfs(visited,0,0,n,m,mx))







dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 判断坐标是否在迷宫的范围内
def in_bounds(x, y, n, m):
    return 0 <= x < n and 0 <= y < m


# 深度优先搜索 (DFS) 统计所有路径的条数
def dfs(maze, visited, x, y, n, m):
    # 如果到达右下角，找到一条路径，返回1
    if x == n - 1 and y == m - 1:
        return 1

    # 计数器，统计路径条数
    path_count = 0

    # 尝试四个方向移动
    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]

        if in_bounds(next_x, next_y, n, m) and not visited[next_x][next_y] and maze[next_x][next_y] == 0:
            # 标记为已访问
            visited[next_x][next_y] = True
            path_count += dfs(maze, visited, next_x, next_y, n, m)
            # 回溯，取消访问标记
            visited[next_x][next_y] = False

    return path_count


# 读取输入
n, m = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(n)]

# 初始时访问矩阵
visited = [[False] * m for _ in range(n)]
visited[0][0] = True  # 起点标记为已访问

# 执行DFS，从(0, 0)开始，统计路径条数
result = dfs(maze, visited, 0, 0, n, m)

# 输出结果
print(result)