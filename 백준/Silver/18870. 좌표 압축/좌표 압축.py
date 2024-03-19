import sys
import bisect

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

# 중복 없는 리스트로 정렬
sort_num = list(set(numbers))
sort_num.sort()

# 해당 숫자의 인덱스를 프린트
for i in numbers:
    print(bisect.bisect_left(sort_num, i), end=" ")