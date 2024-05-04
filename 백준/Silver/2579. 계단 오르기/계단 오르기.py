import sys
input  = sys.stdin.readline

def up(idx, cnt):
    if dp[cnt][idx] != 0:
        return dp[cnt][idx]
    
    if idx < 0:
        return 0
    
    tmp = []
    
    if cnt + 1 < 2:
        tmp.append(up(idx - 1, cnt + 1))
    
    tmp.append(up(idx - 2, 0))
    dp[cnt][idx] = max(tmp) + stairs[idx]
    
    return dp[cnt][idx]

n = int(input())
stairs = [int(input()) for _ in range(n)]
dp = [[0 for _ in range(n)] for __ in range(2)]
dp[0][0] = stairs[0]

if n == 2:
    print(sum(stairs))
elif n == 3:
    print(max(stairs[0] + stairs[2], stairs[1] + stairs[2]))
else:
    print(up(n - 1, 0))