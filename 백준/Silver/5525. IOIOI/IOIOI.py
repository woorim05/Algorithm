import sys
input  = sys.stdin.readline

N = int(input())
M = int(input())
S = input().rstrip()
form = 2*N+1
cnt = 0
check = ''
for i in range(1,form+1):
    if i % 2 !=0:
        check+='I'
    else:
        check+='O'

for i in range(M):
    if S[i:i+form] == check:
        cnt+=1

print(cnt)