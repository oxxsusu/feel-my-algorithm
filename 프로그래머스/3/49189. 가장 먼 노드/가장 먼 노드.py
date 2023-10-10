import heapq

def solution(n, edge):
    
    # 다익스트라
    distance = {node: float('inf') for node in range(1, n+1)}
    d = {}
    for i in range(1, n+1): d[i] = []
    for s, e in edge: d[s].append(e); d[e].append(s)
    distance[1] = 0 # 시작지 1로 초기화
    q = []
    heapq.heappush(q, [distance[1], 1])
    
    while q:
        current_distance, now = heapq.heappop(q)    # 현재까지의 거리, 탐색할 노드
        if distance[now] < current_distance: continue   # 현재 보고 있는 거리가 기록된 최단거리보다 길다면 바로 pass
        
        for next in d[now]:
            new_distance = current_distance + 1
            if new_distance < distance[next]:
                distance[next] = new_distance
                heapq.heappush(q, [distance[next], next])
            
    return list(distance.values()).count(max(distance.values()))
