from typing import MutableSequence

# shell 정렬
def shell_sort(a: MutableSequence) -> None:
    n = len(a)
    h = n // 2
    while h > 0:
        for i in range(h, n):
            j = i - h
            tmp = a[i]
            while j >= 0 and a[j] > tmp:
                a[j + h] = a[j]
                j -= h
            a[j + h] = tmp
        h //= 2


# shell 정렬 초기값
def shell_sort(a: MutableSequence) -> None:
    n = len(a)

    # h값이 배수가 되면 그룹으로 나누어 정렬한 후 합치면 다시 처음 단계와 같아져 그룹의 의미가 무의미해짐
    # => h값이 서로 배수가 되지 않아야 함. => 원소가 충분히 뒤섞이므로 효율 좋은 정렬 가능
    # h의 초기값: 지나치케 크면 효과 X. 원소 수를 9로 나누었을 때 몫을 넘지 않도록 권장됨
    h = 1
    while h < n // 9:
        h = h * 3 + 1

    while h > 0:
        for i in range(h, n):
            j = i - h
            tmp = a[i]
            while j >= 0 and a[j] > tmp:
                a[j + h] = a[j]
                j -= h
            a[j + h] = tmp
        h //= 3

if __name__ == '__main__':
    num = int(input('원소 수'))
    x = [None] * num

    for i in range(num):
        x[i] = int(input())

    shell_sort(x)

    for i in range(num):
        print(f'x[{i}] = {x[i]}')