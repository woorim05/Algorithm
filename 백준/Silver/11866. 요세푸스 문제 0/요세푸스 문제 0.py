import sys

n, k = map(int, sys.stdin.readline().split())
idx = 0
people = list(range(1, n + 1))
josephus = []
while len(people) > 1:
    idx = (idx + k - 1) % len(people)
    josephus.append(people.pop(idx))
josephus.append(people[0])
print('<' + ', '.join(map(str, josephus)) + '>')