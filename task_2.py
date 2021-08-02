
with open('text.txt') as file:
    line_2 = file.readlines()
    for el, line in enumerate(line_2):
        text_count = len(line.split())
        print(f'строка №{el + 1} - {text_count} слова')

