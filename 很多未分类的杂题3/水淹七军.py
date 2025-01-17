import sys
direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
data = sys.stdin.read().split()
k = int(data[0])
id = 1
answer = []
def dfs(matrix, x, y, tx, ty):
    m, n = len(matrix), len(matrix[0])
    h = matrix[x][y]
    stack = [(x, y)]
    visited = [[False for _ in range(n)] for _ in range(m)]

    while stack:
        x, y = stack.pop()
        if x == tx and y == ty:
            return True
        visited[x][y] = True
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and matrix[nx][ny] < h:  # 允许流向等高或更低的位置
                    stack.append((nx, ny))

    return False
for _ in range(k):
    m, n = int(data[id]), int(data[id + 1])
    id += 2
    matrix = [list(map(int, data[id + i * n:id + (i + 1) * n])) for i in range(m)]
    id += m * n
    a, b = int(data[id]) - 1, int(data[id + 1]) - 1
    id += 2
    p = int(data[id])
    id += 1
    pos = [(int(data[id + i * 2]) - 1, int(data[id + i * 2 + 1]) - 1) for i in range(p)]
    id += p * 2

    result = any(dfs(matrix, x, y, a, b) for x, y in pos)
    answer.append("Yes" if result else "No")
sys.stdout.write("\n".join(answer) + "\n")