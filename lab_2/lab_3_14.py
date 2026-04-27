import random

array = random.choices(range(100), k=10)
print(array)
min_idx = array.index(min(array))
max_idx = array.index(max(array))

array[min_idx], array[max_idx] = array[max_idx], array[min_idx]
print(array)
mean_of_array = sum(array) / len(array)
print(mean_of_array)
for i in range(len(array)):
    if array[i] > mean_of_array:
        array[i] = 1
print(array)