classe = list()
while True:
    nome = str(input("Nome: "))
    mat = float(input("Matematica: "))
    port = float(input("Português: "))
    geo = float(input("Geografia: "))
    hist = float(input("Historia: "))
    filo = float(input("Filofia: "))
    quim = float(input("Quimica: "))
    fis = float(input("Fisica: "))
    media = (mat + port + geo + hist + filo + quim + fis) / 7
    classe.append([nome, [mat, port, geo, hist, filo, quim, fis],media])
    continuar = str(input("Quer continuar? [S/N]"))
    if continuar in 'Nn' :
        break
print('*' *30)
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
print('-' *22)
for i, a in enumerate(classe):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
