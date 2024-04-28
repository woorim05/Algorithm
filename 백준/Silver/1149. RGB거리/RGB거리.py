import sys
input  = sys.stdin.readline

n = int(input())
rgb = [list(map(int, input().split())) for _ in range(n)]
dp = [[0, 0, 0] for _ in range(n)]
dp[0] = rgb[0]
    
for i in range(1, n):
    for j in range(0, 3):
        minimum = 1000000
        for k in range(0, 3):
            if j == k:
                continue
            if dp[i - 1][k] < minimum:
                minimum = dp[i - 1][k]
            dp[i][j] = minimum + rgb[i][j]
print(min(dp[n - 1])) 
