def solution(brown, yellow):
    # 노랑 기준
    w, h = yellow, 0
    
    while w >= h:
        h += 1
        if yellow%h != 0:
            continue
        
        w = yellow // h
        temp = 2*(w+2) + h*2
        if temp == brown:
            break
    
    answer = [w+2, h+2]
    
    return answer