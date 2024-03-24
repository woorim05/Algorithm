import sys

while True:
    vps = sys.stdin.readline().rstrip()
    temp = []
    
    if vps == '.': break
    
    if '(' not in vps and ')' not in vps and '[' not in vps and ']' not in vps:
        print("yes")
        continue
    
    for j in vps:
        if j == '(':
            temp.append(j)
        elif j == ')':
            if temp: 
                if temp.pop() != '(':
                    print("no"); break
            else: print("no"); break
        
        if j == '[':
            temp.append(j)
        elif j == ']':
            if temp:
                if temp.pop() != '[':
                    print("no"); break
            else: print("no"); break
        
    else:
        if len(temp) == 0:
            print("yes")
        else: print("no")