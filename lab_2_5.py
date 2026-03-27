x = input('Введите текст: ')
final_x = ''
for i in x:
    final_x += chr(ord(i) + 32)
print(final_x)