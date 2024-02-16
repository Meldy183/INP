f = open('books.csv', encoding='utf-8')
mas = list()
for i in f:
    mas.append(i.strip().split(';'))
f2 = open('books_rowling.csv', 'w', encoding='utf-8')
f2.write('book_id;authors;original_title;ratings_1\n')
for i in range(len(mas)):
    mas[i][-1] = mas[i][-1].replace(',', '.', 1)
for i in mas:
    if 'Дж.К. Роулинг' in i[2] and float(i[-1]) > 8:
        print(f'{i[2]} - {i[-2]}\t {i[-1]}')
        f2.write(f'{i[0]};{i[2]};{i[-2]};{i[-1]}\n')
