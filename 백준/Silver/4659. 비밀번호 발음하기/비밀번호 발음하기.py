vowel = ['a', 'e', 'i', 'o', 'u']

while True:
    tc = input()
    lst = list(tc)
    if tc == 'end': break

    # 모음 플래그
    acceptable = False
    for s in lst:
        if s in vowel:
            acceptable = True
            break
    if not acceptable:
        print(f"<{tc}> is not acceptable.")
        continue

    # 모음, 자음 연속 검사
    if len(tc) >= 3:
        for i in range(len(tc)-2):
            f = lst[i:i+3]
            if (f[0] in vowel and f[1] in vowel and f[2] in vowel) or (f[0] not in vowel and f[1] not in vowel and f[2] not in vowel):
                acceptable = False
                break
        if not acceptable:
            print(f"<{tc}> is not acceptable.")
            continue

    # 연속 글자 검사
    if len(tc) > 1:
        for i in range(len(tc)-1):
            f = lst[i:i+2]
            if (f[0] == f[1]) and (f != ['e', 'e'] and f != ['o', 'o']):
                acceptable = False
                break

    if not acceptable:
        print(f"<{tc}> is not acceptable.")
        continue

    print(f"<{tc}> is acceptable.")