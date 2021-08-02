
import random

with open('text_5.txt', 'w') as file:
    for _ in range(20):
        file.write(f'{random.randint(0, 15)} ')

with open('text_5.txt') as file:
    str_nums = file.read().split()
    sum = 0
    for el in str_nums:
        sum += int(el)

print(sum)


