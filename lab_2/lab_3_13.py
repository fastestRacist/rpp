import random

array = random.choices(range(100), k=10)
for i in range(len(array)):
    for j in range(len(array)):
        if i != j:
            if array[i] == array[j]:
                print(f'Повторение элемента {array[i]} и {array[j]} с индексами {i}, {j}')

new_array = []
for i in range(len(array)):
    if array[i] < 15:
        new_array.append(array[i]*2)
    else:
        new_array.append(array[i])
print(array)
print(new_array)