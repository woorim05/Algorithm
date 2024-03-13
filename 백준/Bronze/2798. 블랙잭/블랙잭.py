n, m = map(int, input().split())
cards = list(map(int,input().split()))
results = []
for i, v in enumerate(cards):
    for j, v2 in enumerate(cards[(i+1):], start=i+1):
        for k, v3 in enumerate(cards[(j+1):], start=j+1):
            sum = v + v2+ v3
            if sum <= m: results.append(sum)
print(max(results))
