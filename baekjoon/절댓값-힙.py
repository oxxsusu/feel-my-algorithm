import sys
from heapq import *

N = int(sys.stdin.readline().rstrip())
_list = [int(sys.stdin.readline().rstrip()) for i in range(N)]
heap = []

for n in _list:
    if n == 0:
        if not heap:
            print(0)
        else:
            print(heappop(heap)[1])
    else:
        heappush(heap, (abs(n), n))
