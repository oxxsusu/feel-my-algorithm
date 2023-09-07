N = int(input())
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
graph = [[0]*101 for _ in range(101)]
ans = 0


for _ in range(N):
    x, y, d, g = map(int, input().split())
    graph[x][y] = 1

    prev = [d]
    for i in range(g):
        rec = [(p+1)%4 for p in prev]
        prev += reversed(rec)

    # 움직이기
    for p in prev:
        nx, ny = x+dx[p], y+dy[p]
        graph[nx][ny] = 1
        x, y = nx, ny

# 정사각형 찾기
for i in range(100):
    for j in range(100):
        if graph[i][j] and graph[i+1][j] and graph[i][j+1] and graph[i+1][j+1]:
            ans += 1

print(ans)