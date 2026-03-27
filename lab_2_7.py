text = input('Введите произвольную строку: ')
count = 0
result = ''
for i in range(len(text)):
    if i < len(text) // 2 and text[i] == '!':
        result += '%'
        count += 1
    else:
        result += text[i]
print('Результат: ', result)
print('Количество замен: ', count)