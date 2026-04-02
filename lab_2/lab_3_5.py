import sys


args_list = sys.argv
array = []
for i in range(1, len(args_list)):
    array.append(int(args_list[i]))
print(array)

for i, char in enumerate(array):
    if char < 0 and array[i-1] < 0:
        print(f'Пара: ({char}, {array[i-1]})')

uniqe_array = (set(array))
uniqe_array = [x for x in uniqe_array]
print(uniqe_array)