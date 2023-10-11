from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0]*bridge_length)
    truck_weights = deque(truck_weights)
    while bridge:
        time += 1
        bridge.popleft()
        
        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:            
                t = truck_weights.popleft()
                bridge.append(t)
            else: bridge.append(0)

    return time