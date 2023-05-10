from collections import deque

n, m = map(int, input().split())
floor = [list(input()) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

v = [(-1, 0), (1, 0)]   # 세로
h = [(0, -1), (0, 1)]   # 가로

def bfs(x, y):
    visited[x][y] = True
    q = deque()
    if floor[x][y] == '-':
        q.append((x, y, '-', h))
    else:
        q.append((x, y, '|', v))

    while q:
        x, y, s, d = q.popleft()
        for dx, dy in d:
            nx, ny = x+dx, y+dy
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and floor[nx][ny] == s:
                visited[nx][ny] = True
                q.append((nx, ny, s, d))

ans = 0
for x in range(n):
    for y in range(m):
        if not visited[x][y]:
            ans += 1
            bfs(x, y)

print(ans)