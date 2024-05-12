import sys
input  = sys.stdin.readline

def dfs(idx, rst, p, s, m, d):
    global mx, mn
    
    if -10**9 > rst or rst > 10**9:
        return
    
    if idx == n:
        mx = max(mx, rst)
        mn = min(mn, rst)
        return
    
    if p > 0:
        dfs(idx + 1, rst + arr[idx], p-1, s, m, d)
    if s > 0:
        dfs(idx + 1, rst - arr[idx], p, s-1, m, d)
    if m > 0:
        dfs(idx + 1, rst * arr[idx], p, s, m-1, d)
    if d > 0:
        dfs(idx + 1, int(rst/arr[idx]), p, s, m, d-1)

n = int(input())
arr = list(map(int, input().split()))
p, s, m, d = map(int, input().split())
mx, mn = -10**9, 10**9
dfs(1, arr[0], p, s, m, d)
print(mx)
print(mn)