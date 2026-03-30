import sys

args_list = sys.argv

array = [int(args_list[i]) for i in range(1, len(args_list))]

max_element = max(array)
count = 0
sum = 0
for i in range(len(array)):
    if array[i] < max_element:
        count +=1
    elif array[i] > 5:
        sum += array[i]
print(f'{array}\n{max_element}\n{count}\n{sum}')