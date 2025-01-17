from collections import deque
T=int(input())
def bfs(start,end,r,c,k,matrix):
    dire = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    queue = deque([[start, 0]])
    visited = {(0, start[0], start[1])}
    while queue:
        [x, y], time = queue.popleft()
        for dx, dy in dire:
            nx = dx + x
            ny = dy + y
            t = (time + 1) % k
            if 0 <= nx < r and 0 <= ny < c and (t, nx, ny) not in visited:
                if [nx, ny] == end:
                    return time + 1
                elif t == 0 or matrix[nx][ny] != '#':
                    visited.add((nx, ny, t))
                    queue.append([[nx, ny], time + 1])
    return 'Oop!'
for _ in range(T):
    r1,c1,k1=map(int,input().split())
    matrix1=[]
    for i in range(r1):
        s=input()
        if 'S' in s:
            start1=[i,s.index('S')]
        if 'E' in s:
            end1=[i,s.index('E')]
        matrix1.append(s)
    print(bfs(start1,end1,r1,c1,k1,matrix1))


from collections import deque

def bfs(x, y):
    visited = {(0, x, y)}
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    queue = deque([(0, x, y)])
    while queue:
        time, x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            temp = (time + 1) % k
            if 0 <= nx < r and 0 <= ny < c and (temp, nx, ny) not in visited:
                cur = maze[nx][ny]
                if cur == 'E':
                    return time + 1
                elif cur != '#' or temp == 0:
                    queue.append((time + 1, nx, ny))
                    visited.add((temp, nx, ny))
    return 'Oop!'


t = int(input())
for _ in range(t):
    r, c, k = map(int, input().split())
    maze = [list(input()) for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if maze[i][j] == 'S':
                print(bfs(i, j))

