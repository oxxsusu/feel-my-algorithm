T = int(input())
for _ in range(T):
    n = int(input())
    d = dict()
    for _ in range(n):
        name, type = input().split()
        if type not in d.keys():
            d[type] = 2
        else:
            d[type] += 1

    type_list = d.keys()
    tn = 0, len(type_list)
    ans = 1
    for type in d.keys():
        ans *= d[type]

    print(ans-1)