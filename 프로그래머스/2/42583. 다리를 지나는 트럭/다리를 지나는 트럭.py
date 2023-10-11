from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0]*bridge_length)
    truck_weights = deque(truck_weights)
    bweight = 0
    while bridge:
        time += 1
        bweight -= bridge.popleft()
        
        if truck_weights:
            if bweight + truck_weights[0] <= weight:            
                t = truck_weights.popleft()
                bweight += t
                bridge.append(t)
            else: bridge.append(0)

    return time