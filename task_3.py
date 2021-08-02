
with open('text.txt') as file:
    line_3 = file.readlines()
    sotr = {}
    oplat = 0
    for line in line_3:
        sot_info = line.split()
        sotr.update({sot_info[0]: float(sot_info[1])})
        oplat += float(sot_info[1])
    sredn = oplat / len(sotr)
    print(f'Средняя зарплата =  {sredn}')
    for el, el_1 in sotr.items():
        if el_1 > sredn:
            print(f'{el}: {el_1}')


