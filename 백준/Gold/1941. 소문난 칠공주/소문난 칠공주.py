from itertools import combinations
from collections import deque
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

def leedasom(g):
    cnt = 0
    for x, y in g:
        if classroom[x][y] == 'S':
            cnt += 1
    if cnt >= 4:
        return True
    return False

def bfs(g):
    visited = [[False]*5 for _ in range(5)]
    visited[g[0][0]][g[0][1]] = True
    q = deque()
    q.append((g[0][0], g[0][1]))
    l = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<5 and 0<=ny<5 and not visited[nx][ny]:
                visited[nx][ny] = True

                if (nx, ny) in g:
                    l += 1
                    if l == 7:
                        return True
                    q.append((nx, ny))
    return False

classroom = [list(input()) for _ in range(5)]
cord = []
for x in range(5):
    for y in range(5):
        cord.append((x, y))

groups = [g for g in combinations(cord, 7) if leedasom(g)] # 메모리 방지용

ans = 0
for g in groups:
    if bfs(g):
        ans += 1

print(ans)