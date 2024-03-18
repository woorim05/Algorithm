from typing import MutableSequence

# 단순 삽입 정렬
def insertion_sort(a: MutableSequence) -> None:
    n = len(a)
    for i in range(n - 1):
        j = i
        tmp = a[i]
        while j > 0 and a[j - 1] > tmp:
            a[j] = a[j - 1]
            j -= 1
        a[j] = tmp

        
if __name__ == '__main__':
    num = int(input('원소 수'))
    x = [None] * num

    for i in range(num):
        x[i] = int(input())

    insertion_sort(x)

    for i in range(num):
        print(f'x[{i}] = {x[i]}')