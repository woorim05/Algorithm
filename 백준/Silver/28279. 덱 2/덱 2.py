import sys
from collections import deque

n = int(sys.stdin.readline())
deq = deque()

for _ in range(n):
    command = sys.stdin.readline().split()
    if command[0] == '1':
        deq.appendleft(int(command[1]))
    elif command[0] == '2':
        deq.append(int(command[1]))
    elif command[0] == '3':
        print(deq.popleft() if deq else -1)
    elif command[0] == '4':
        print(deq.pop() if deq else -1)
    elif command[0] == '5':
        print(len(deq))
    elif command[0] == '6':
        print(0 if deq else 1)
    elif command[0] == '7':
        print(deq[0] if deq else -1)
    else:
        print(deq[-1] if deq else -1)