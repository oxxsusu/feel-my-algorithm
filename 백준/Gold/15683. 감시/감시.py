N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
directions = [[],
              [[0], [1], [2], [3]],  # 1번 방향
              [[0, 2], [1, 3]],  # 2번 방향
              [[0, 1], [1, 2], [2, 3], [3, 0]],     # 3번 방향
              [[3, 0, 1], [0, 1, 2], [1, 2, 3], [2, 3, 0]], # 4번 방향
              [[0, 1, 2, 3]]    # 5번 방향
              ]

def cp(gd):
    return [g[:] for g in gd]

def safety_size(gd):
    cnt = 0
    for x in range(N):
        cnt += gd[x].count(0)

    # print(f"현재 안전지대 크기 {cnt}")
    return cnt

def dfs(grid, depth):
    global ans

    if depth == len(cctv):
        ans = min(ans, safety_size(grid))
        return

    x, y, t = cctv[depth]
    ds = directions[t]
    gd = cp(grid)

    for d in ds:
        monitor(gd, x, y, d)
        dfs(gd, depth+1)    # 현재까지의 탐색 결과를 가지고 다음 cctv 탐색
        gd = cp(grid)   # 다음 방향 탐색용으로 복사해두기

def monitor(ng, x, y, d):
    for i in d:
        nx, ny = x, y
        while True:
            nx += dx[i]
            ny += dy[i]

            if 0<=nx<N and 0<=ny<M:
                if ng[nx][ny] == 6:
                    break

                if ng[nx][ny] == 0:
                    ng[nx][ny] = -1

                if ng[nx][ny] in [1, 2, 3, 4, 5]:
                    continue

            else:
                break


cctv, ans = [], int(1e9)
for x in range(N):
    for y in range(M):
        if grid[x][y] != 0 and grid[x][y] != 6:
            cctv.append((x, y, grid[x][y]))

dfs(grid, 0)
print(ans)

