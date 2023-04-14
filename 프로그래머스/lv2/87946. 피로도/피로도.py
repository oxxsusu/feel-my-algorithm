from itertools import permutations

def solution(k, dungeons):
    size = len(dungeons)
    order = [i for i in range(size)]
    cases = list(permutations(order, size))
    answer = 0

    for case in cases:
        count, heart = 0, k
        for i in case:
            enter, spend = dungeons[i]
            if heart < enter:
                break
            count += 1
            heart -= spend 
            
        if count > answer:
            answer = count
    
    return answer