from collections import deque
from copy import deepcopy

r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]
dx, dy = [1, 0, 0, -1], [0, 1, -1, 0]
ans = 0

q = {(0, 0, board[0][0])}

while q:
    x, y, temp = q.pop()
    ans = max(ans, len(temp))

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<r and 0<=ny<c and board[nx][ny] not in temp:
            q.add((nx, ny, temp+board[nx][ny]))

print(ans)