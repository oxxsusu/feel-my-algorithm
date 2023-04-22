N, M = map(int, input().split())
num = sorted(list(map(int, input().split())))

s = []
visit = [False]*(max(num)+1)

def dfs(stack):

    if len(stack) == M:
        print(' '.join(map(str, stack)))

    for n in num:
        if visit[n]:
            continue

        if stack:
            mn = max(stack)
            if n > mn:
                visit[n] = True
                stack.append(n)
                dfs(stack)
                stack.pop()
                visit[n] = False
        else:
            visit[n] = True
            stack.append(n)
            dfs(stack)
            stack.pop()
            visit[n] = False

dfs(s)