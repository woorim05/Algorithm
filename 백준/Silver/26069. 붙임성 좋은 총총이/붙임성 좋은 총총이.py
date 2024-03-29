import sys

n = int(sys.stdin.readline())
member = set()
result = 0
for _ in range(n):
    p1, p2 = sys.stdin.readline().rstrip().split()
    if p1 == 'ChongChong' or p2 == 'ChongChong': 
        member.add(p1)
        member.add(p2)
    elif p1 in member:
        member.add(p2)
    elif p2 in member:
        member.add(p1)
print(len(member))