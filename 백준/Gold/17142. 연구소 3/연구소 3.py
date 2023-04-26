from itertools import combinations
from collections import deque

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

virus, empty = [], []

def count(m):
    mn = 0
    for x in range(N):
        for y in range(N):
            if m[x][y] == '':
                # print("띠용 이거 빈칸임")
                return False

            if m[x][y].isdigit() and int(m[x][y]) > mn:
                mn = int(m[x][y])

    return mn

for x in range(N):
    for y in range(N):
        if grid[x][y] == 2:
            virus.append((x, y))    # 바이러스 좌표
        if grid[x][y] == 0:
            empty.append((x, y))    # 빈 칸 좌표

mv = combinations(virus, M)     # M개의 바이러스 조합을 뽑음
ans = float('inf')

for v in mv:    # 각 조합마다 최소시간 출력
    _map = [['']*N for _ in range(N)]

    for x in range(N):
        for y in range(N):
            if grid[x][y] == 2:    
                if (x, y) in v:     # 활성 처리
                    _map[x][y] = '0'
                else:   # 비활성 처리
                    _map[x][y] = '*'
            if grid[x][y] == 1:     # 벽 처리
                _map[x][y] = '-'

    q = deque()
    # visited = [[False]*N for _ in range(N)]
    # 방문배열 필요없을듯.. 방문 안한 지점이면 ''일테니까

    # 초기화
    for x, y in v:
        q.append((x, y, 1))    # 큐에 집어넣고 bfs 고

    while q:
        x, y, t = q.popleft()
        for dx, dy in directions:
            nx, ny = x+dx, y+dy

            # 벽 이거나 원발지 가 아닌 경우에만 전파
            if 0<=nx<N and 0<=ny<N:
                if _map[nx][ny] == '':  # 빈 칸이면 바이러스 전파
                    _map[nx][ny] = str(t)
                    q.append((nx, ny, t+1))
                if _map[nx][ny] == '*':  # 비활성 바이러스면
                    _map[nx][ny] = '0'
                    q.append((nx, ny, t+1))

    # print(_map)
    mn = count(_map)
    if mn and mn < ans:
        ans = mn

if len(empty)==0:
    print(0)
elif ans != float('inf'):
    print(ans)
else:
    print(-1)
