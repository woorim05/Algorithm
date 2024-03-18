n = int(input())
txt = []

for _ in range(n):
    txt.append(input())

txt = list(set(txt))
txt.sort(key=lambda x: (len(x), x))

for i in txt:
    print(i)