N, M = map(int, input().split())
ans = []
visit = [False] * (N+1)

def dfs():
    if len(a) == M:
        print(' '.join(map(str, a)))
        return

    for i in range(1, N+1):
        if visit[i]:
            continue
        visit[i] = True
        a.append(i)
        dfs()
        a.pop()
        visit[i] = False

a = []

dfs()