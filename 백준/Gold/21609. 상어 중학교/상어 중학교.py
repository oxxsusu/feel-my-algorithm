from collections import deque

N, M = map(int, input().split())
black, rainbow = -1, 0
grid = [list(map(int, input().split())) for _ in range(N)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
INF = float('inf')
point = 0
largest_block = []

# 주어진 좌표를 기준으로 블럭 그룹 찾기
def find_group(r, c):
    visit = [[False]*N for _ in range(N)]
    block = [(r, c)]    # 시작점
    color = grid[r][c]  # 무지개 제외 이 색상이 아니라면 깐다
    if color==rainbow or color==black or color==INF:
        # print(f"무지개랑 검은 색, 빈칸에서 출발할 수 없습니다")
        return False
    visit[r][c] = True
    q = deque()
    q.append((r, c))
    while q:
        x, y = q.popleft()
        connection = 0
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            # 격자 안에 있으면서, 검은색 블록이 아니어야 함
            if 0<=nx<N and 0<=ny<N and grid[nx][ny] != black and grid != INF:
                if grid[nx][ny]==rainbow or grid[nx][ny]==color:
                    connection += 1
                    if not visit[nx][ny]:
                        visit[nx][ny]= True
                        q.append((nx, ny))
                        block.append((nx, ny))
        if connection == 0:
            break

    normal_cnt = 0
    for bx, by in block:
        if grid[bx][by]==color:
            normal_cnt += 1

    if normal_cnt<1 or len(block)<2:
        return False
    else:
        # print(f"block : {block}")
        block.sort(key=lambda a: (a[0], a[1]))
        return block
        # standard = find_standard(block)
        # return {'block': block, 'standard': standard}    # 딕셔너리로 리턴해봅세~

# 기준 블럭 찾기
def find_standard(block):
    cand = []
    # 무지개 블록 제거
    for bx, by in block:
        if grid[bx][by] != rainbow:
            cand.append((bx, by))

    cand.sort(key=lambda a:(a[0], a[1]))    # 행 -> 열작은 순 정렬
    standard = cand[0]
    # print(f"standard: {standard}")
    return standard

def find_rainbow(block):
    cnt = 0
    for bx, by in block:
        if grid[bx][by] == rainbow:
            cnt += 1

    return cnt

def remove(block):
    for bx, by in block:
        grid[bx][by] = INF  # 블럭 자리를 INF로 채우고
    pt = len(block)**2
    # print(f"블럭을 부수고 {pt}점 획득")
    global point    # 전역변수 point를 가져와서 사용하겠다
    point += pt

def gravity():
    dx, dy = 1, 0  # 공백 기준으로 위에 숫자가 있으면 바꾼다 (그래야 떨어지니까)
    # print(f"추락 전 : {grid}")

    # 오른쪽 아래(끝) 부터 떨어뜨리기 + 세로로 먼저 떨구기
    for y in range(N-1, -1, -1):
        for x in range(N-1, -1, -1):
            # 숫자 하나 잡고
            if grid[x][y] != black and grid[x][y] != INF:
                nx, ny = x+dx, y+dy
                while 0<=nx<N and 0<=ny<N and grid[nx][ny] == INF:  # 아래가 공백이면 계속 떨어져
                    grid[x][y], grid[nx][ny] = grid[nx][ny], grid[x][y]
                    x, y = nx, ny
                    nx, ny = x+dx, y+dy
                    # print("추락 1회 완료")

    # print(f"추락 후: {grid}")

def rotate():
    global grid
    grid = list(map(list, zip(*grid)))[::-1]

# def test():
#     block = find_group(1, 0)
#     # 크기가 가장 큰 블록 찾는 코드 추가 (무지개 > 기준블록행 > 기준블록열 큰순)
#     print(block)
#     remove(block)
#     gravity()
#     rotate()
#     gravity()

def autoplay():
    global largest_block
    block_list = []
    for x in range(N):
        for y in range(N):
            found_block = find_group(x, y)
            if found_block and found_block not in block_list:
                block_list.append(find_group(x, y))

    if len(block_list)==0:
        return False

    cand = []
    len_list = []
    for i in range(len(block_list)):
        block = block_list[i]
        len_list.append(len(block))

    max_length = max(len_list)
    for block in block_list:
        if len(block)==max_length:
            cand.append(block)

    # print(f"cand:{cand}")
    if len(cand)==1:
        largest_block = cand[0]
    else:
        max_rainbow = find_rainbow(cand[0])
        # print(f"max rainbow:{max_rainbow}")
        rainbow_cand = []
        for c in cand:
            if find_rainbow(c) >= max_rainbow:
                max_rainbow = find_rainbow(c)
                rainbow_cand.append(c)

        # print(f"rainbow cand: {rainbow_cand}")
        if len(rainbow_cand)==1:
            largest_block = rainbow_cand[0]
        else:
            # 기준 블럭 잡기
            standard_cand = []
            for i in range(len(rainbow_cand)):
                standard = find_standard(rainbow_cand[i])
                standard_cand.append((i, standard[0], standard[1]))

            largest_idx = max(standard_cand, key=lambda a: (a[1], a[2]))[0]
            largest_block = rainbow_cand[largest_idx]
            # print(f"기준블럭까지 간 최대 블럭 : {largest_block}")

    # print(f"가장 큰 블록 : {largest_block}")
    remove(largest_block)
    gravity()
    rotate()
    gravity()
    return True


while True:
    go = autoplay()
    if not go:
        break
print(point)
