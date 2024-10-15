def heapify(unsorted, index, heap_size):
    largest = index
    left = 2 * index + 1
    right = 2 * index + 2

    if left < heap_size and unsorted[left] > unsorted[largest]:
        largest = left

    if right < heap_size and unsorted[right] > unsorted[largest]:
        largest = right
    
    if largest != index:
        unsorted[largest], unsorted[index] = unsorted[index], unsorted[largest]
        heapify(unsorted, largest, heap_size)

def heap_sort(unsorted):
    n = len(unsorted)

    for i in range(n//2-1, -1, -1):
        heapify(unsorted, i, n)

    return unsorted

import sys

N = int(sys.stdin.readline())

data_list = []
for _ in range(N):
    data = int(input())
    data_list.append(data)

array = []

answer = []
for i in data_list:
    if i == 0:
        sorted = heap_sort(array)
        if len(sorted) == 0:
            answer.append(0)
        else:
            answer.append(sorted[0])
            array = sorted[1:]
    else:
        array.append(i)

print('\n'.join(map(str, answer)))