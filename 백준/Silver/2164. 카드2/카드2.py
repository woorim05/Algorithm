import sys
from collections import deque

n = int(sys.stdin.readline())
numbers = deque(range(1, n + 1))
i = 0
while len(numbers) > 1:
    numbers.popleft()
    numbers.rotate(-1)
print(numbers[0])
