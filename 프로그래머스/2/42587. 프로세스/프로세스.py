from collections import deque

def solution(priorities, location):
    answer = [] 
    q = deque((i, j) for i, j in enumerate(priorities))
    while q:
        process = q.popleft()
        if q and any(process[1] < k[1] for k in q):
            q.append(process)
        else:
            answer.append(process)
    
    # 실행 순서 찾기
    for i in answer:
        if i[0] == location:
            return answer.index(i)+1
    
    return answer