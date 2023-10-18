d = []
v = ['A','E','I','O','U']
def pm(idx, route, l):
    if len(route) == l: d.append(''.join(route)); return
    for i in range(idx, 5): pm(idx, route+[v[i]], l)

def solution(word):
    for k in range(1, 6): pm(0, [], k)
    d.sort()
    answer = d.index(word)+1
    
    return answer