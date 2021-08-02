
with open('text.txt', 'w') as file:
    line_1 = input('Введите текст: \n')
    while line_1:
        file.write(f'{line_1}\n')
        line_1 = input('Введите текст: \n')

