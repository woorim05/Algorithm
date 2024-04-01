import sys
from collections import Counter

n, m = map(int, sys.stdin.readline().split())
words = []
for i in range(n):
    s = sys.stdin.readline().rstrip()
    if len(s) >= m:
        words.append(s)

counter = Counter(words)
sorted_words = sorted(counter.items(), key=lambda item: (-item[1], -len(item[0]), item[0]))

for word in sorted_words:
    print(word[0])