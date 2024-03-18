from typing import MutableSequence

# 버블정렬
def bubble_sort1(a: MutableSequence) -> None:
    n = len(a)
    for i in range(n - 1): # n-1번 패스 수행 => 원소를 비교하는 총 횟수 = n(n-1)/2
        # 패스
        for j in range(n -1, i, -1):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]


# 교환 횟수에 따른 중단
def bubble_sort2(a: MutableSequence) -> None:
    n = len(a)
    for i in range(n - 1):
        exchng = 0  # 패스에서 교환 횟수
        for j in range(n - 1, i, -1):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]
                exchng += 1
        if exchng == 0: # 패스4에서 교환이 없었으므로 중단. (패스 5, 6이 생략됨)
            break


# 스캔 범위를 제한
def bubble_sort3(a: MutableSequence) -> None:
    n = len(a)
    k = 0
    while k < n - 1:
        last = n - 1 
        for j in range(n - 1, k, -1):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]
                last = j # 마지막으로 교환한 두 원소 중 오른쪽 원소
        k = last

# 셰이커 정렬
def shaker_sort(a: MutableSequence) -> None:
    left = 0
    right = len(a) - 1
    last = right
    while left < right:
        # 뒤에서부터 앞으로 정렬
        for j in range(right, left, -1):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]
                last = j
        left = last
        # 앞에서부터 뒤로 정렬
        for j in range(left, right):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                last = j
        right = last


if __name__ == '__main__':
    num = int(input('원소 수'))
    x = [None] * num

    for i in range(num):
        x[i] = int(input())

    # bubble_sort1(x) # 비교: 21, 교환: 8
    # bubble_sort2(x) # 비교: 18, 교환:8
    # bubble_sort3(x) # 비교: 18, 교환:8
    shaker_sort(x)

    for i in range(num):
        print(f'x[{i}] = {x[i]}')