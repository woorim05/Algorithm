n = int(input())
a = dict()
b = []
for _ in range(n):
    name, log = map(str, input().split())
    a[name] = log
    
for i in a:
   if a[i] == "enter": b.append(i) 
   
b.sort(reverse=True)
for i in b:
    print(i)