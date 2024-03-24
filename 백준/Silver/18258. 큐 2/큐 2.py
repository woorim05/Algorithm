import sys
from collections import deque

n = int(sys.stdin.readline())
que = deque()
for _ in range(n):
    command = sys.stdin.readline().strip()
    if command == 'pop':
        print(que.popleft() if que else -1)
    elif command == 'size':
        print(len(que))
    elif command == 'empty':
        print(1 if len(que) == 0 else 0)
    elif command == 'front':
        print(que[0] if que else -1)
    elif command == 'back':
        print(que[-1] if que else -1)
    else:
        que.append(int(command.split()[1]))