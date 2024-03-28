n = int(input())
member = set()
result = 0
for _ in range(n):
    s = input()
    if s == 'ENTER': 
        result += len(member)
        member.clear()
    else:
        member.add(s)
result += len(member)
print(result)