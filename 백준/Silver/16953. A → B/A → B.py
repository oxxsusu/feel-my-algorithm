from collections import deque
a, b = map(int, input().split())

op = deque()
op.append((a, 0))
while op:
    n, cnt = op.popleft()
    if n>b: continue
    if n == b: print(cnt+1); quit()
    op.append((n*2, cnt+1))
    op.append((int(str(n)+'1'), cnt+1))

print(-1)