from collections import deque

dx, dy = [-1,-1,-1,0,0,1,1,1], [-1,0,1,-1,1,-1,0,1]

def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        for i in range(8):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<h and 0<=ny<w and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx, ny))

while True:
    w, h = map(int, input().split())
    cnt = 0
    if w==0 and h==0:
        break

    graph = [list(map(int, input().split())) for _ in range(h)]

    for x in range(h):
        for y in range(w):
            if graph[x][y]==1:
                cnt += 1
                bfs(x, y)

    print(cnt)