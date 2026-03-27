import sys

args_list = sys.argv

array = [int(arg) for arg in args_list[1:]]
max_element = max(array)
array_final = []
average = sum(array) / len(array)
for i in range(len(array)):
    if array[i] == 0:
        array_final.append(average)
    else:
        array_final.append(array[i])
print(f'Максимальный элемент: {max_element}')
print(f'Массив в обратном порядке: {array[::-1]}')
print(f'Замена 0 на среднее арифметическое: {array_final}')