import sys
from operator import itemgetter

n = int(sys.stdin.readline())
list = []

for _ in range(n):
    list.append(tuple(map(int, sys.stdin.readline().split())))

newList = sorted(list, key=itemgetter(1, 0))

for i in newList:
    print(i[0], i[1])