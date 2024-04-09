def dfs():
    if len(numbers) == m:
        print(*numbers)
        return
    
    for i in range(1, n + 1):
        if not numbers or (numbers and i >= numbers[-1]):
            numbers.append(i)
            dfs()
            numbers.pop()

n, m = map(int, input().split())
numbers = []
dfs() 