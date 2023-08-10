from collections import deque
import sys
input = sys.stdin.readline

N, L, R = map(int, input().split())
populations = [list(map(int, input().split())) for _ in range(N)]

# 국경 열기 -> bfs
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
day = 0     # 인구이동 날짜수

while True:
    visited = [[False]*N for _ in range(N)]
    move = False
    for r in range(N):
        for c in range(N):
            if visited[r][c]:
                continue
                
            q = deque()
            q.append((r, c))
            visited[r][c] = True    # 방문처리
            memo = [(r, c)]
            while q:
                x, y = q.popleft()
                for i in range(4):
                    nx, ny = x+dx[i], y+dy[i]
                    if 0<=nx<N and 0<=ny<N and not visited[nx][ny]:
                        diff = abs(populations[x][y] - populations[nx][ny])
                        if L <= diff <= R:
                            memo.append((nx, ny))
                            visited[nx][ny] = True
                            q.append((nx, ny))
            
            # 계산해서 배치
            total = 0
            length = len(memo)
            if length == 1:
                continue
            move = True
            for x, y in memo:
                total += populations[x][y]
            for x, y in memo:
                populations[x][y] = total // length

    if not move:
        break
    day += 1

print(day)

