import sys

t = int(input())

for i in range(t):
    n = int(sys.stdin.readline().rstrip())
    f = [0] * (n + 1)

    if n <= 3: print(1)
    elif n <= 5: print(2)
    else:
        f[1], f[2], f[3] = 1, 1, 1
        f[4], f[5] = 2, 2 
        for i in range(6, n + 1):
            f[i] = f[i - 2] + f[i - 3]
        print(f[n])
