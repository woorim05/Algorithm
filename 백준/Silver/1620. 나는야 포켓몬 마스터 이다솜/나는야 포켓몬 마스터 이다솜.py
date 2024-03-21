import sys
n, m = map(int, sys.stdin.readline().split())
pocketmons_list = []
pocketmons_dict = {}
for i in range(n):
    s = sys.stdin.readline().strip()
    pocketmons_list.append(s)
    pocketmons_dict[s] = i
    
for _ in range(m):
    q = sys.stdin.readline().strip()
    if q.isdigit():
        print(pocketmons_list[int(q)-1])
    else:
        print(pocketmons_dict[q]+1)        
