# 1012번
from collections import deque

T = int(input())
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs(m, n):
    q = deque()
    q.append((m, n))

    while q:
        m, n = q.popleft()
        for dx, dy in directions:
            nx, ny = m+dx, n+dy
            if 0 <= nx < M and 0 <= ny < N and farm[nx][ny]:
                farm[nx][ny] = 0
                q.append((nx, ny))


for _ in range(T):
    M, N, K = map(int, input().split())  # M = x, N = y
    farm = [[0] * N for _ in range(M)]

    for i in range(K):
        x, y = map(int, input().split())
        farm[x][y] = 1

    count = 0
    for x in range(M):
        for y in range(N):
            if farm[x][y]:
                bfs(x, y)
                count += 1

    print(count)
