import sys
input  = sys.stdin.readline

s= input().rstrip()
minus = s.split('-')
result = sum(map(int, minus[0].split('+')))
for i in minus[1:]:
	result -= sum(map(int, i.split('+')))
print(result)