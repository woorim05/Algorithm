def cantorian(n, count, result):
    space = ' ' * (3 ** (count-1))
    result += space + result

    if count == n:
        return result

    if len(result) == 3**count:
        count += 1
    return cantorian(n, count, result)

while True:
    try:
        n = int(input())
        if n == 0:
            print('-')
        else:
            print(cantorian(n, 1, '-'))
    except EOFError:
        break
