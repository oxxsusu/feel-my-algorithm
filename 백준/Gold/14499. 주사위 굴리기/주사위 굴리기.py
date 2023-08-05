# 윗면이 1인경우, 2인경우, 5, 6인 경우에 따라서...

n, m, x, y, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
move = list(map(int, input().split()))

dice = [0]*6    # 주사위 위치별 수 기록
ew, ns, f = [3, 0, 2], [1, 0, 4], 5     # 초기 주사위 포인터

def roll(command): # 이동명령번호, 현재 동서방향, 남북방향, 바닥포인터
    global f, x, y

    if command==1:  # 동쪽
        ny = y+1
        if 0 <= ny < m: y = ny
        else: return  # 벗어나면 명령 무시
        temp = f    # 바닥 값 저장해놓고
        f = ew.pop()    # 새로운 바닥값
        ew.insert(0, temp) # 바닥값 앞에 끼워넣고
        ns[1] = ew[1]   # ns 중간값 바꿔줌
    elif command==2:    # 서쪽
        ny = y-1
        if 0 <= ny < m: y = ny
        else: return
        temp = f
        f = ew.pop(0)   # 앞자리가 새로운 바닥값이 됨
        ew.append(temp)
        ns[1] = ew[1]   # ns 중간값
    elif command==3:    # 북쪽
        nx = x-1
        if 0 <= nx < n: x = nx
        else: return
        temp = f
        f = ns.pop(0)
        ns.append(temp)
        ew[1] = ns[1]
    elif command==4:
        nx = x+1
        if 0 <= nx < n: x = nx
        else: return
        temp = f
        f = ns.pop()
        ns.insert(0, temp)
        ew[1] = ns[1]

    # 바닥면에 복사
    copy(x, y)

    # 윗면 출력
    upper_ptr = ew[1]
    print(dice[upper_ptr])

def copy(x, y):
    if grid[x][y] == 0:
        grid[x][y] = dice[f]    # 지도에 주사위 복사
    else:
        dice[f] = grid[x][y]
        grid[x][y] = 0  # 칸에 쓰여있는 수는 0이 된다... 여길 빼먹음 ㅡㅡ

# 초기 주사위 위치에서 복사
copy(x, y)

for command in move:
    roll(command)    # 주사위 굴리가