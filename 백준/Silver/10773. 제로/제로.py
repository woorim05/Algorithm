import sys
n = int(sys.stdin.readline().strip())
stack = []
for i in range(n):
    k = int(sys.stdin.readline().strip())
    if k == 0: stack.pop()
    else: stack.append(k)
print(sum(stack))