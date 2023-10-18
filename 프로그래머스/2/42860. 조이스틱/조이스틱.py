def solution(name):
    answer = 0    # 디폴트 : 오른쪽 끝까지 이동
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    horizon = len(name)-1
    for idx, char in enumerate(name):
        if alpha.index(char) < 13: answer += alpha.index(char)
        else: answer += 26 - alpha.index(char)

        not_a = idx + 1
        while not_a < len(name) and name[not_a] == 'A': not_a += 1
        horizon = min([horizon, 2 *idx + len(name) - not_a, idx + 2 * (len(name) - not_a)])
    answer += horizon
    return answer