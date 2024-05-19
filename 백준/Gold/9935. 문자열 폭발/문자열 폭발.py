import sys
input  = sys.stdin.readline

s = input().rstrip()
bomb = list(input().rstrip())
n = len(bomb)
stack = []
for c in s:
    stack.append(c)
    if stack[-n:] == bomb:
        for _ in range(n):
            stack.pop()

print(''.join(stack) if stack else 'FRULA')