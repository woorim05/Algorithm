n, m = map(int, input().split())
a = set()
b = set()
for _ in range(n):
    a.add(input())
for _ in range(m):
    b.add(input())
result = sorted(a & b)
print(len(result))
print(*result, sep="\n")