def solution(citations):
    answer = 0
    citations.sort()
    n = len(citations)
    
    for h in range(max(citations)+1):
        up = len([c for c in citations if c >= h])
        down = len([c for c in citations[:n-up] if c <= h])
        if up >= h and len(citations[:n-up]) == down: answer = h
        
    return answer