import sys

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
numbers.sort()
sum = 0
for i in range(n):
    sum += numbers[i] * (n - i)
print(sum)