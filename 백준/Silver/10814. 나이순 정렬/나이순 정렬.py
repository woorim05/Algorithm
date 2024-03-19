import sys
from operator import itemgetter

n = int(sys.stdin.readline())
list = []

for _ in range(n):
    a, b = map(str, sys.stdin.readline().split())
    list.append((int(a), b))

list.sort(key=itemgetter(0))

for i in list:
    print(i[0], i[1])