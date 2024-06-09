import sys
input  = sys.stdin.readline

N, K = map(int, input().split())
dp = [[0] * (K+1) for _ in range(N+1)]
things = [[0, 0]]
for _ in range(N):
    things.append(list(map(int, input().split())))

for i in range(1, N+1):
    for j in range(1, K+1):
        if j - things[i][0] < 0:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(things[i][1] + dp[i-1][j-things[i][0]], dp[i-1][j])
            
print(dp[-1][-1])