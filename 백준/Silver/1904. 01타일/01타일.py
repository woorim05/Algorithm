def fibonacci(n):
    f = [0] * (n + 1)
    f[1] = 1
    f[2] = 2
    for i in range(3, n + 1):
        f[i] = (f[i - 1] + f[i - 2]) % 15746
    return f[n]
    
n = int(input())
if n <= 2:
    print(n)
else:
    print(fibonacci(n))
