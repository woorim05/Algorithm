n, k = map(int, input().split())
nums = list(map(int, input().split()))
arr = [sum(nums[0:k])]

for i in range(n - k):
    arr.append(arr[i] - nums[i] + nums[i+k])

print(max(arr))