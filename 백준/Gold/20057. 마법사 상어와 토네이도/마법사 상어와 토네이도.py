N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
spread_left = [(-1, 1, 1), (1, 1, 1), (-1, 0, 7), (1, 0, 7), (-1, -1, 10), (1, -1, 10), (0, -2, 5), (-2, 0, 2), (2, 0, 2)]   # a -> b에서 b점 좌표 기준 x, y, %
spread_down = [(-1,-1,1), (-1,1,1), (0,1,7), (0,-1,7), (0,-2,2), (0,2,2), (1,-1,10), (1,1,10), (2,0,5)]
spread_right = [(-1,-1,1), (1,-1,1), (-1,0,7), (1,0,7), (-2,0,2), (2,0,2), (-1,1,10), (1,1,10), (0,2,5)]
spread_up = [(1,-1,1), (1,1,1), (0,-1,7), (0,1,7), (0,-2,2), (0,2,2), (-1,-1,10), (-1,1,10), (-2,0,5)]
spread_direction = [spread_left, spread_down, spread_right, spread_up]
alpha = [(0, -1), (1,0), (0,1), (-1,0)]
def move():
    ans = 0
    length = 1
    x, y, d = N//2, N//2, 0

    while x != 0:
        # 길이만큼 이동
        for _ in range(2):
            dx, dy = directions[d]
            for _ in range(length):
                # print(f"x:{x}, y:{y}, d:{d}, length:{length}")
                nx, ny = x+dx, y+dy

                # 이동으로 인한 모래 뿌리기
                x, y = nx, ny
                ans += spread(x, y, d)
                # print(graph)

            # 방향을 길이만큼 가고 나서 바꾸기
            d += 1
            if d>3:
                d %= 4  # 방향은 4로 나눈 나머지로 해야 인덱스가 됨

        # 이동거리 증가
        length += 1

    # while문 탈출하면 length 그대로 해서 한번 더 이동
    length -= 1
    dx, dy = directions[d]
    for _ in range(length):
        nx, ny = x+dx, y+dy
        x, y = nx, ny
        ans += spread(x, y, d)

    print(ans)



def spread(x, y, d):
    sand = graph[x][y]  # 현재 a->b 위치의 모래 양
    graph[x][y]=0
    left = sand
    answer = 0
    # 방향에 따라 정해진 비율만큼 모래 버리기
    for dx, dy, ratio in spread_direction[d]:
        nx, ny, spread_sand = x+dx, y+dy, int(sand*0.01*ratio)
        left -= spread_sand     # 모래 버리기
        # 만약 모래가 격자 밖을 벗어나면, 정답에 추가
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            answer += spread_sand
        else:
            graph[nx][ny] += spread_sand    # 흩어진 모래 주변에 추가

    # alpha 자리에 남은 모래들 추가
    ax, ay = alpha[d]
    nx, ny = x+ax, y+ay
    if 0 <= nx < N and 0 <= ny < N:
        graph[nx][ny] += left
    else:
        answer += left

    # print(f"나간 모래 - {answer}")
    return answer

move()