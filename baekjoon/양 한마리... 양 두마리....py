# 11123번, DFS/BFS
import sys
from collections import deque

T = int(sys.stdin.readline())

# x 오른쪽, x 왼쪽, y 위쪽, y 아래쪽
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs(x, y):
    # 연속된 양들의 위치를 저장할 큐
    q = deque()
    # 첫 양 저장
    q.append((x, y))
    # 이미 탐색한 자리의 양은 풀로 막아서 중복 탐색 방지
    cage[x][y] = '.'

    while q:
        x, y = q.popleft()
        # 현재 양의 다음 위치 탐색
        for dx, dy in directions:
            # 다음 위치 좌표값
            nx, ny = x+dx, y+dy
            # 인덱스 범위 내에서 이어진 다음 위치가 양이면 큐로 좌표 삽입
            if 0 <= nx < H and 0 <= ny < W and cage[nx][ny] == '#':
                q.append((nx, ny))
                cage[nx][ny] = '.'  # 이미 방문한 위치는 풀로 막음

for _ in range(T):
    H, W = map(int, sys.stdin.readline().rstrip().split())
    cage = [list(sys.stdin.readline().rstrip()) for _ in range(H)]
    count = 0

    for h in range(H):
        for w in range(W):
            if cage[h][w] == '#':
                bfs(h, w)
                count += 1
