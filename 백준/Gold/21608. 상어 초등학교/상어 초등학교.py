N = int(input())
std_num = N**2
like_list = [[] for _ in range(std_num)]
order = []
INF = int(1e9)
classroom = [[INF]*N for _ in range(N)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]     # 상하좌우 순

# 교실 자리를 돌면서 해당 학생이 좋아하는 학생이 그 자리 주변에 몇 명이나 있는지.
def like_count(idx):
    temp, result = [], []
    like = like_list[idx]   # 이 학생이 좋아하는 학생 목록

    for x in range(N):
        for y in range(N):
            if classroom[x][y] == INF:  # 빈 자리면 상하좌우를 탐색
                count = 0
                for dx, dy in directions:
                    nx, ny = x+dx, y+dy
                    if 0<=nx<N and 0<=ny<N:
                        nearby_std = classroom[nx][ny]
                        # print(f"({x}, {y}) 근처에 앉은 학생이 있는데 얘가 {nearby_std}이야")
                        if nearby_std in like:
                            count += 1

                # 근처 좋아하는 학생 수 다 셌으면 목록에 추가
                temp.append((x, y, count))

    max_count = max(temp, key=lambda a: a[2])[2]

    for x, y, count in temp:
        if count == max_count:
            result.append((x, y))
    return result

# 해당 좌표 근처에 빈 자리가 몇 개나 있는지 count
def left_seats(x, y):
    count = 0

    for dx, dy in directions:
        nx, ny = x+dx, y+dy
        if 0<=nx<N and 0<=ny<N and classroom[nx][ny] == INF:
            count += 1

    return count

# 자리배치 만족도조사
def rate():
    rating = [0]*std_num
    for x in range(N):
        for y in range(N):
            idx = classroom[x][y]
            like_list_idx = like_list[idx]
            count = 0
            for dx, dy in directions:
                nx, ny = x+dx, y+dy
                if 0<=nx<N and 0<=ny<N and classroom[nx][ny] in like_list_idx:
                    count += 1
            if count==0:
                rating[idx] = 0
            elif count==1:
                rating[idx] = 1
            elif count==2:
                rating[idx] = 10
            elif count==3:
                rating[idx] = 100
            elif count==4:
                rating[idx] = 1000

    print(sum(rating))

for _ in range(std_num):
    idx, love1, love2, love3, love4 = map(int, input().split())
    # 인덱스로 바꾸려면 학생 번호 -1
    order.append(idx-1)
    like_list[idx-1].append(love1-1)
    like_list[idx-1].append(love2-1)
    like_list[idx-1].append(love3-1)
    like_list[idx-1].append(love4-1)

# 두번째 학생부터 배치 시작
for i in range(std_num):

    index = order[i]
    # 좋아하는 학생 인접 수가 제일 큰 좌표 구하기
    like_seat_list = like_count(index)

    # 좌표가 한 개면, 그 자리에 배치
    if len(like_seat_list) == 1:
        x, y = like_seat_list[0][0], like_seat_list[0][1]
        classroom[x][y] = index

    # 여러 개면 2단계로
    else:
        cand = []
        for r, c in like_seat_list:
            cand.append((r, c, left_seats(r, c)))

        # x, y, 인접 빈자리수 튜플로 묶어서 비교
        max_cnt = max(cand, key=lambda a: a[2])[2]

        filter = []
        for x, y, left in cand:
            if left == max_cnt:
                filter.append((x, y))

        filter.sort(key=lambda b: (b[0], b[1]))
        x, y = filter[0][0], filter[0][1]
        classroom[x][y] = index

rate()