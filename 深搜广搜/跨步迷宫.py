from collections import deque


def bfs(n, m, grid):
    queue = deque()
    queue.append(((0, 0), 0))
    visited = [[False for _ in range(m)] for _ in range(n)]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue:
        (x, y), steps = queue.popleft()

        if (x, y) == (n - 1, m - 1):
            return steps

        for dx, dy in directions:
            nx = dx + x
            ny = dy + y

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] == 0:
                visited[nx][ny] = True
                queue.append(((nx, ny), steps + 1))

                mx, my = dx * 2 + x, dy * 2 + y
                if 0 <= mx < n and 0 <= my < m and not visited[mx][my] and grid[mx][my] == 0:
                    visited[mx][my] = True
                    queue.append(((mx, my), steps + 1))

    return -1


n1, m1 = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n1)]

print(bfs(n1, m1, matrix))


