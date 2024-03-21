import sys
s = sys.stdin.readline().strip()
result = set()
for i in range(1, len(s)):
    for j in range(0, len(s)):
        result.add(s[j:j+i])
print(len(result) + 1)