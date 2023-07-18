from collections import deque
import copy

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

r, c, k = map(int, input().split())
route = [list(input()) for _ in range(r)]
count = 0

q = deque()
visited = [[False]*c for _ in range(r)]
visited[r-1][0] = True
q.append((r-1, 0, visited, 1))

while q:
    x, y, v, depth = q.popleft()
    if x==0 and y==c-1:
        if depth == k:
            count += 1
        continue

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<r and 0<=ny<c and not v[nx][ny] and route[nx][ny] != 'T':
            nv = copy.deepcopy(v)
            nv[nx][ny] = True
            q.append((nx, ny, nv, depth+1))

print(count)