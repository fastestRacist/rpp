text = input('Введите текст: ')
final_text = ''
count = 0
for i in text:
    if i == 'a':
        final_text += ''
        count += 1
    else:
        final_text += i
print(count, final_text)