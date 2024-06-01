import sys
input  = sys.stdin.readline

N = int(input())
A = list(map(int, input().rstrip().split()))
stack = []
nges = [-1] * N

for i in range(N):
    while stack and A[stack[-1]] < A[i]:
        nges[stack.pop()] = A[i]
    stack.append(i)
print(*nges)
