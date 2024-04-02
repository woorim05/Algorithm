def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)

def merge(A, p, q, r):
    global count, result
    
    i = p
    j = q + 1
    tmp = []

    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp.append(A[i])
            i += 1
        else:
            tmp.append(A[j])
            j += 1

    while i <= q:
        tmp.append(A[i])
        i += 1

    while j <= r:
        tmp.append(A[j])
        j += 1

    i = p
    for val in tmp:
        count += 1
        if count == k: result = val
        A[i] = val
        i += 1
        
count = 0
result = 0
n, k = map(int, input().split())
arr = list(map(int, input().split()))
merge_sort(arr, 0, len(arr) - 1)
print(-1 if count < k else result)