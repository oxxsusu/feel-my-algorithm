INF = float('inf')
n, m = map(int, input().split())
dp = [INF] * (n+1) # 최단거리 기록용
bus = []
cycle = False

for _ in range(m):
    start, end, cost = map(int, input().split())
    bus.append((start, end, cost))

dp[1] = 0   # 시작점 0으로 초기화
for i in range(n):

    for s, e, c in bus:
        if dp[s] != INF and dp[e] > dp[s] + c:
            if i == n-1:
                cycle = True

            dp[e] = dp[s] + c

if cycle:
    print(-1)
else:
    for i in range(2, n+1):
        if dp[i] == INF:
            print(-1)
        else:
            print(dp[i])