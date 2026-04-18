import random

array = random.sample(range(100), 10)
unique_values = set(array)
for i in range(len(array)):
    for j in range(len(array)):
        if i != j:
            if array[i] == array[j]:
                print(f'Повторение элемента {array[i]} и {array[j]} с индексами {i}, {j}')

    