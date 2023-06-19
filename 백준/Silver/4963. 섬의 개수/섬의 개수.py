from collections import deque

def bfs(x, y):
    diff = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    
    q = deque()
    q.append((x, y))
    maps[x][y] = 0 # 방문처리
    
    while q:
        now = q.popleft()
        
        for i in range(8):
            nx = now[0] + diff[i][0]
            ny = now[1] + diff[i][1]
            if 0 <= nx < h and 0 <= ny < w:
                if maps[nx][ny] == 1:
                    maps[nx][ny] = 0
                    q.append((nx, ny))
                    
while True:
    w, h = map(int, input().split())
    maps = []
    ans = 0
    
    if w == h == 0:
        break
        
    for _ in range(h):
        maps.append(list(map(int, input().split())))
        
    for i in range(h):
        for j in range(w):
            if maps[i][j] == 1:
                ans += 1
                bfs(i, j)
                
    print(ans)