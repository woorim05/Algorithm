n = int(input())

for i in range(1, n+1):
    digitSum = sum((map(int, str(i))))
    if i + digitSum == n:               
        print(i)
        break
    if i == n: print(0)