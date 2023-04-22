N, M = map(int, input().split())
num = sorted(list(map(int, input().split())))    # 사전순 - 미리 정렬
stack = []
mn = max(num)
visit = [False]*(mn+1)

def dfs(stack):
    if len(stack) == M:
        print(' '.join(map(str, stack)))
        return

    for n in num:
        if visit[n]:
            continue

        visit[n] = True
        stack.append(n)
        dfs(stack)
        stack.pop()    # 트리 복귀
        visit[n] = False

dfs(stack)