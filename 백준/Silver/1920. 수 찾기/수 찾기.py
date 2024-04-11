n = int(input())
num = set(map(int, input().split()))
m = int(input())
x = list(map(int, input().split()))
for i in x:
    if i in num:
        print(1)
    else:
        print(0)