import random
n = random.randint(5, 10)
array = random.choices(range(100), k = n)
print(array)
new_array = []
for i in range(len(array)):
    if array[i] < 10:
        new_array.append(array[i])
print(new_array)
for i in range(len(array)):
    if i % 2 == 0:
        array[i] = array[i] * 2
print(array)