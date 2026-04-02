text = input('Введите строку: ')
final_text = ''
g_count = 0
g_count_max = 0
for i in text:
    if i == '.':
        final_text += '!'
    else:
        final_text += i
    if i == 'g':
        g_count += 1
        if g_count > g_count_max:
            g_count_max = g_count
    else:
        g_count = 0
print(f"Результат: {final_text}")
print(f"Максимальная последовательность 'g': {g_count_max}")