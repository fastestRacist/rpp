import sys
import math
args_list = sys.argv

array = [int(args_list[i]) for i in range(1, len(args_list))]

sum_elements = sum(array)
prod_elements = math.prod(array)
print(array)
for num in range(len(array)):
    if array[num] == 0:
        array[num] = sum_elements / len(array)
print(sum_elements)
print(prod_elements)
print(array)