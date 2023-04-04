N, M = map(int, input().split())
sky = [list(map(int, input().split())) for _ in range(N)]
move = [tuple(map(int, input().split())) for _ in range(M)]

directions =[(0,0), (0,-1), (-1,-1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)] #(x,y) 순 -> 이동할때 y,x로 담기


def watercopy(r, c):
    count = 0
    ds = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
    for dx, dy in ds:
        nx, ny = r+dx, c+dy
        # 이때 대각선에서 경계를 넘어가는 칸은 앞으로 돌아오지 않는다
        if 0 <= nx < N and 0 <= ny < N and sky[nx][ny] > 0:
            count += 1
    sky[r][c] += count
    # print(f"({r}, {c})에 물이 {count}만큼 있어")


# 비바라기 : 구름이 있는 곳의 x,y 좌표를 입력 받는다.
def bibaragi(clouds, d, s):
    for _ in range(len(clouds)):
        x, y = clouds.pop(0)
        dx, dy = directions[d]    # d는 1부터 되게 숫자 맞춰놨음

        # s만큼 이동
        for _ in range(s):
            nx, ny = x+dx, y+dy
            if nx < 0:
                nx = N-1
            if nx >= N:
                nx = 0
            if ny < 0:
                ny = N-1
            if ny >= N:
                ny = 0
            x, y = nx, ny

        # 다시 구름 위치 집어넣기
        clouds.append((x, y))

        # 구름에서 비 내리기
        sky[x][y] += 1

        # 대각선 물 검사해서 추가
        # watercopy(x, y)

        # print(f"구름 이동한 위치: {clouds}")

    for x, y in clouds:
        watercopy(x, y)

    # 다음 구름 위치 찾기
    new_clouds = []
    for r in range(N):
        for c in range(N):
            if sky[r][c] >= 2 and (r, c) not in clouds:
                new_clouds.append((r, c))
                sky[r][c] -= 2  # 구름이 생기면 물의 양이 2만큼 줄어든다
    return new_clouds


# init
first_clouds = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]

# 이동 시작
for dd, ss in move:
    # print(f"first cloud: {first_clouds}")
    next_clouds = bibaragi(first_clouds, dd, ss)
    # print(f"next cloud: {next_clouds}")
    first_clouds = next_clouds
    # print(sky)

ans = 0
for i in range(N):
    for j in range(N):
       ans += sky[i][j]

print(ans)
