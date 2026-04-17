import sys
import random

args_list = sys.argv

array = [int(args_list[i]) for i in range(1, len(args_list))]
array = array[:10]
print(array)
odds_array = [x for x in array if x % 2 != 0]
print(min(odds_array))

array_b = random.sample(range(1,100), 10)
print(array_b)

array, array_b = array_b, array

print(array, '\n', array_b)