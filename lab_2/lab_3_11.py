import sys

args_list = sys.argv

array = [int(args_list[i]) for i in range(1, len(args_list))]
even_array = []
for i in range(len(array)):
    if not array[i] % 2:
        even_array.append(array[i])
max_odd = max(even_array)
print(max_odd)
even_array.sort(reverse=False)
new_odds_array = [x for x in even_array if x < 10]
if new_odds_array:
    print(new_odds_array)
else:
    print('Нет четных чисел меньше 10')