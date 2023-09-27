dlist = []

def dfs(left, route):
    if not left:
        dlist.append(route)
        return
    
    for j in range(len(left)):
        if left[j][0] == route[-1]:
            cleft, croute = deepcopy(left), deepcopy(route)
            croute.append(left[j][1])
            cleft.pop(j)
            dfs(cleft, croute)
        
def deepcopy(arr):
    return [a[:] for a in arr]
    

def solution(tickets):  
    for i in range(len(tickets)):
        start, dest = tickets[i]
        if start == 'ICN':
            route = [start, dest]
            ct = deepcopy(tickets)
            ct.pop(i)
            dfs(ct, route)
        
    temp = []
    for d in dlist:
        if len(d) == len(tickets) + 1:
            temp.append(d)
            
    return min(dlist)