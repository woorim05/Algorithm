n = int(input())
cards = list(map(int, input().split()))
m = int(input())
numbers = list(map(int, input().split()))
count = {}

for i in cards:
    if i in count: count[i] += 1
    else: count[i] = 1
    
for i in numbers:
    if i in count:
        print(count[i], end=" ")
    else: print(0, end=" ")