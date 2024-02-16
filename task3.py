f = open('books.csv', encoding='utf-8')
f.readline()
mas = list()
for i in f:
    mas.append(i.strip().split(';'))
s = input()  # Названия писать строго в соответствии с регистром
while s != 'хватит':
    cnt = 0
    for i in mas:
        if s in i[-2]:
            if cnt == 5:
                print('и др.')
                break
            print(f'{i[-2]} - {i[1]} - {i[0]} - {i[-1]}')
            cnt += 1
    if cnt == 0:
        print('Данной книги в этой библиотеке нет')
    s = input()