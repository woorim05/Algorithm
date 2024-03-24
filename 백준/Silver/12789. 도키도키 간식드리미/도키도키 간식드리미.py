import sys

n = int(sys.stdin.readline())
lines = list(map(int, sys.stdin.readline().split()))
lines.reverse()
tmp = []
num = 1
while num <= n:
    if tmp:
        if not lines and num != tmp[-1]:
            break
        if num == tmp[-1]:
            num += 1
            tmp.pop()
            continue
    if lines:
        if num == lines[-1]:
            num += 1
            lines.pop()
            continue
        else:
            tmp.append(lines.pop())
        
            
if tmp or lines:
    print("Sad")
else:
    print("Nice")