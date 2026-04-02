text = input("Введите строку: ")
text = text + ' '
count = 0
for i in range(len(text)):
    if text[i].isalpha() and not text[i-1].isalpha():
        if text[i] == 'm':
            count += 1
print(f"Количество слов, начинающихся с буквы 'm': {count}")