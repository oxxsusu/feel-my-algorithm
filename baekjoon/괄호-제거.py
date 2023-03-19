import sys
from itertools import *

_str = list(enumerate(sys.stdin.readline().rstrip()))
stack, brc = [], []

for s in _str:
    if s[1] == '(':
        stack.append(s)
    elif s[1] == ')':
        brc.append([stack.pop()[0], s[0]])

count = 1
if not brc:
    print(''.join([s[1] for s in _str]))
else:
    print_list = []
    while count <= len(brc):
        for c in combinations(brc, count):
            c_list = []
            new_s = ''
            for i in c:
                c_list += i
            for s in _str:
                if s[0] not in c_list:
                    new_s += s[1]
            print_list.append(''.join(new_s))
        count += 1

    for p in set(sorted(print_list)):  # 중복제거...
        print(p)
