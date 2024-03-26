import sys
from collections import deque

n = int(sys.stdin.readline())
balloons = deque(enumerate(map(int, sys.stdin.readline().split()), start=1))
result = []

while balloons:
    idx, value = balloons.popleft()
    result.append(idx)

    if value > 0:
        balloons.rotate(-value + 1)
    else:
        balloons.rotate(-value)

print(*result)