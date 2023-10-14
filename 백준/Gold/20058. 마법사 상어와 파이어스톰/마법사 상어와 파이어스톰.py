from collections import deque

N, Q = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(2**N)]
Q_list = list(map(int, input().split()))
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

def partition_rotate(sx, sy, level):
    size = 2**level
    part = [[0]*size for _ in range(size)]
    for x in range(size):
        for y in range(size): part[x][y] = grid[x+sx][y+sy]

    # 회전
    part = list(zip(*part[::-1]))
    # 원래 칸으로 복귀
    for x in range(size):
        for y in range(size): grid[x+sx][y+sy] = part[x][y]

def decrease():
    # 얼음이 0 이상 있는 칸 중 주변에 얼음 있는 칸이 2개 이하인 칸은 좌표 기록해뒀다가 한꺼번에 얼음 줄이기
    memo = []
    size = 2**N
    for x in range(size):
        for y in range(size):
            if grid[x][y] < 1: continue
            count = 0
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if 0<=nx<size and 0<=ny<size and grid[nx][ny] > 0: count += 1
            if count < 3: memo.append((x, y))
    for x, y in memo: grid[x][y] -= 1

def bfs(r, c):
    q = deque()
    q.append((r, c))
    size = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<2**N and 0<=ny<2**N and grid[nx][ny] > 0:
                grid[nx][ny] = -1
                size += 1
                q.append((nx, ny))
    return size


def simulation():
    for q in Q_list: # 단계
        region = [i*2**q for i in range(2 ** (N-q))]
        # 회전
        for r in region:
            for c in region:
                partition_rotate(r, c, q)
        # 얼음 줄이기
        decrease()

    # 최종 : 남아있는 얼음의 합과 가장 큰 덩어리 크기 구하기
    ice_sum, largest = 0, 0
    for x in range(2**N):
        for y in range(2**N): ice_sum += grid[x][y]

    for x in range(2**N):
        for y in range(2**N):
            # bfs 하고, 그래도 방문 안 한 곳 있으면 그때 새로 bfs
            if grid[x][y] > 0: largest = max(largest, bfs(x, y))

    print(ice_sum)
    print(largest)

simulation()