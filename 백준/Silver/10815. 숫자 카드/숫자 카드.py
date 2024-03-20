import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))
arr = [0] * (20000000 + 1)

for i in a:
    arr[i + 10000000] = 1

for i in b:
    print(arr[i + 10000000], end=" ")