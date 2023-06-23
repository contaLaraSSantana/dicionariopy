d = {}

while True:
    a = str(input('Digite a chave: '))
    d[a]=str(input('Digite o valor: '))
    res = str(input('Deseja continuar S/N: '))
    if res in 'N':
        break
print(d)
