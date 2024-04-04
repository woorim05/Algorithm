def star(ls, x, y, n):
    k = (n - x) // 3
    
    if k == 1:
        ls[y + 1][x + 1] = ' '
        return ls
    
    for i in range(y + k, y + k * 2 ):
        for j in range(x + k, x + k * 2 ):
            ls[i][j] = ' '
    
    for i in range(3):
        for j in range(3):
            star(ls, (x + k * j), (y + k * i), (x + k * (j + 1)))
    
    return ls        
    
    
n = int(input())
ls = [['*' for _ in range(n)] for _ in range(n)]

for s in star(ls, 0, 0, n):
    print(*s, sep='')