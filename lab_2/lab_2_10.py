text = input('Введите строку: ')
text = text + ' '
final_text = ''
for i in range(len(text)):
    if not text[i-1].isalpha() and text[i].isalpha():
        final_text += chr(ord(text[i]) - 32)
    else:
        final_text += text[i]
print(final_text)