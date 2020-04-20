import random

size = 10
array = [i for i in range(10)]
random.shuffle(array)
print(array)

# n = 1
# while n < len(array):
#     for i in range(len(array) - 1):
#         if array[i] > array[i + 1]:
#             array[i], array[i + 1] = array[i + 1], array[i]
#     n += 1
# print(array)

def selection_sort(array):
    for i in range(len(array)):
        idx_min = i
        for j in range(i + 1, len(array)):
            if array[j] < array[idx_min]:
                idx_min = j
        array[idx_min], array[i] = array[i], array[idx_min]

selection_sort(array)
print(array)