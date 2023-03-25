# 1461

N, M = map(int, input().split())
L = sorted(list(map(int, input().split())))

first, last = (L[0], abs(L[0])), (L[len(L)-1], abs(L[len(L)-1]))
end = max((first, last), key=lambda x: x[1])[0]

plus, minus, d = [], [], 0
for l in L:
    if l > 0:
        plus.append(l)
    else:
        minus.append(l)
plus.sort(reverse=True) # 양수는 거꾸로 인덱싱해야 멀리서부터 갖다놓을 수 있음

books_list = [plus[i:i+M] for i in range(0, len(plus), M)] + [minus[i:i+M] for i in range(0, len(minus), M)]

for books in books_list:
    if end in books:
        d += abs(end)
    else:
        max_distance = max(map(abs, books))
        d += max_distance*2

print(d)