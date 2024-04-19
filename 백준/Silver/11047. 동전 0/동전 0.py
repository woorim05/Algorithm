import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
cnt = 0
coins.sort(reverse=True)
for coin in coins:
    if k >= coin:
        cnt += (k // coin)
        k %= coin
print(cnt)