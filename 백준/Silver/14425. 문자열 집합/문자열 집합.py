n, m = map(int, input().split())
a = set([input() for _ in range(n)])
b = [input() for _ in range(m)]
result = 0
for i in b:
    if i in a: result += 1
print(result)    