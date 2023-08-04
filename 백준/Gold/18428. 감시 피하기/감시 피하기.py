from itertools import combinations

N = int(input())
wall = [list(input().split()) for _ in range(N)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

pool = []
teachers = []
for x in range(N):
    for y in range(N):
        if wall[x][y] == 'X':
            pool.append((x, y))
        if wall[x][y] == 'T':
            teachers.append((x, y))

def monitor(w):
    for x, y in teachers:
        # 방향별로 끝까지 탐섹
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            while 0<=nx<N and 0<=ny<N:
                if w[nx][ny] == 'O':    # 장애물 찾으면 해당 방향 감시 종료
                    break
                if w[nx][ny] == 'S':    # 학생 찾으면 False
                    return False
                nx, ny = nx+dx[i], ny+dy[i]
    return True

comb = combinations(pool, 3)    # 장애물 구역 정하기
ans = 'NO'
for c in comb:
    c_wall = [a[:] for a in wall] # deepcopy
    # 장애물 설치
    for x, y in c:
        c_wall[x][y] = 'O'

    # 감시
    if monitor(c_wall):
        ans = 'YES'
        break

print(ans)