from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [1, 0, 0, -1], [0, 1, -1, 0]
cnt, max_size = 0, 0

def bfs(x, y):
    global cnt, max_size
    size = 0
    q = deque()
    grid[x][y] = 0
    q.append((x, y))

    while q:
        x, y = q.popleft()
        size += 1
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<m and grid[nx][ny]==1:
                grid[nx][ny] = 0
                q.append((nx, ny))

    cnt += 1
    max_size = max(max_size, size)

for r in range(n):
    for c in range(m):
        if grid[r][c] == 1: bfs(r, c)

print(f'{cnt}\n{max_size}')