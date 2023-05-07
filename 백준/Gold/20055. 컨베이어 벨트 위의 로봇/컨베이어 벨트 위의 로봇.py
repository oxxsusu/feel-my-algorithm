N, K = map(int, input().split())
belt = list(map(int, input().split()))   # 벨트. 내구도
robot = [False] * N*2

zero = 0
enter, out = 0, N - 1

def move():

    global zero
    # 한 칸 회전 (로봇, 벨트)
    e = belt.pop()
    belt.insert(0, e)
    if robot:
        re = robot.pop()
        robot.insert(0, re)

    # 내리는 칸 검사해서, 있으면 내림
    robot[out] = False

    for i in range(N-2, -1, -1):
        if robot[i] and not robot[i+1] and belt[i+1] > 0:
            robot[i+1] = robot[i]
            robot[i] = False    # 이동
            belt[i+1] -= 1  # 이동 후 내구도 깎기

            if robot[out]:  # 언제든지 내리는 위치에서는 내려지게
                robot[out] = False

    # 올리는 칸의 내구도가 0 이상이면 올리는 위치에 올리기
    if belt[enter] > 0:
        robot[enter] = True
        belt[enter] -= 1

    # 전체 내구도 검사
    zero = belt.count(0)

stage = 1
while zero < K:
    move()

    if zero >= K:
        break
    else:
        stage += 1

print(stage)