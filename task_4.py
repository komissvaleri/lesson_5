
eng_nums = {
    'One': "Один",
    'Two': "Два",
    'Three': "Три",
    'Four': "Четыре",
}
with open('text.txt') as file, open('new_text.txt', 'w') as new_text:
    line_4 = file.readlines()
    for line in line_4:
        data = line.split()
        rus_nums = eng_nums.get(data[0])
        new_text.write(f'{line.replace(data[0], rus_nums)}')

