import sys

args_list = sys.argv

array = []
for i in range(1, len(args_list)):
    array.append(int(args_list[i]))
print(array)
odd_index_sum = 0
for i in range(len(array)):
    if i % 2:
        odd_index_sum += array[i]
print(odd_index_sum)
for i in range(len(array)):
    if array[i] < 15:
        array[i] *= 2
print(array)