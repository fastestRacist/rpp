x = input('Введите строку: ')
final_x = ''
count = 0
for i in x:
    if i == '.':
        final_x += ''
        count += 1
    else:
        final_x += i

print(f'Замен: {count}\nИтог: {final_x}')