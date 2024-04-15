n = int(input())
nums = list(map(int, input().split()))

curr = 0
maximum = -10**8
for num in nums:
    curr = max(curr + num, num)
    maximum = max(maximum, curr)
print(maximum)