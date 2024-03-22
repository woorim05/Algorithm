import sys
n = int(sys.stdin.readline().strip())
for i in range(n):
    vps = sys.stdin.readline().strip()
    temp = []
    for j in vps:
        if j == '(': temp.append(j)
        else:
            if temp: temp.pop()
            else: print("NO"); break
    else:
        if len(temp) == 0: print("YES")
        else: print("NO")