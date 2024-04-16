import sys

n, m = map(int, input().split())
arr = list(map(int, input().split()))
sum_list = [0]

for item in arr:
    sum_list.append(sum_list[-1] + item)

for _ in range(m):
    i, j = map(int, sys.stdin.readline().rstrip().split())
    print(sum_list[j] - sum_list[i-1])