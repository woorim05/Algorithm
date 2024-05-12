import sys
input  = sys.stdin.readline

s = input()
q = int(input())

arr = [[0] * 26] # 알파벳 개수

for i in range(len(s)-1): # 누적합
    arr.append(arr[len(arr) - 1][:])
    arr[i + 1][ord(s[i])-97] += 1

for _ in range(q):
    a, l, r = input().split()
    l, r = int(l), int(r)
    
    print(arr[r+1][ord(a)-97] - arr[l][ord(a)-97])