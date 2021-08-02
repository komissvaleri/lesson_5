
result = {}
with open('text_6.txt', 'r') as file:
    line_6 = file.readlines()
    for line in line_6:
        data = line.split()
        hours = 0
        for el in data[1:]:
            if el != '-':
                num = '0'
                for i in el:
                    if i.isdigit():
                        num += i
                    else:
                        break
                hours += int(num)
        result.update({data[0].strip(':'): hours})
print(result)

