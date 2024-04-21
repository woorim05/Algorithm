import sys
input = sys.stdin.readline

n = int(input())
times = [list(map(int, input().split())) for _ in range(n)]
times.sort(key = lambda x: (x[1], x[0]))
end = 0
cnt = 0

for i in range(n):
    if times[i][0] >= end:
        end = times[i][1]
        cnt += 1
        
print(cnt)