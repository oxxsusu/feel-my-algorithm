import heapq

def solution(operations):
    min_heap, max_heap = [], []
    
    for op in operations:
        operator, num = op.split(' ')
        num = int(num)
        
        if operator == 'I': 
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
        
        if operator == 'D':
            if not min_heap or not max_heap: continue
            
            if num == 1:
                target = -heapq.heappop(max_heap)
                min_heap.remove(target)
            if num == -1:
                target = heapq.heappop(min_heap)
                max_heap.remove(-target)
                
    if not max_heap: return [0,0]
    else: return [-heapq.heappop(max_heap), heapq.heappop(min_heap)]