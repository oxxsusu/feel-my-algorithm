# 17086번
from collections import deque

directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]  # 8방향
N, M = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(N)]
q = deque()

for n in range(N):
    for m in range(M):
        if area[n][m] == 1:
            q.append((n, m))

while q:
    x, y = q.popleft()
    for dx, dy in directions:
        nx, ny = x+dx, y+dy
        if 0 <= nx < N and 0 <= ny < M:
            # 거리 +1씩 업데이트하고, 아직 방문하지 않은 지점이면 큐에 넣기
            if not area[nx][ny]:
                area[nx][ny] = area[x][y] + 1
                q.append((nx, ny))

print(max(map(max, area))-1)

