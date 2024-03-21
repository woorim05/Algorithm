import sys

n, m = map(int, sys.stdin.readline().split())
a = set()
b = set()
for _ in range(n):
    a.add(sys.stdin.readline().strip())
for _ in range(m):
    b.add(sys.stdin.readline().strip())
result = sorted(a & b)
print(len(result))
print(*result, sep="\n")