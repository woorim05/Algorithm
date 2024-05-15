import sys
input  = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
result = 0
curr = b[0]
min_city = min(b)

for i in range(n - 1):
    result += curr * a[i]
    if b[i + 1] < curr and curr != min_city:
        curr = b[i + 1]
            
print(result) 