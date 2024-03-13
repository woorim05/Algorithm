a = int(input())
b = [[0 for _ in range(100)] for _ in range(100)]
result = 0
for i in range(a):
    c, d = map(int, input().split())
    for j in range(c-1, c+9):
        for k in range(d-1, d+9):
            b[j][k] = 1

for i in b:
    for j in i:
        result += j

print(result)