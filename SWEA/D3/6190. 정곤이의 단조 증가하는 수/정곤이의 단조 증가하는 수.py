from itertools import combinations
T = int(input())

for t in range(T):
    N = int(input())
    num = list(map(int, input().split()))

    case = combinations(num, 2)
    answer = -1
    for c in case:
        sc = str(c[0]*c[1])
        if len(sc) < 2: continue

        flag = True
        for i in range(len(sc)-1):
                if sc[i] > sc[i+1]: flag = False; break

        if flag: answer = max(answer, int(sc))

    print(f'#{t+1} {answer}')