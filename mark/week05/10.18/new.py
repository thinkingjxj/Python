def heap_adjust(n, i, array):
    while 2 * i < n:
        lchild_index = 2 * i
        max_child_index = lchild_index
        if n > lchild_index and array[lchild_index + 1] > array[lchild_index]:
            max_child_index = lchild_index + 1
        if array[max_child_index] > array[i]:
            array[max_child_index], array[i] = array[i], array[max_child_index]
            i = max_child_index
        else:
            break
def heapsort(total, array):
    for i in range(total // 2, 0, -1):
        heap_adjust(total, i, array)
    return array

lst = [0,3,2,8,4,5,1,6,7,9]
new = heapsort(10,lst)
print(new)

