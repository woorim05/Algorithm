from typing import MutableSequence

# 단순 선택 정렬
def selection_sort(a: MutableSequence) -> None:
    n = len(a)
    for i in range(n - 1):
        min = i
        for j in range(i + 1, n):
            if a[j] < a[min]:
                min = j
        a[i], a[min] = a[min], a[i]

        
if __name__ == '__main__':
    num = int(input('원소 수'))
    x = [None] * num

    for i in range(num):
        x[i] = int(input())

    selection_sort(x)

    for i in range(num):
        print(f'x[{i}] = {x[i]}')