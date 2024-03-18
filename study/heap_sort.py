from typing import MutableSequence

# heap 정렬
def heap_sort(a: MutableSequence) -> None:
    
    def down_heap(a: MutableSequence, left: int, right: int) -> None:
        # a[left] ~ a[right]를 힙으로 만들기
        tmp = a[left]
        parent = left
        while parent < (right + 1) // 2:
            cl = parent * 2 + 1     # 왼쪽 자식
            cr = cl + 1             # 오른쪽 자식
            child = cr if cr <= right and a[cr] > a[cl] else cl
            if tmp >= a[child]:
                break
            a[parent] = a[child]
            parent = child
        a[parent] = tmp

    n = len(a)

    for i in range((n - 1) // 2, -1, -1):
        down_heap(a, i , n - 1)
    
    for i in range(n - 1, 0, -1):
        a[0], a[i] = a[i], a[0]
        down_heap(a, 0, i - 1)


if __name__ == '__main__':
    num = int(input('원소 수: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input())

    heap_sort(x)

    for i in range(num):
        print(f'x[{i}] = {x[i]}')