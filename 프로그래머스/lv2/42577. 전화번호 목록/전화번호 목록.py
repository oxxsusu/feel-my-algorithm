def solution(phone_book):
    d = {}
    for num in phone_book:
        d[num] = True
        
    for key in d:
        temp = ''
        for k in key:
            temp += k
            if temp in d.keys() and temp != key:
                return False
            
    return True