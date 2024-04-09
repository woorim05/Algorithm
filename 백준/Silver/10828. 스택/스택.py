import sys

n = int(input())
stack = []
for i in range(n):
    command = sys.stdin.readline().rstrip()
    if command == 'pop':
        print(stack.pop() if stack else -1)
    elif command == 'size':
        print(len(stack))
    elif command == 'empty':
        print(0 if stack else 1)
    elif command == 'top':
        print(stack[-1] if stack else -1)
    else:
        stack.append(int(command.split()[1]))