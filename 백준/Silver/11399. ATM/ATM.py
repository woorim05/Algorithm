import sys

n = int(sys.stdin.readline())
numbers = sorted(list(map(int, sys.stdin.readline().split())))
sum = 0
for i in range(n):
    sum += numbers[i] * (n - i)
print(sum)