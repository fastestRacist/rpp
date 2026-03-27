text = input('Введите строку: ')
text = text + ' '
count = 0
for i in range(len(text)):
    if not text[i].isalpha() and text[i-1].isalpha():
        count += 1
print(count)