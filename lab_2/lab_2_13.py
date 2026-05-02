text = input('Введите строку:')
while '(' not in text or ')' not in text:                
    text = input('Введите строку:')

start = text.find('(')
end = text.find(')', start)

if end != -1:
    content = text[start + 1 : end]
    print(f"Содержимое: {content}")
else:
    print("Закрывающая скобка не найдена")