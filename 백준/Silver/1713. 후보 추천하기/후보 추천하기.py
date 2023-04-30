N = int(input())
A = int(input())
student = list(map(int, input().split()))
gallery = []

for s in student:
    size = len(gallery)
    # 학생이 이미 사진틀에 걸려있는지를 판단
    find = False

    for i in range(size):
        si, v = gallery[i]
        if si == s:
            gallery[i][1] += 1  # 이미 걸려있으면 추천수 증가
            find = True
            break

    if not find:
        # 비어있는 사진틀 없을 경우 -> 학생이 이미 걸려있는지, 새로 걸어야 하는지를 판단
        if size == N:
            min_cand = []
            mn = min(gallery, key=lambda x: x[1])[1]    # 가장 작은 추천수를 찾고
            for i in range(N):
                if gallery[i][1] == mn:
                    gallery.pop(i)  # 제일 먼저 만나는 (= 가장 오래된) 학생을 제거함
                    break

        gallery.append([s, 0])

ans = []
for s, v in gallery:
    ans.append(s)
ans.sort()
print(' '.join(map(str, ans)))