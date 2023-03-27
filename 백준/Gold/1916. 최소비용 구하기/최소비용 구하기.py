from heapq import *
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
buses = [list(map(int, input().split())) for _ in range(M)]
start_city, end_city = map(int, input().split())

q, bus_list = [], [[] for _ in range(N+1)] # 각 도시마다 그 도시에서 출발하는 버스 리스트를 정리함
for b in buses:
    start, end, dist = b[0], b[1], b[2]
    bus_list[start].append((end, dist)) # 도착지와 비용을 튜플로 연결

dist_list = [float("inf") for _ in range(N+1)]   # 도시마다 거리 기록, 출발지는 0으로 초기화
dist_list[start_city] = 0
heappush(q, (0, start_city))

while q:
    d, node = heappop(q)    # d, node : 현재까지의 이동거리, 현재 노드
    if node == end_city:
        print(d)
        break

    if dist_list[node] < d:
        continue

    for bus in bus_list[node]:  # 현재 도시에서 출발하는 버스 리스트
        next_stop, next_distance = bus[0], bus[1]
        cost = dist_list[node] + next_distance  # 현재까지의 거리와 다음 목적지까지의 거리를 합친 값이 cost
        if cost < dist_list[next_stop]: # 다음 목적지까지 노드를 거친 거리값 cost가 그 목적지로 가는 직행거리보다 가까우면 갱신
            dist_list[next_stop] = cost
            heappush(q, (cost, next_stop))