count = 0
x = input('Введите строку:')
x2 = ''
for i in x:
    if i == ':':
        count +=1
        x2 += '%'
    else:
        x2 += i
print(count, x2)