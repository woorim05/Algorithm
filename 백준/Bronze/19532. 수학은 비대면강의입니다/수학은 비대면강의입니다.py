a, b, c, d, e, f = map(int, input().split())
flag = False
resultX, resultY = 0, 0
for x in range(-999, 1000):
    for y in range(-999, 1000):
        if (a*x + b*y == c) and (d*x + e*y == f):
            flag = True
            resultX, resultY = x, y
            break
    if flag: break
print(resultX, resultY)