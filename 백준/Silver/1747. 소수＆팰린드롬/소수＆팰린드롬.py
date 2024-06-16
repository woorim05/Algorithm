import sys
import math
input  = sys.stdin.readline

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

N = int(input())
while True:
    if str(N) == str(N)[::-1]:
        if is_prime(N):
            print(N)
            break
    N += 1
