from itertools import combinations
from collections import deque

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

def wall_selection():
    empty = []
    for x in range(N):
        for y in range(M):
            if grid[x][y]==0:
                empty.append((x, y))

    return combinations(empty, 3)

# bfs
def spread(ngrid):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    q = deque()

    for x in range(N):
        for y in range(M):
            if ngrid[x][y] == 2:
                q.append((x, y))    # 바이러스 자리 먼저 넣어주고 시작

    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0<=nx<N and 0<=ny<M and ngrid[nx][ny] == 0:
                ngrid[nx][ny] = 2
                q.append((nx, ny))

    return ngrid

def safety_zone(ngrid):
    size = 0
    for x in range(N):
        for y in range(M):
            if ngrid[x][y] == 0:
                size += 1

    return size

def simulation():
    max_size = 0
    ls = wall_selection()

    for l in ls:
        ngrid = [arr[:] for arr in grid]
        for x, y in l:
            ngrid[x][y] = 1      # 벽 세우기
        ngrid = spread(ngrid)
        size = safety_zone(ngrid)
        if size > max_size:
            max_size = size

    return max_size

print(simulation())
