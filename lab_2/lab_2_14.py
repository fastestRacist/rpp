text = input('Введите строку: ')
count = 0
text = text + ' '
for i in range(len(text)):
    if not text[i].isalpha() and text[i-1] == 'u':
        count += 1
print(count)