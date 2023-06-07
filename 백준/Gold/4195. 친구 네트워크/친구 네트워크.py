def find(x):
    if parent[x] == x: return x
    else:
        p = find(parent[x])
        parent[x] = p
        return p

def union(x, y):
    x, y = find(x), find(y)

    if x != y:
        parent[y] = x
        number[x] += number[y]
    print(number[x])

for _ in range(int(input())):
    num = int(input())
    parent, number = {}, {}
    for i in range(num):
        a, b = input().split()
        if a not in parent:
            parent[a] = a
            number[a] = 1
        if b not in parent:
            parent[b] = b
            number[b] = 1
        union(a, b)