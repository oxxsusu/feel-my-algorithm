def solution(citations):
    H_index = []

    for h in range(len(citations), -1, -1):
        upper = [x for x in citations if x >= h]
        lower = [x for x in citations if x not in upper]
        
        lower.sort(reverse=True)
        if len(upper) >= h:
            if lower and lower[0] <= h:
                H_index.append(h)
                break
            
            if not lower and h != 0:
                H_index.append(h)
                break
                
    if len(H_index)==0:
        answer = 0
    else:
        answer = max(H_index)
                
    return answer