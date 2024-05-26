from collections import deque
import sys
input  = sys.stdin.readline

N = int(input())
l = int(input())
check = deque(input().rstrip())
a = ''
ans = 0
while check and l > 1:
    temp = a
    cnt = 0
    while temp != 'I' and l > 1:
        temp = check.popleft()
        l -= 1
    
    while check and l > 1:
        a, b = check.popleft(), check.popleft()
        l -= 2
        if a == 'O' and b == 'I':
            cnt += 1
        elif a == 'I' and b == 'O':
            check.appendleft(b)
            l += 1
            break
        else:
            break
    ans += max(cnt - N + 1, 0)

print(ans)