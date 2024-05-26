from collections import deque
import ast
import sys
input  = sys.stdin.readline

T = int(input())

for _ in range(T):
    cmd = list(input().rstrip())
    n = int(input())
    arr = deque(ast.literal_eval(input().rstrip()))
    rvs = False
    try:
        for c in cmd:
            if c == 'R':
                rvs = not rvs
            else:
                if rvs:
                    arr.pop()
                else:
                    arr.popleft()
        
        if rvs: arr.reverse()
        print("["+",".join(map(str, arr))+"]")
    
    except IndexError:
        print("error")
        