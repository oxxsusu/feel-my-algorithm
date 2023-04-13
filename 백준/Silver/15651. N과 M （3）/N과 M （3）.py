# point - 같은 수 여러번 골라도 됨
N, M = map(int, input().split())
l = []

def dfs():
    if len(l)==M:
        print(' '.join(map(str, l)))
        return

    for i in range(1, N+1):
        l.append(i)
        dfs()
        l.pop()

dfs()