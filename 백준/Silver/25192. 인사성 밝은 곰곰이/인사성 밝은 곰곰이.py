n = int(input())
member = []
result = 0
for _ in range(n):
    s = input()
    if s == 'ENTER': 
        result += len(set(member))
        member.clear()
    else:
        member.append(s)
result += len(set(member))
print(result)