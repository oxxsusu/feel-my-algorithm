import heapq

n, m = map(int, input().split())
init = list(map(int, input().split()))
q = []
for i in init:
    heapq.heappush(q, i)

for _ in range(m):
    a = heapq.heappop(q)
    b = heapq.heappop(q)
    heapq.heappush(q, a+b)
    heapq.heappush(q, a+b)

print(sum(q))