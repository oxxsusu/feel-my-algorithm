def solution(phone_book):
    answer = True
    
    hash = {}
    for pnum in phone_book:
        hash[pnum] = 1
        
    for key in phone_book:
        temp = ''
        for k in key:
            temp += k
            if temp in hash and temp != key:
                answer = False

    
    return answer