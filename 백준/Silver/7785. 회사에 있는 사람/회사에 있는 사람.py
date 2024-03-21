n = int(input())
a = dict()
b = []
for _ in range(n):
    name, log = map(str, input().split())
    if log == 'enter': a[name] = 1
    else: a[name] = 0
    
for i in a:
   if a[i] == 1: b.append(i) 
   
b.sort(reverse=True)
for i in b:
    print(i)