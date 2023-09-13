from collections import deque

dx, dy = [1, 0, 0, -1], [0, 1, -1, 0]

def solution(maps):
    answer = float('inf')
    n, m = len(maps), len(maps[0])
    
    q = deque()
    maps[0][0] = 0  # visited
    q.append((0, 0, 1))

    while q:
        x, y, depth = q.popleft()
        
        if x == n-1 and y == m-1:
            answer = min(answer, depth)
        
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<m and maps[nx][ny] == 1:
                maps[nx][ny] = 0
                q.append((nx, ny, depth+1))
    
    if answer == float('inf'):
        answer = -1
    return answer