n, m = map(int, input().split())
ls = sorted(list(map(int, input().split())))

s = []
visited = [False] * n

def dfs():
    prev = 0    # 직전값. 길이 2이고 배열이 2 7 9 9 있는데 7 9 뽑고 pop해서 다시 9를 뽑으면 또 7 9가 되니까 직전값 기록해뒀다가 못하게.
    if len(s) == m:
        print(*s)
        return

    for i in range(n):
        if not visited[i] and prev != ls[i]:
            visited[i] = True
            s.append(ls[i])
            prev = ls[i]
            dfs()
            s.pop()
            visited[i] = False

dfs()