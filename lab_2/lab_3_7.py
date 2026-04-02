import sys

args_list = sys.argv

array = [int(args_list[i]) for i in range(1, len(args_list))]

even_sum = 0
odds_prod = 1
max_element = max(array)
min_element = min(array)
max_index = array.index(max_element)
min_index = array.index(min_element)

for i in range(len(array)):
    if not i % 2:
        even_sum += array[i]
    else:
        odds_prod *= array[i]

array[max_index], array[min_index] = array[min_index], array[max_index]

print(array,'\n',even_sum,'\n',odds_prod)