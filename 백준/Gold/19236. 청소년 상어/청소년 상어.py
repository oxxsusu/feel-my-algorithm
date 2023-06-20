import copy

directions = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
sea = [[] for _ in range(4)]

for j in range(4):
    ls = list(map(int, input().split()))
    for i in range(4):
        sea[j].append([ls[i*2], ls[i*2+1]-1])    # 물고기 번호, 방향 입력

ans = []

def dfs(sx, sy, score, sea):
    # 상어가 먹는 행위
    score += sea[sx][sy][0]
    sea[sx][sy][0] = 0  # 물고기 제거, 방향은 그대로
    ans.append(score)

    # 물고기 이동 (1번부터)
    for f in range(1, 17):
        fx, fy = float('inf'), float('inf')
        # f번 물고기의 좌표 찾기
        for x in range(4):
            for y in range(4):
                if sea[x][y][0] == f:
                    fx, fy = x, y
                    break
        # 번호에 해당하는 물고기가 sea에 없다면 pass
        if fx==float('inf') and fy==float('inf'):
            continue

        fd = sea[fx][fy][1]
        for k in range(8):
            nd = (fd + k) % 8   # 다음 방향 번호
            nx, ny = fx+directions[nd][0], fy+directions[nd][1]
            if not (0<=nx<4 and 0<=ny<4) or (nx==sx and ny==sy):
                continue

            # 상어 아니면 이동 후 멈추기
            sea[fx][fy][1] = nd     # 방향 갱신
            sea[fx][fy], sea[nx][ny] = sea[nx][ny], sea[fx][fy]
            break

    # 상어 이동
    sd = sea[sx][sy][1]
    for j in range(1, 4):
        snx, sny = sx+directions[sd][0]*j, sy+directions[sd][1]*j
        if 0<=snx<4 and 0<=sny<4 and sea[snx][sny][0] != 0:
            # dfs
            dfs(snx, sny, score, copy.deepcopy(sea))

dfs(0, 0, 0, sea)
print(max(ans))