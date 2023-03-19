# 14503번
import sys

N, M = map(int, input().split())
r, c, _d = map(int, input().split())  # (r,c) / d는 방향
room = [list(map(int, input().split())) for _ in range(N)]

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 북(0), 동(1), 남(2), 서(3)


def dfs_robot(x, y, d, count):

    # 1번 조건 : 현재 칸이 아직 청소되지 않은 경우 현재 칸을 청소
    if not room[x][y]:
        count = count + 1
        room[x][y] = 2

    # 주변에 청소할 칸이 있는지 여부를 검사
    cleanable = False
    for dx, dy in directions:
        nx, ny = x+dx, y+dy

        # (3번) 청소할 칸이 있으면 표시
        if 0 <= nx < N and 0 <= ny < M and not room[nx][ny]:
            cleanable = True

    # 청소할 칸이 있으면 반시계 회전 후 전진 가능한지 확인 후 전진
    if cleanable:
        # 반시계 회전
        d = d-1
        if d < 0:
            d = 3

        # 앞쪽 칸 전진할 수 있는 지 검사
        nx, ny = x + directions[d][0], y + directions[d][1]
        if 0 <= nx < N and 0 <= ny < M and not room[nx][ny]:
            x, y = nx, ny   # 전진

        return dfs_robot(x, y, d, count)

    # 청소할 칸 없으면
    else:
        # 후진 가능하면 후진
        nx, ny = x - directions[d][0], y - directions[d][1]
        if 0 <= nx < N and 0 <= ny < M and room[nx][ny] != 1:
            return dfs_robot(nx, ny, d, count)
        else:
            return count

print(dfs_robot(r, c, _d, 0))