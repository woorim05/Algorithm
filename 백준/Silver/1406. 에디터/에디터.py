import sys
input  = sys.stdin.readline

left = list(input().rstrip())
right = []

for _ in range(int(input())) :
    cmd = input().rstrip()
    if cmd == 'L':
        if left: right.append(left.pop())
    elif cmd == 'D':
        if right: left.append(right.pop())
    elif cmd == 'B':
        if left: left.pop()
    else:
        left.append(cmd[-1])

print("".join(left+right[::-1]))