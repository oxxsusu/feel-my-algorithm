N = int(input())
key = int(input())

grid = [[0]*N for _ in range(N)]
x, y = N//2, N//2
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
grid[x][y] = 1

idx = 2
for n in range(3, N+1, 2):
    # 순서 있음 : 위로 N-2 -> 오른쪽 N-2 -> 아래 N-1 -> 왼쪽 N-1 후 N증가(홀수) 후 계속 반복
    for i in range(2):
        for _ in range(n-2):
            x, y = x+dx[i], y+dy[i]
            grid[x][y] = idx
            idx += 1

    for i in range(2, 4):
        for _ in range(n-1):
            x, y = x+dx[i], y+dy[i]
            grid[x][y] = idx
            idx += 1

for _ in range(N-1):
    x, y = x+dx[0], y+dy[0]
    grid[x][y] = idx
    idx += 1

for g in grid: print(*g)
for r in range(N):
    for c in range(N):
        if grid[r][c] == key: print(r+1, c+1)