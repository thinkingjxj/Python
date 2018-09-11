def fixdown(array, k, n):
    N = n - 1
    while 2 * k <= N:
        j = 2 * k
        if j < N and array[j] < array[j + 1]:
            j += 1
        if array[k] < array[j]:
            array[k], array[j] = array[j], array[k]
            k = j
        else:
            break

def heapsort(l):
    n = len(l) - 1
    for i in range(n // 2, 0, -1):
        fixdown(l, i, len(l))
    while n > 1:
        l[1], l[n] = l[n], l[1]
        fixdown(l, 1, n)
        n -= 1
    return l[1:]

lst = [0, 25, 55, 77, 1, 61, 11, 59, 15, 48, 19]
res = heapsort(lst)
print(res)
