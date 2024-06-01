import sys
input  = sys.stdin.readline

N = int(input())
A = list(map(int, input().rstrip().split()))
stack = []
nges = [-1 for _ in range(N)]
for i in range(N-1, -1, -1):
    number = A[i]
    
    if not stack:
        nges[i] = -1
        stack.append(number)
        continue
    
    top = stack[-1]
    if number < top:
        nges[i] = top
    else:
        while stack and stack[-1] <= number:
            stack.pop()

        if stack: nges[i] = stack[-1]
    
    stack.append(number)
    
print(*nges)