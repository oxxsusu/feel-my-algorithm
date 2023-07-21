N, M, K = map(int, input().split())
graph = [[[] for _ in range(N)] for _ in range(N)]

def dir_check(dls):
    start = dls[0]%2
    for d in dls:
        if d%2 != start:
            return False
    return True

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    graph[r-1][c-1].append((m, s, d))

# 이동
for _ in range(K):
    move_list = []
    for x in range(N):
        for y in range(N):
            while graph[x][y]:  # 빈 칸이 될 때까지 m, s, d 추출해 이동
                m, s, d = graph[x][y].pop()
                move_list.append((x, y, m, s, d))

    # 이동
    for r, c, m, s, d in move_list:
        nr, nc = (r+dx[d]*s)%N, (c+dy[d]*s)%N
        graph[nr][nc].append((m, s, d))     # 이동한 위치에 새로 달아줌

    # 같은 칸 합체
    for x in range(N):
        for y in range(N):
            cnt = len(graph[x][y])
            if cnt > 1:    # 2개 이상 파이어볼이 있는 칸에서 합체
                sum_m, sum_s, sum_d = 0, 0, []
                while graph[x][y]:
                    m, s, d = graph[x][y].pop()
                    sum_m += m
                    sum_s += s
                    sum_d.append(d)
                # 새로운 질량, 새로운 속력, 새로운 방향 구하기
                nm = sum_m // 5
                ns = sum_s // cnt
                nd = []
                if dir_check(sum_d): nd = [0, 2, 4, 6]
                else: nd = [1, 3, 5, 7]
                if nm < 1: continue    # 질량 0 소멸시키기
                for i in range(4):
                    graph[x][y].append((nm, ns, nd[i]))

# 질량 count
ans = 0
for x in range(N):
    for y in range(N):
        while graph[x][y]:
            m, s, d = graph[x][y].pop()
            ans += m

print(ans)