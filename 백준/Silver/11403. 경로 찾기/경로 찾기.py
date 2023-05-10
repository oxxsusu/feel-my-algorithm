from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
ans = [[0]*n for _ in range(n)]

def solution():
    for i in range(n):
        q = deque()
        q.append(i)
        visited = [False]*n

        while q:
            start = q.popleft()
            if visited[start]:
                continue

            visited[start] = True
            for dest in range(n):
                if graph[start][dest]:
                    ans[i][dest] = 1
                    q.append(dest)

    for a in ans:
        print(*a)

solution()