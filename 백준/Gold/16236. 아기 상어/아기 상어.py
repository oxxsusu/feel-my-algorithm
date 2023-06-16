from collections import deque
import heapq

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
baby = 2

dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]

def eat(sx, sy):
    global baby

    cand = []
    q = deque()
    visited = [[False]*n for _ in range(n)]
    visited[sx][sy] = True
    q.append((sx, sy, 1))

    while q:
        x, y, depth = q.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and graph[nx][ny] <= baby:
                visited[nx][ny] = True

                if 0 < graph[nx][ny] < baby:
                    cand.append((depth, nx, ny))

                q.append((nx, ny, depth+1))

    if not cand:
        return False

    distance, cord_x, cord_y = min(cand, key=lambda x: (x[0], x[1], x[2]))
    graph[sx][sy] = 0
    graph[cord_x][cord_y] = 9

    global t
    t += distance
    return cord_x, cord_y


sx, sy = 0, 0
for x in range(n):
    for y in range(n):
        if graph[x][y] == 9:
            sx, sy = x, y

t = 0
count = 0

while True:
    cord = eat(sx, sy)
    if not cord:
        print(t)
        break

    count += 1
    if count == baby:
        count = 0
        baby += 1

    sx, sy = cord