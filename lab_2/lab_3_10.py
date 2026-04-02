import sys

args_list = sys.argv

array = [int(args_list[i]) for i in range(1, len(args_list))]
seen = set()
duplicates = set()
for num in array:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)
if duplicates:
    print(f"Повторяющиеся элементы: {sorted(duplicates)}")
else:
    print("Повторяющиеся элементы отсутствуют")
array1 = array.copy()
for i in range(len(array1)):
    if array1[i] < 10:
        array1[i] = 0
    elif array1[i] > 20:
        array1[i] = 1
print(f'Первый массив: {array}, Второй массив: {array1}')