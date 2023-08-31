from itertools import combinations

N = int(input())
S, B, case = [], [], []
for i in range(N):
    s1, b1 = map(int, input().split())
    S.append(s1)
    B.append(b1)

for n in range(1, N+1):
    case += combinations(range(N), n)

def diff(idx_list):
    sour, bitter = 1, 0
    for l in idx_list:
        sour *= S[l]
        bitter += B[l]
    return abs(sour - bitter)

min_diff = float('inf')
for c in case:
    min_diff = min(diff(c), min_diff)

print(min_diff)