n, m = map(int, input().split())
space = [list(map(int, input().split())) for _ in range(n)]

direction = [-1, 0, 1]
ans = float('inf')

def dfs(x, y, cd, fuel):
    global ans
    if x == n-1:
        ans = min(ans, fuel)
        return

    nx, ny = x+1, y+cd
    if 0<=nx<n and 0<=ny<m:
        for d in direction:
            if d != cd: dfs(nx, ny, d, fuel+space[nx][ny])

for i in range(m):
    for d in direction:
        dfs(0, i, d, space[0][i])

print(ans)