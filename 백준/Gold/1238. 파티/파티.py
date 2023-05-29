import heapq

n, m, x = map(int, input().split())
adj = [[] for _ in range(n+1)]

for _ in range(m):
    start, end, t = map(int, input().split())
    adj[start].append((end, t))


def dijkstra(start):
    INF = float('inf')

    q = []
    heapq.heappush(q, (0, start))
    dp = [INF]*(n+1)
    dp[start] = 0

    while q:
        cost, now = heapq.heappop(q)
        if dp[now] < cost:
            continue

        for next, c in adj[now]:
            new_cost = cost+c
            if new_cost < dp[next]:
                dp[next] = new_cost

            heapq.heappush(q, (new_cost, next))

    return dp

ans = 0
x_to_i = dijkstra(x)

for i in range(1, n+1):
    if i == x:
        continue

    temp_dp = dijkstra(i)
    time = temp_dp[x] + x_to_i[i]
    if ans < time:
        ans = time

print(ans)