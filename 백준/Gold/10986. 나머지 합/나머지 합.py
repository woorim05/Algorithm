import sys
input  = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
remain = [0 for _ in range(m)]
sum = 0
for i in range(n):
    sum += arr[i]
    remain[sum % m] += 1
answer = remain[0]
for v in remain:
    answer += v*(v-1)//2
print(answer)