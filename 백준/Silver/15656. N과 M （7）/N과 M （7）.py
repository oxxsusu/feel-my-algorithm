N, M = map(int, input().split())
num = sorted(list(map(int, input().split())))
s = []

def dfs(stack):

    if len(stack) == M:
        print(' '.join(map(str, stack)))
        return

    for n in num:
        stack.append(n)
        dfs(stack)
        stack.pop()

dfs(s)