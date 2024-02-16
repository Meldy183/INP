# получает данные об одной книге, а возвращает рекомендовать её или нет в зависимости от рейтинга
def f_r(x: list):
    if float(x[-1]) < 5:
        return 'не рекомендовать'
    if float(x[-1]) >= 8:
        return 'рекомендовать в первую очередь'
    return 'рекомендовать после'


# чтение файла в список и замена запятых в числах на точки для обработки флоат
f = open('books.csv', encoding='utf-8')
x = f.readline()
mas = list()
for i in f:
    mas.append(i.strip().split(';'))
for i in range(len(mas)):
    mas[i][-1] = mas[i][-1].replace(',', '.', 1)
f2 = open('books_grade.csv', 'w', encoding='utf-8')
f2.write(x.strip() + ';recomendations\n')
for i in range(len(mas)):
    string_helper = f_r(mas[i])
    f2.write(f'{";".join(mas[0])};{string_helper}\n')
