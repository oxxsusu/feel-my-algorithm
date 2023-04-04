N, M, K = map(int, input().split())
# 각 격자 위치마다 fireball의 번호를 달자
fireballs = [list(map(int, input().split())) for _ in range(M)]

# 격자 그래프 위 -> 그 자리에 있는 파이어볼의 인덱스가 리스트로 존재하도록
graph = [[[] for _ in range(N)] for _ in range(N)]
directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

def move(idx):
    r, c, m, s, d = fireballs[idx]
    dx, dy = directions[d]  # 방향
    x, y = r, c     # 초기 x, y 좌표

    # 속력만큼 이동
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

    # 이동한 위치에 인덱스 붙이기
    fireballs[idx][0], fireballs[idx][1] = x, y
    graph[x][y].append(idx)

def is_same(_list):
    first = _list[0]
    result = True

    if first%2 == 0:    # 첫 수가 짝수이면 계속 짝수여야 true 리턴
        for l in _list:
            if l%2 != 0:    # 하나라도 짝수가 아니면 바로 False 리턴
                return False
    else:
        for l in _list:
            if l%2 == 0:
                return False

    return result

def magic():
    for x in range(N):
        for y in range(N):
            num = len(graph[x][y])
            if num > 1:
                m, s, direction = 0, 0, []
                while graph[x][y]:
                    i = graph[x][y].pop()
                    m += fireballs[i][2]
                    s += fireballs[i][3]
                    direction.append(fireballs[i][4])

                m = m//5
                s = s//num
                same, diff = [0, 2, 4, 6], [1, 3, 5, 7]
                if is_same(direction):
                    direction_list = same
                else:
                    direction_list = diff

                # print(f"새로운 파이어볼의 방향: {direction_list}. 질량 {m} 속도 {s}")
                # 질량이 0이 아닌 경우에만 fireball의 정보를 리스트로 만들어서 붙이기
                if m > 0:
                    for d in direction_list:
                        fireballs.append([x, y, m, s, d])
                        # 좌표에도 해당 파이어볼의 인덱스를 붙여주기
                        graph[x][y].append(len(fireballs)-1)

# init
for i in range(len(fireballs)):
    # 1부터 시작이니까 바꿔주기 ㄱㄱ
    x, y = fireballs[i][0], fireballs[i][1]
    fireballs[i][0] -= 1
    fireballs[i][1] -= 1
    graph[x-1][y-1].append(i)

# 이동 명령 시작
for _ in range(K):
    # print(f"이동 전: {graph}")

    # 움직여야 할 파이어볼의 인덱스를 받음
    moving_list = []
    for x in range(N):
        for y in range(N):
            while graph[x][y]:
                new_idx = graph[x][y].pop()
                moving_list.append(new_idx)

    # 이동~
    for idx in moving_list:
        move(idx)

    # 이동이 모두 끝난 뒤 2개 이상의 파이어볼이 있는 칸에서는?
    magic()

    # print(f"마법 후: {graph}")

ans_m = 0
for x in range(N):
    for y in range(N):
        while graph[x][y]:
            i = graph[x][y].pop()
            ans_m += fireballs[i][2]

print(ans_m)
