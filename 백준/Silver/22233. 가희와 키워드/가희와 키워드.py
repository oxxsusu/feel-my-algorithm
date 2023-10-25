import sys
input = sys.stdin.readline

N, M = map(int, input().split())
d = dict()
ans = 0
for _ in range(N):
    key = input().rstrip()
    if not d.get(key):
        d[key] = True
        ans += 1

for _ in range(M):
    keys = list(input().rstrip().split(','))
    for key in keys:
        if d.get(key):
            d[key] = False
            ans -= 1
    print(ans)