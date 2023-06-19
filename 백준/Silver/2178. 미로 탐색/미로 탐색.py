from collections import deque

n, m = map(int, input().split())
graph = []
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

def bfs():
    cand = []
    q = deque()
    q.append((0, 0, 1))
    graph[0][0] = '0'

    while q:
        x, y, d = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny]=='1':
                if nx==n-1 and ny==m-1:
                    cand.append(d+1)

                graph[nx][ny] = '0'
                q.append((nx, ny, d+1))

    print(min(cand))

for _ in range(n):
    graph.append(list(input()))

bfs()