import heapq

q = []
n = int(input())

for _ in range(n):
    index, start, end = map(int, input().split())
    t = end - start
    heapq.heappush(q, (start, end))

start, end = heapq.heappop(q)
proceed = []
heapq.heappush(proceed, end)
while q:
    start, end = heapq.heappop(q)

    # 가장 빨리 끝나는 강의랑 시작 시간이 같거나 이후이면 강의실 잡을 필요 xx
    if start >= proceed[0]:
        heapq.heappop(proceed)
        
    heapq.heappush(proceed, end)

print(len(proceed))