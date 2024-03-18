from typing import MutableSequence

# 배열을 두 그룹으로 나누기
def partition(a: MutableSequence, left: int, right: int) -> None:
    pl = left                  # 왼쪽 커서
    pr = right                 # 오른쪽 커서
    x = a[(left + right) // 2] # 피벗
    
    while pl <= pr:
        while a[pl] < x: pl += 1
        while a[pr] > x: pr -= 1

        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1
    
    # 재귀
    if left < pr: partition(a, left, pr) 
    if right > pl: partition(a, pl, right)

def quick_sort(a: MutableSequence) -> None:
    partition(a, 0, len(a) - 1)

if __name__ == '__main__':
    num = int(input('원소 수: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input())

    quick_sort(x)

    for i in range(num):
        print(f'x[{i}] = {x[i]}')