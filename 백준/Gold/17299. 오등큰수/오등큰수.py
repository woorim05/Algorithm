import sys
input  = sys.stdin.readline

N = int(input())
A = list(map(int, input().rstrip().split()))
F = [0] * 1000001

for i in A:
    F[i] += 1

stack = []
ngfs = [-1] * N

for i in range(N):
    while stack and F[A[stack[-1]]] < F[A[i]]:
        ngfs[stack.pop()] = A[i]
    stack.append(i)
    
print(*ngfs)