f = open('books.csv', encoding='utf-8')
k = f.readline()
p = 671
m = 1e9 + 9
mas = list()
for i in f:
    mas.append(i.strip().split(';'))
for i in range(len(mas)):
    mas[i][-1] = mas[i][-1].replace(',', '.', 1)
dictionary = dict()
for i in mas:
    x = i[2].split(',')
    for j in x:
        if j not in dictionary:
            dictionary[j] = [0, 0]
        dictionary[j][0] += (float(i[-1]) * p ** dictionary[j][1]) % m
        dictionary[j][1] += 1
mas2 = [(i, dictionary[i]) for i in dictionary]
mas2.sort(reverse=True, key=lambda x: x[1][0])
for i in range(10):
    print(f'Автор: {mas2[i][0]}, Средний рейтинг: {mas2[i][1][0]}')
