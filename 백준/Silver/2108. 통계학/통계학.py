import sys
import statistics
from collections import Counter

n = int(sys.stdin.readline())
numbers = []
result = 0
for _ in range(n):
    numbers.append(int(sys.stdin.readline().rstrip()))
numbers.sort()

# 산술평균
print(round(statistics.mean(numbers)))

# 중앙값
print(numbers[n//2])

# 최빈값
counter = Counter(numbers)
sorted_counter = sorted(counter.items(), key=lambda x: (-x[1], x[0]))
mode_values = [value for value, count in sorted_counter if count == sorted_counter[0][1]]
if len(mode_values) > 1:
    second_mode_value = mode_values[1]
    print(second_mode_value)
else:
    print(mode_values[0])

# 범위
print(max(numbers) - min(numbers))