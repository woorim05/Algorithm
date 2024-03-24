import sys

while True:
    vps = sys.stdin.readline().rstrip()
    temp = []
    
    if vps == '.': break
    
    if '(' not in vps and ')' not in vps and '[' not in vps and ']' not in vps:
        print("yes")
        continue
    
    for j in vps:
        if j == '(' or j == '[':
            temp.append(j)
        elif j == ')':
            if not temp or temp.pop() != '(': 
                print("no"); break
        elif j == ']':
            if not temp or temp.pop() != '[': 
                print("no"); break
    else:
        if len(temp) == 0:
            print("yes")
        else: print("no")