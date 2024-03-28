import sys

n = int(sys.stdin.readline())
member = set()
result = 0
for _ in range(n):
    s = sys.stdin.readline().rstrip()
    if s == 'ENTER': 
        member.clear()
    elif s not in member:
        member.add(s)
        result += 1
print(result)