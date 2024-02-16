def msort(x: list):
    if len(x) < 2:
        return x
    result = []
    mid = int(len(x) / 2)
    y = msort(x[:mid])
    z = msort(x[mid:])
    i = 0
    j = 0
    while i < len(y) and j < len(z):
        if float(y[i][-1]) > float(z[j][-1]):
            result.append(z[j])
            j += 1
        else:
            result.append(y[i])
            i += 1
    result += y[i:]
    result += z[j:]
    return result


f = open('books.csv', encoding='utf-8')
f.readline()
mas = list()
for i in f:
    mas.append(i.strip().split(';'))
for i in range(len(mas)):
    mas[i][-1] = mas[i][-1].replace(',', '.', 1)
mas = msort(mas)
for i in range(3):
    print(f'{mas[i][-2]} - {mas[i][2]} - {mas[i][-1]}')
