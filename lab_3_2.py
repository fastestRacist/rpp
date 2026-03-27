import sys

args_list = sys.argv
array = []
for i in range(1, len(args_list)):
    array.append(int(args_list[i]))
min_element = min(array)
index_of_min_element = array.index(min_element)
print(f'Массив: {array}, минимальный элемент - {min_element} с индексом {index_of_min_element}')
positive_elements = []
negative_elements = []
for element in array:
    if element >= 0:
        positive_elements.append(element)
    else:
        negative_elements.append(element)
positive_elements_str = ''
negative_elements_str = ''
for i in range(len(array)):
    if i == 0:
        positive_elements_str += str(array[i])
    elif array[i] >= 0:
        positive_elements_str += ' ' + str(array[i])
    else:
        negative_elements_str += ' ' + str(array[i])
print(f'Положительные значения массива: {positive_elements_str}')
print(f'Отрицательные значения массива: {negative_elements_str}')
#доделать 