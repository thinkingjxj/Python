import math


def print_tree(array, unit_width=2):
    length = len(array)
    depth = math.ceil(math.log2(length + 1))

    index = 0
    width = 2 ** depth - 1
    for i in range(depth):
        for j in range(2 ** i):
            print('{:^{}}'.format(array[index], width * unit_width),
                  end=' ' * unit_width)
            index += 1
            if index >= length:
                break
        width = width // 2
        print()


print_tree([x + 1 for x in range(9)])

origin = [0, 3, 2, 8, 4, 5, 1, 6, 7, 9]
total = len(origin) - 1
print(origin)
print_tree(origin)


def heap_adjust(n, i, array: list):
    while 2 * i <= n:
        lchild_index = 2 * i
        max_child_index = lchild_index
        if n > lchild_index and array[lchild_index + 1] > array[i]:
            max_child_index = lchild_index + 1
        if array[max_child_index] > array[i]:
            array[i], array[max_child_index] = array[max_child_index], array[i]
            i = max_child_index
        else:
            break
        print_tree(array)


heap_adjust(total, total // 2, origin)
print(origin)
print_tree(origin)


def max_heap(total, array: list):
    for i in range(total // 2, 0, -1):
        heap_adjust(total, i, array)
    return array
