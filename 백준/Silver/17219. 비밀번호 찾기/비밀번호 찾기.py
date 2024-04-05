import sys

n, m = map(int, sys.stdin.readline().split())
memo = {}
for i in range(n):
    a, b = sys.stdin.readline().rstrip().split()
    memo[a] = b

for i in range(m):
    a = sys.stdin.readline().rstrip()
    print(memo[a])