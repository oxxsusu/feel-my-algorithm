from itertools import permutations

def solution(k, dungeons):
    d = len(dungeons)  
    ps = permutations(range(d), d)
    answer = 0
    
    for p in ps:
        power, depth = k, 0
        for i in p:
            if power >= dungeons[i][0]:
                power -= dungeons[i][1]
                depth += 1
        answer = max(answer, depth)
    
    return answer